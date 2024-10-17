__all__ = ("user_router", "analis_router", "analis_value")

from .user.views import router as user_router
from .analis.views import router as analis_router
from .analis_value.views import router as analis_value_router
from .analis_standart.views import router as analis_standart_router
from .test_schedule.views import router as schedule_router
