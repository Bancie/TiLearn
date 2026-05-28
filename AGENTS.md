# AGENTS.md

## Cursor Cloud specific instructions

This repository contains two independent products:

1. **Python library (`app/tilearn`)** — a scheduling/time-management optimization package (Python ≥ 3.10).
2. **Documentation site (`docs/`)** — a Docusaurus 3.x static site (Node ≥ 20).

### Running the Python library

```bash
pip install -e .                # editable install from repo root
python -c "import tilearn as tl; print(tl.wspt([['J1',2,0,8,4]]))"
```

No external services (databases, Docker, etc.) are required. The library is file-system-based (CSV I/O).

### Running the docs site (dev mode)

```bash
cd docs
npm ci
npm start          # serves at http://localhost:3000/TiLearn/
```

The `baseUrl` is `/TiLearn/`, so the root page is at `http://localhost:3000/TiLearn/`.

### Lint / Typecheck

- **Docs TypeScript check**: `cd docs && npx tsc --noEmit`
- **Docs build** (also serves as a lint-like check for broken links): `cd docs && npm run build`
- There is no Python linter or test runner configured in the repo currently.

### Notes

- `mkdocs.yml` at the repo root is legacy/unused — the active docs system is Docusaurus in `docs/`.
- The `run.py` at the repo root imports from `tilearn` and exercises all the module's public APIs. It is not a runnable script on its own (it only defines imports).
- Docusaurus build produces warnings about broken anchors in API reference pages — these are pre-existing and unrelated to env setup.
