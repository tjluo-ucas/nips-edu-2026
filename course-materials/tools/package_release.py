"""Create staged, spoiler-aware Education Track ZIP bundles and checksums."""

import hashlib
import shutil
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RELEASE = ROOT / "build" / "release"
FIXED_ZIP_TIME = (2026, 1, 1, 0, 0, 0)
MAX_SUBMISSION_BYTES = 200 * 1024 * 1024
JUNK_PARTS = {".git", ".pytest_cache", "__pycache__", "build", ".venv"}
JUNK_NAMES = {".DS_Store", "missfont.log"}
JUNK_SUFFIXES = {".aux", ".log", ".out", ".pyc", ".synctex.gz"}
OBSOLETE_NAMES = {"Archive.zip", "slide_theme_reference.pptx"}
ROOT_DOCS = ["README.md", "LICENSE.md", "BUILD.md", "MANIFEST.md", "THIRD_PARTY.md", "requirements.txt"]
LEARNER_WITHHELD = {
    "materials/01_instructor_guide.md",
    "materials/03_slide_outline.md",
    "materials/validated_issue17.md",
}


def allowed(path):
    relative = path.relative_to(ROOT)
    return (
        path.is_file()
        and not any(part in JUNK_PARTS for part in relative.parts)
        and path.name not in JUNK_NAMES
        and path.name not in OBSOLETE_NAMES
        and not any(path.name.endswith(suffix) for suffix in JUNK_SUFFIXES)
        and not (
            relative.parts
            and relative.parts[0] == "paper"
            and path.name.startswith("NeurIPS-")
            and path.suffix.lower() == ".pdf"
        )
    )


def all_files():
    return sorted((path for path in ROOT.rglob("*") if allowed(path)), key=lambda item: item.as_posix())


def learner_files(files):
    selected = []
    for path in files:
        rel = path.relative_to(ROOT)
        if rel.as_posix() in ROOT_DOCS:
            selected.append(path)
        elif rel.parts and rel.parts[0] == "materials":
            if (
                "instructor_only" not in rel.parts
                and "pilot" not in rel.parts
                and "slides" not in rel.parts
                and "notebooks" not in rel.parts
                and rel.as_posix() not in LEARNER_WITHHELD
            ):
                selected.append(path)
    return selected


def instructor_files(files):
    return [path for path in files if path.relative_to(ROOT).parts[0] != "paper"]


def write_zip(destination, files, prefix):
    with zipfile.ZipFile(destination, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path in files:
            rel = path.relative_to(ROOT)
            info = zipfile.ZipInfo(f"{prefix}/{rel.as_posix()}", FIXED_ZIP_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, path.read_bytes())


def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    if RELEASE.exists():
        shutil.rmtree(RELEASE)
    RELEASE.mkdir(parents=True)
    files = all_files()
    outputs = {
        "neurips2026-verification-centered-se-submission.zip": files,
        "verification-centered-se-learner-package.zip": learner_files(files),
        "verification-centered-se-instructor-package.zip": instructor_files(files),
    }
    learner_rel = {path.relative_to(ROOT).as_posix() for path in outputs["verification-centered-se-learner-package.zip"]}
    forbidden_learner = {
        rel for rel in learner_rel
        if rel.startswith("materials/instructor_only/")
        or rel.startswith("materials/slides/")
        or rel.startswith("materials/notebooks/")
        or rel in LEARNER_WITHHELD
    }
    if forbidden_learner:
        raise RuntimeError(f"learner package leaks staged material: {sorted(forbidden_learner)}")
    submission_rel = {path.relative_to(ROOT).as_posix() for path in files}
    forbidden_submission = {
        rel for rel in submission_rel
        if rel == "Archive.zip"
        or rel.endswith("slide_theme_reference.pptx")
        or (rel.startswith("paper/NeurIPS-") and rel.endswith(".pdf"))
    }
    if forbidden_submission:
        raise RuntimeError(f"submission package includes excluded third-party/obsolete files: {sorted(forbidden_submission)}")
    for name, selected in outputs.items():
        write_zip(RELEASE / name, selected, "verification-centered-se")
    submission = RELEASE / "neurips2026-verification-centered-se-submission.zip"
    if submission.stat().st_size >= MAX_SUBMISSION_BYTES:
        raise RuntimeError("submission ZIP exceeds the 200 MB limit")
    checksum_lines = [f"{sha256(RELEASE / name)}  {name}" for name in sorted(outputs)]
    (RELEASE / "SHA256SUMS").write_text("\n".join(checksum_lines) + "\n", encoding="utf-8")
    print(f"submission_bytes={submission.stat().st_size}")
    for name in sorted(outputs):
        print(f"{name}: {len(outputs[name])} files")


if __name__ == "__main__":
    main()
