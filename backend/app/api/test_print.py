from fastapi import APIRouter, Depends

from app.api.deps import get_test_service, get_verified_user_email
from app.services.test_service import TestService

router = APIRouter(tags=["test"])


@router.get("/test_print")
def test_print(
    email: str = Depends(get_verified_user_email),
    test_service: TestService = Depends(get_test_service),
) -> dict[str, bool]:
    test_service.run_test(email)
    return {"ok": True}

