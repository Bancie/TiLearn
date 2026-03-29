---
title: Building from source
description: Contributor setup for running tilearn and docs from source.
---

This page describes a practical local development workflow for contributors.

## Prerequisites

- Python 3.10+
- `pip`
- Git
- Node.js 18+ (for docs site)

## 1) Clone repository

```bash
git clone https://github.com/Bancie/TiLearn.git
cd TiLearn
```

## 2) Set up Python environment

```bash
python -m venv .venv
source .venv/bin/activate
pip install -U pip
```

## 3) Install project dependencies

If `requirements.txt` is used:

```bash
pip install -r requirements.txt
```

For editable development install:

```bash
pip install -e .
```

## 4) Smoke test package import

```bash
python -c "import tilearn as tl; print(tl.__name__)"
```

## 5) Run docs locally

```bash
cd docs
npm install
npm run start
```

The local docs site usually runs at `http://localhost:3000`.

## 6) Build docs for production

```bash
cd docs
npm run build
```

## Contribution checklist

- Keep API docs aligned with code and docstrings.
- Prefer small, focused pull requests.
- Update examples when function behavior or signatures change.
- Ensure no stale references to deprecated APIs remain.
