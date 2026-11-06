# Changelog

## 2026-11-06 — Modular registry and lifecycle foundation

- Added a central registry with stable skill IDs, versions, file paths, statuses and routing triggers.
- Added shared skill routing and lifecycle/versioning protocols.
- Expanded and versioned the six initial specialist skills at 1.0.0.
- Added a compact global ChatGPT core-instructions file and revised the installation guide for ordinary chats and optional Projects.
- Added registry/routing acceptance tests, a standard-library registry validator and a GitHub Actions workflow to run the validator on pushes and pull requests to `main`.
- Updated ChatGPT master instructions, Codex guidance and repository documentation.
- Runtime-level behavior and the GitHub Actions run remain subject to verification in their target environments; no runtime skill execution test is claimed here.
