import subprocess
import unittest
from types import SimpleNamespace
from machine_check import probe


class MachineCheckTests(unittest.TestCase):
    def test_missing_tool(self):
        self.assertFalse(probe('gemini', lookup=lambda _: None)['installed'])

    def test_returns_only_version_not_raw_output(self):
        result = probe('codex', lookup=lambda _: '/example/codex', run=lambda *a, **k: SimpleNamespace(returncode=0, stdout='codex 1.2.3 user=PRIVATE secret=PRIVATE'))
        self.assertEqual(result['version'], '1.2.3')
        self.assertNotIn('PRIVATE', str(result))

    def test_timeout(self):
        def timeout(*a, **k):
            raise subprocess.TimeoutExpired('tool', 8)
        self.assertIsNone(probe('codex', lookup=lambda _: '/example/codex', run=timeout)['version'])

    def test_batch_shim_not_executed(self):
        def forbidden(*a, **k):
            self.fail('batch shim must not execute')
        self.assertTrue(probe('codex', lookup=lambda _: 'codex.cmd', run=forbidden)['installed'])

    def test_nonzero_output_is_not_version(self):
        result = probe('codex', lookup=lambda _: '/example/codex', run=lambda *a, **k: SimpleNamespace(returncode=1, stdout='error 1.2.3'))
        self.assertIsNone(result['version'])


if __name__ == '__main__':
    unittest.main()
