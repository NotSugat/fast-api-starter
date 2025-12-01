import os

# fastapi
from fastapi import FastAPI
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from dotenv import load_dotenv

# sqlalchemy
from sqladmin import Admin, ModelView

# import
from app.core.database import engine
from app.models.admin import UserAdmin
from app.api.routers.main_router import router

# from app.core.settings import config

# Load environment variables from .env file
load_dotenv()

cors_origins_str = os.getenv("CORS_ORIGINS", "*")
origins = (
    [origin.strip() for origin in cors_origins_str.split(",")]
    if cors_origins_str != "*"
    else ["*"]
)


def init_routers(app_: FastAPI) -> None:
    app_.include_router(router)
    # admin dashboard
    admin = Admin(app_, engine)
    admin.add_view(UserAdmin)


def make_middleware() -> List[Middleware]:
    middleware = [
        Middleware(
            CORSMiddleware,
            allow_origins=origins,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        ),
        # Middleware(SQLAlchemyMiddleware),
    ]
    return middleware
