# Convexis Specification Lock (Phase 1)

## Module diagram
- `apps/web`: React + Vite + TypeScript SPA with Dashboard/Options/Stocks/Risk/Settings routes.
- `apps/api`: FastAPI backend, single SQLAlchemy connection pool, future ingestion orchestration.
- `packages/shared`: shared TS types for API contracts.
- `scripts/*`: python bootstrap + runtime launchers for unified `npm install`, `npm run dev`, `npm run start`.

## Config entities
- `db_config`: host, port, dbname, user, password, sslmode, timeout, pool options.
- `ftp_config`: host, port, auth, passive mode, remote path, filename regex per report.
- `pgp_config`: key source/path, key fingerprint, passphrase reference.
- `report_definitions[]`: report key, filename regex/date captures, encoding, decimal rules, dedupe strategy.
- `csv_to_db_mapping[]`: block matchers, selectors, transforms, validations, target table, upsert keys/strategy.
- `domain_mapping`: canonical view SQL mapping + materialized-view toggle and refresh strategy.
- `scheduler_config`: timezone (Europe/Madrid), run time, enable flag, retry policy.

## Parsing DSL schema
- `blocks[]`
  - `start_match`: `{type: token|regex|header, value}`
  - `end_match`: `{type: token|regex|blank_rows, value}`
  - `columns[]`: `{name, selector: header_exact|header_regex|index|label_adjacent, value}`
  - `filters[]`: include/exclude regex + footer skip directives
  - `transforms[]`: numeric/date/currency/sign/default/compute
  - `validations[]`: required, uniqueness, domain constraints
- Output is normalized row objects consumed by CSV→DB mapping.

## DB permission fallback plan
1. Attempt to ensure minimal `convexis_meta` schema for configs + run logs.
2. If permission denied, use local encrypted config/log store under app data path.
3. Business data writes always target existing broker tables (no schema alteration).
4. Staging is optional; fallback is dry-run with local error logs.

## Endpoint list
- Health: `GET /api/health`, `GET /api/health/db`
- Config: `GET/POST /api/config/{db|ftp|pgp|reports}`
- Mapping: `GET/POST /api/config/mappings/csv-to-db`, `POST /api/mappings/csv-to-db/test`, `POST /api/mappings/csv-to-db/save`, `GET/POST /api/mappings/domain`, `POST /api/mappings/domain/generate-views`
- Ingestion: `POST /api/ingest/run`, `GET /api/ingest/runs`
- Analytics: `GET /api/dashboard`, `GET /api/options`, `GET /api/stocks`, `GET /api/risk/overview`, `GET /api/risk/options`, `GET /api/rolls`

## UI route map
- `/` Dashboard
- `/options` Options
- `/stocks` Stocks
- `/risk` Risk
- `/settings` Settings (DB, FTP, PGP, CSV conversion, domain mapping, scheduler tabs)

## Incremental execution status
- ✅ Step 1 complete: UI shell + backend skeleton + health endpoints + Vite dev proxy + prod static serving scaffold.
- ⏭️ Steps 2-10 pending.
