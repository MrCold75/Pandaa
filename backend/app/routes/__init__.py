from .auth import router as auth_router
from .users import router as users_router
from .moving_requests import router as moving_requests_router
from .quotes import router as quotes_router
from .ratings import router as ratings_router

__all__ = [
    "auth_router",
    "users_router",
    "moving_requests_router",
    "quotes_router",
    "ratings_router"
]
