import csv
import tempfile
import unittest
from pathlib import Path

from analyze_pilot import REQUIRED_FIELDS, summarize


class AnalyzePilotTest(unittest.TestCase):
    def test_empty_template_makes_no_claim(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "pilot.csv"
            with path.open("w", newline="", encoding="utf-8") as handle:
                csv.DictWriter(handle, fieldnames=sorted(REQUIRED_FIELDS)).writeheader()
            self.assertEqual(summarize(path)["status"], "NO_HUMAN_DATA")

    def test_descriptive_summary_uses_completed_pairs(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "pilot.csv"
            fields = sorted(REQUIRED_FIELDS)
            rows = [
                dict(participant_id="P01", agent_experience="some", pre_score="4", post_score="8", discovered_before_release="1", evidence_trace_score="3", architecture_score="4", transfer_score="3", transfer_pass="1", completion_minutes="148", completed="1", setup_incidents="1"),
                dict(participant_id="P02", agent_experience="none", pre_score="6", post_score="8", discovered_before_release="0", evidence_trace_score="3", architecture_score="2", transfer_score="2", transfer_pass="0", completion_minutes="150", completed="1", setup_incidents="0"),
            ]
            with path.open("w", newline="", encoding="utf-8") as handle:
                writer = csv.DictWriter(handle, fieldnames=fields)
                writer.writeheader()
                writer.writerows(rows)
            result = summarize(path)
            self.assertEqual(result["n_completed"], 2)
            self.assertEqual(result["mean_paired_gain"], 3.0)
            self.assertEqual(result["discovery_rate"], 0.5)
            self.assertEqual(result["transfer_pass_rate"], 0.5)


if __name__ == "__main__":
    unittest.main()
