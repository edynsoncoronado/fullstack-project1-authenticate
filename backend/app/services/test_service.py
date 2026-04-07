from __future__ import annotations

from datetime import datetime, timezone


class TestService:
    """First use-case hook: log authenticated context (backend container stdout)."""

    def run_test(self, user_email: str) -> None:
        now = datetime.now(timezone.utc)
        print(f"test_print user={user_email} datetime={now.isoformat()}")

