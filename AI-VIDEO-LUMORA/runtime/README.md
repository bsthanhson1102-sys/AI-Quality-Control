# AI-QC executable pilot (development)

Status: **INTEGRATION IN PROGRESS / NOT DEPLOYED / NO VIDEO PASS**.

Modules:
- `orchestrator.py`: deterministic intake, approval gate, state persistence, candidate MP4 inspection
- `worker_pipeline.py`: injected Creator/Critic/Editor/Regression/Auditor callbacks, seven weighted criteria, >=90/100 and zero Critical/Major, four-round cap
- `video_review.py`: bridge from MP4 technical inspection into QC, blocking missing consent/medical review
- `test_*.py`: unit and integration fixtures

To run from this directory: `python -m unittest discover -v`.
To run the original blocked pilot: `python orchestrator.py --brief lumora_brief.json --state-dir .pilot-state`.

**Evidence boundary (2026-11-19):** GitHub files were created and fetched for readback. An attempted clean local fetch failed because `raw.githubusercontent.com` DNS resolution was unavailable in the execution container. Therefore the committed integrated test suite is **NOT VERIFIED**, regardless of earlier isolated prototype test claims. No CI execution, independent AI workers, actual cinematic video generator, legally licensed footage, visual reviewer or production PASS is verified. This code cannot be used as proof of >80% pilot maturity. User authorization remains mandatory for cost, publishing, credentials, and consent.
