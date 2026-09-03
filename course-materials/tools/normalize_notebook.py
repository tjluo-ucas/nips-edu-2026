"""Remove volatile execution metadata from an executed notebook."""

import json
import sys
from pathlib import Path


def normalize(path: Path) -> None:
    notebook = json.loads(path.read_text(encoding="utf-8"))
    for cell in notebook.get("cells", []):
        cell.get("metadata", {}).pop("execution", None)
    notebook.get("metadata", {}).get("language_info", {}).pop("version", None)
    path.write_text(
        json.dumps(notebook, ensure_ascii=False, indent=1) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: normalize_notebook.py NOTEBOOK.ipynb")
    normalize(Path(sys.argv[1]))
