from fastapi import APIRouter, Depends

from app.api.deps import get_auth_service
from app.schemas.login import LoginRequest, LoginResponse
from app.services.auth_service import AuthService

router = APIRouter(tags=["auth"])


@router.post("/login", response_model=LoginResponse)
def login(
    body: LoginRequest,
    auth_service: AuthService = Depends(get_auth_service),
) -> LoginResponse:
    auth_service.login_with_google_id_token(body.id_token)
    return LoginResponse(ok=True)

