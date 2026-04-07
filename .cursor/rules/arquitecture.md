# Application Architecture

This project follows a request-driven architecture where the frontend never talks directly to the database or Google services.
All flows go through the FastAPI backend.

---

## 🔐 Authentication Flow

1. User opens landing page in Next.js
2. User clicks "Login with Google"
3. NextAuth/Auth.js handles Google OAuth in the frontend
4. Frontend receives Google ID Token (JWT)
5. Frontend calls: POST /api/login in FastAPI with the token
6. FastAPI verifies the token with Google
7. If user does not exist → create user in PostgreSQL
8. If user exists → fetch user
9. FastAPI responds OK
10. Frontend redirects user to /dashboard

Important rules:

- Backend is stateless
- No sessions stored
- Every request from frontend includes Bearer token
- Backend always validates Google JWT

---

## 🧭 Main Pages

### Landing Page
- Shows login button
- No backend calls except login

### Dashboard Page
- Accessible only if authenticated
- Contains a test button that calls backend

---

## 🧪 First Use Case: `test_print`

This is the first backend use case to validate architecture.

Flow:

1. User clicks "Test" button in dashboard
2. Frontend calls: GET /api/test_print with Bearer token
3. Backend:
   - Extracts user from token
   - Gets current datetime
   - Prints in console:
     - user email
     - datetime
4. Backend returns OK
5. Visible in backend container logs

This endpoint exists ONLY to validate:

- Auth flow
- Dependency injection
- Layer separation
- Logging
- Docker/devcontainer networking

---

## 🗃️ Database Responsibility

PostgreSQL stores:

- Users table
  - id
  - email
  - name
  - picture
  - created_at

No auth logic in database.

---

## 🧱 Backend Layers In This Project

For the login and test_print use cases:

- api/login → calls AuthService
- api/test_print → calls TestService
- AuthService → uses UserRepository
- TestService → does not access DB
- UserRepository → only DB access layer

---

## 🚫 What frontend must NEVER do

- Never validate Google token
- Never store business logic
- Never talk directly to database
- Never assume user exists without backend confirmation

---

## 🧠 Mental Model Cursor Must Follow

When implementing features, think:

> "Where does this belong: api, service, repository, or domain?"

Never mix responsibilities.