import copy
import hashlib
import unittest

from test_release_gate import BASE
from publish_gate import verify


def approved(artifact):
    return {
        "artifact_sha256": hashlib.sha256(artifact.encode("utf-8")).hexdigest(),
        "decision": "APPROVED",
        "reviewer": "Human reviewer",
        "evidence": "Reviewed content and policy; approval recorded in workflow.",
        "domain_review": "PASS",
        "technical_review": "PASS",
    }


class TestPublishGate(unittest.TestCase):
    def test_requires_approval(self):
        self.assertEqual(verify(BASE, None)["decision"], "BLOCKED")

    def test_valid_record_is_not_certification(self):
        self.assertEqual(verify(BASE, approved(BASE["artifact"]))["decision"], "APPROVAL_RECORDED")

    def test_blocks_modified_artifact(self):
        a = copy.deepcopy(BASE)
        a["artifact"] += " unreviewed text"
        self.assertIn("ARTIFACT_HASH_MISMATCH", verify(a, approved(BASE["artifact"]))["reasons"])

    def test_blocks_self_reported_low_score(self):
        a = copy.deepcopy(BASE)
        a["final_auditor"]["scores"] = [0] * 7
        self.assertEqual(verify(a, approved(a["artifact"]))["decision"], "BLOCKED")

    def test_blocks_unresolved_major(self):
        a = copy.deepcopy(BASE)
        a["recheck"]["M1"] = "UNRESOLVED"
        self.assertEqual(verify(a, approved(a["artifact"]))["decision"], "BLOCKED")

    def test_blocks_unidentified_reviewer(self):
        a = approved(BASE["artifact"])
        a["reviewer"] = ""
        self.assertIn("REVIEWER_NOT_IDENTIFIED", verify(BASE, a)["reasons"])

    def test_blocks_domain_not_pass(self):
        a = approved(BASE["artifact"])
        a["domain_review"] = "NOT RUN"
        self.assertIn("DOMAIN_REVIEW_NOT_PASS", verify(BASE, a)["reasons"])

    def test_blocks_forged_approval_field(self):
        a = approved(BASE["artifact"])
        a["decision"] = "PENDING"
        self.assertEqual(verify(BASE, a)["decision"], "BLOCKED")


if __name__ == "__main__":
    unittest.main()
