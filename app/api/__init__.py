__all__ = ("user_router", "analis_router")

from .user.views import router as user_router
from .analis.views import router as analis_router