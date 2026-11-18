# AI-QC executable pilot (v0.1)
This is a deterministic orchestration **skeleton**, not independent agents or a video generator.
Run: `python -m unittest -v test_orchestrator.py`
Demo: `python orchestrator.py --brief lumora_brief.json --state-dir .pilot-state`
Expected demo: BLOCKED / PRODUCTION_CAPABILITY_MISSING.
Never claim an MP4 or >=90 QC PASS without production and inspection evidence.
Local initial implementation tested 7/7 with Python unittest on 2026-11-19. The committed copy has not been separately executed from a fresh GitHub checkout.
