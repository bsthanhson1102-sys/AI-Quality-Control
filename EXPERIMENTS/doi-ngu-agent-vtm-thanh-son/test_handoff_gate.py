"""Synthetic packet fixtures, not evidence of real AI or Facebook execution."""
import copy
import tempfile
import unittest
from pathlib import Path
from handoff_gate import STAGES, confined, digest, validate


class GateTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / 'caption.txt').write_text('Synthetic fixture, not for publication.')
        (self.root / 'evidence.txt').write_text('SIMULATED REVIEW FIXTURE')
        hashes = {'caption.txt': digest(self.root / 'caption.txt')}
        evidence = [{'path': 'evidence.txt', 'sha256': digest(self.root / 'evidence.txt')}]
        self.packet = {'task_id': 'fixture-001', 'round': 1, 'ai_qc_commit': 'a' * 40,
                       'artifacts': [{'path': k, 'sha256': v} for k, v in hashes.items()],
                       'stages': {s: {'status': 'completed', 'reviewer': s,
                                      'evidence': evidence, 'artifact_hashes': hashes,
                                      'verdict': 'approved'} for s in STAGES},
                       'gates': dict.fromkeys(('technical', 'domain', 'regression'), 'verified'),
                       'scores': [25, 20, 15, 15, 10, 10, 5], 'findings': []}

    def tearDown(self):
        self.tmp.cleanup()

    def test_structurally_valid_fixture(self):
        self.assertEqual(validate(self.packet, self.root), [])

    def test_each_missing_stage_blocks(self):
        for stage in STAGES:
            p = copy.deepcopy(self.packet)
            del p['stages'][stage]
            with self.subTest(stage=stage):
                self.assertTrue(validate(p, self.root))

    def test_critical_and_major_block_high_score(self):
        for severity in ('Critical', 'Major'):
            p = copy.deepcopy(self.packet)
            p['findings'] = [{'severity': severity, 'resolution': 'open'}]
            self.assertTrue(validate(p, self.root))

    def test_changed_artifact_blocks(self):
        (self.root / 'caption.txt').write_text('Changed after approval')
        self.assertTrue(validate(self.packet, self.root))

    def test_changed_evidence_blocks(self):
        (self.root / 'evidence.txt').write_text('Changed evidence')
        self.assertTrue(validate(self.packet, self.root))

    def test_stale_approval_blocks(self):
        self.packet['stages']['final']['artifact_hashes'] = {}
        self.assertTrue(validate(self.packet, self.root))

    def test_self_approval_blocks(self):
        self.packet['stages']['final']['reviewer'] = 'production'
        self.assertTrue(validate(self.packet, self.root))

    def test_round_limits(self):
        for value in (0, 5, True, '1'):
            self.packet['round'] = value
            self.assertTrue(validate(self.packet, self.root))

    def test_scores(self):
        for scores in ([0] * 7, [100] * 7, [True] * 7, [float('nan')] * 7):
            self.packet['scores'] = scores
            self.assertTrue(validate(self.packet, self.root))

    def test_unverified_domain_blocks(self):
        self.packet['gates']['domain'] = 'not_run'
        self.assertTrue(validate(self.packet, self.root))

    def test_traversal_and_symlink_rejected(self):
        for value in ('../outside', str(self.root / 'caption.txt')):
            with self.assertRaises(ValueError):
                confined(self.root, value)
        (self.root / 'escape').symlink_to(self.root.parent)
        with self.assertRaises(ValueError):
            confined(self.root, 'escape/outside')

    def test_empty_packet_blocks(self):
        self.assertTrue(validate({}, self.root))

    def test_null_gates_fail_closed(self):
        self.packet['gates'] = None
        self.assertTrue(validate(self.packet, self.root))

    def test_same_qc_and_final_reviewer_blocks(self):
        self.packet['stages']['final']['reviewer'] = 'ai_qc'
        self.assertTrue(validate(self.packet, self.root))


if __name__ == '__main__':
    unittest.main()
