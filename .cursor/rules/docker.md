# Docker & DevContainer Architecture Rules

This project is Docker-first and DevContainer-first.

Nothing runs on the host machine.
All services run inside containers.

Cursor must ALWAYS assume the code runs inside containers.

---

## 🐳 Services

The system is composed of 3 containers:

- frontend (Next.js)
- backend (FastAPI)
- postgres (database)

They communicate through the internal Docker network.

Never assume localhost means the host machine.
Inside containers, services talk by service name.

Examples:

- Backend connects to DB using host: `postgres`
- Frontend calls backend using: `http://backend:8000`

---

## 🧪 Development Mode Requirements

Both frontend and backend must support hot reload inside containers.

### Backend
- Use `uvicorn --reload`
- Code mounted as volume
- No rebuild needed after code changes

### Frontend
- Use `next dev`
- Node modules inside container
- Code mounted as volume

---

## 📦 Docker Compose is mandatory

You must assume a `docker-compose.yml` orchestrates:

- frontend
- backend
- postgres

Never propose running services independently.

---

## 🧠 Networking Mental Model

From inside containers:

| From       | To        | URL                     |
|------------|-----------|--------------------------|
| frontend   | backend   | http://backend:8000     |
| backend    | postgres  | postgresql://postgres   |

Never use:
- localhost
- 127.0.0.1

---

## 🗂️ Volume Strategy

Source code is mounted as volume for live reload:

- ./backend → /app
- ./frontend → /app

Do not copy source code into images for development.

---

## 🧰 DevContainer Rules (Cursor)

The DevContainer must attach to the running containers.

Cursor terminal, Python, Node, and debugging happen INSIDE containers.

Never assume:
- local Python
- local Node
- local Postgres

Everything is containerized.

---

## 🔐 Environment Variables

All secrets and configuration must come from:

- `.env`
- docker-compose environment section

Never hardcode:

- DB URLs
- Secrets
- OAuth keys

---

## 🚫 What you must NEVER do

- Never write instructions that require running backend outside Docker
- Never use localhost for service communication
- Never assume developer has dependencies installed locally
- Never write Dockerfiles that copy the whole project without volumes for dev
- Never ignore DevContainer context