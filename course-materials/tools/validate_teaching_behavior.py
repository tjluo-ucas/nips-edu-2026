"""Validate intentional teaching behavior without treating a counterexample as build failure."""

import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_function(path, module_name, function_name):
    spec = importlib.util.spec_from_file_location(module_name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return getattr(module, function_name)


candidate = load_function(
    ROOT / "materials/exercise_repo/src/discount.py",
    "candidate_c017_validation",
    "promotional_discount",
)

visible = [
    (150.0, False, 0.0),
    (120.0, True, 12.0),
    (80.0, True, 0.0),
    (400.0, True, 25.0),
]
assert all(candidate(total, member) == expected for total, member, expected in visible)

actual = candidate(100.0, True)
assert actual == 0.0, f"Candidate C-017 changed; expected teaching counterexample, got {actual}"
print("PASS: visible verifier accepts Candidate C-017")
print("PASS: stronger exact-threshold oracle exposes Candidate C-017 (expected 10.0, observed 0.0)")
