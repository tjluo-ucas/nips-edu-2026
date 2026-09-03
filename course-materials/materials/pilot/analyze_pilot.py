"""Aggregate anonymous formative-pilot data without external dependencies."""

import argparse
import csv
import json
import statistics
from pathlib import Path


REQUIRED_FIELDS = {
    "participant_id",
    "agent_experience",
    "pre_score",
    "post_score",
    "discovered_before_release",
    "evidence_trace_score",
    "architecture_score",
    "transfer_score",
    "transfer_pass",
    "completion_minutes",
    "completed",
    "setup_incidents",
}


def bounded_int(row, field, lower, upper):
    value = int(row[field])
    if not lower <= value <= upper:
        raise ValueError(f"{field} must be in [{lower}, {upper}]")
    return value


def summarize(path):
    with Path(path).open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if set(reader.fieldnames or []) != REQUIRED_FIELDS:
            missing = REQUIRED_FIELDS - set(reader.fieldnames or [])
            extra = set(reader.fieldnames or []) - REQUIRED_FIELDS
            raise ValueError(f"invalid columns; missing={sorted(missing)}, extra={sorted(extra)}")
        rows = list(reader)

    if not rows:
        return {"status": "NO_HUMAN_DATA", "n": 0, "claim": "Pilot-ready; no learning-outcome claim."}

    ids = [row["participant_id"] for row in rows]
    if any(not value.strip() for value in ids) or len(ids) != len(set(ids)):
        raise ValueError("participant_id values must be non-empty and unique")

    records = []
    for row in rows:
        if row["agent_experience"] not in {"none", "some", "frequent"}:
            raise ValueError("agent_experience must be none, some, or frequent")
        records.append({
            "pre": bounded_int(row, "pre_score", 0, 10),
            "post": bounded_int(row, "post_score", 0, 10),
            "discovered": bounded_int(row, "discovered_before_release", 0, 1),
            "evidence": bounded_int(row, "evidence_trace_score", 0, 4),
            "architecture": bounded_int(row, "architecture_score", 0, 4),
            "transfer": bounded_int(row, "transfer_score", 0, 4),
            "transfer_pass": bounded_int(row, "transfer_pass", 0, 1),
            "minutes": float(row["completion_minutes"]),
            "completed": bounded_int(row, "completed", 0, 1),
            "setup_incidents": int(row["setup_incidents"]),
        })
    if any(record["minutes"] <= 0 or record["setup_incidents"] < 0 for record in records):
        raise ValueError("minutes must be positive and setup incidents non-negative")

    completed = [record for record in records if record["completed"]]
    paired_gain = [record["post"] - record["pre"] for record in completed]
    rate = lambda field: sum(record[field] for record in completed) / len(completed) if completed else None
    mean = lambda field: statistics.fmean(record[field] for record in completed) if completed else None
    return {
        "status": "FORMATIVE_PILOT_DATA",
        "n_enrolled": len(records),
        "n_completed": len(completed),
        "mean_pre": mean("pre"),
        "mean_post": mean("post"),
        "mean_paired_gain": statistics.fmean(paired_gain) if paired_gain else None,
        "discovery_rate": rate("discovered"),
        "mean_evidence_trace": mean("evidence"),
        "mean_architecture": mean("architecture"),
        "mean_transfer": mean("transfer"),
        "transfer_pass_rate": rate("transfer_pass"),
        "median_completion_minutes": statistics.median(record["minutes"] for record in completed) if completed else None,
        "setup_incidents_total": sum(record["setup_incidents"] for record in records),
        "claim": "Descriptive formative results; no causal claim.",
    }


def markdown(summary):
    lines = ["# Formative Pilot Summary", ""]
    for key, value in summary.items():
        lines.append(f"- **{key}**: {value}")
    lines.extend(["", "This report is descriptive and must not be presented as causal evidence."])
    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_path")
    parser.add_argument("--json", dest="json_path")
    parser.add_argument("--markdown", dest="markdown_path")
    args = parser.parse_args()
    result = summarize(args.csv_path)
    payload = json.dumps(result, indent=2, sort_keys=True) + "\n"
    print(payload, end="")
    if args.json_path:
        Path(args.json_path).parent.mkdir(parents=True, exist_ok=True)
        Path(args.json_path).write_text(payload, encoding="utf-8")
    if args.markdown_path:
        Path(args.markdown_path).parent.mkdir(parents=True, exist_ok=True)
        Path(args.markdown_path).write_text(markdown(result), encoding="utf-8")


if __name__ == "__main__":
    main()
