# Convexis

Self-hosted quant hedge fund operations webapp.

## Quick start

```bash
git clone <repo>
cd convexis
npm install
npm run dev
```

Production-like run:

```bash
npm run start
```

## What is implemented now

- Monorepo scaffold (`apps/web`, `apps/api`, `packages/shared`).
- Step 1 baseline:
  - React/Vite/TypeScript shell with dark dashboard navigation.
  - FastAPI backend skeleton.
  - `GET /api/health` and `GET /api/health/db` endpoints.
  - Vite dev proxy for `/api`.
  - Backend static serving hook for built frontend.

## Environment

Copy `.env.example` to `.env` and edit values.

```bash
cp .env.example .env
```
