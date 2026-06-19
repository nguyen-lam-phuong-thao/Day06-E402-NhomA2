from __future__ import annotations

import os
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from app.api.feedback import router as feedback_router
from app.api.health import router as health_router
from app.api.recommend import router as recommend_router
from app.api.seed_cafes import router as seed_cafes_router

from app.core.config import get_settings
from app.core.logging import configure_logging

from app.repositories.cafe_repository import CafeRepository
from app.repositories.feedback_repository import FeedbackRepository

from app.services.feedback_service import FeedbackService
from app.services.reason_service import ReasonService
from app.services.recommendation_service import RecommendationService
from app.services.seed_cafe_service import SeedCafeService


BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    configure_logging()
    settings = get_settings()

    cafe_repository = CafeRepository(settings.cafes_path)
    feedback_repository = FeedbackRepository(
        settings.feedback_log_path
    )

    app.state.seed_cafe_service = SeedCafeService(
        repository=cafe_repository,
        default_seed_count=settings.seed_count,
    )

    app.state.recommendation_service = RecommendationService(
        cafe_repository=cafe_repository,
        reason_service=ReasonService(),
        similarity_threshold=settings.similarity_threshold,
        max_results=settings.max_results,
    )

    app.state.feedback_service = FeedbackService(
        feedback_repository
    )

    yield


def create_app() -> FastAPI:
    settings = get_settings()

    app = FastAPI(
        title=settings.app_name,
        lifespan=lifespan,
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.allowed_origins,
        allow_credentials=False,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Static frontend folder
    app.mount(
        "/frontend",
        StaticFiles(directory="frontend"),
        name="frontend",
    )

    # Home page
    @app.get("/")
    async def read_index():
        return FileResponse(
            os.path.join(BASE_DIR, "index.html")
        )

    # APIs
    app.include_router(health_router)
    app.include_router(seed_cafes_router)
    app.include_router(recommend_router)
    app.include_router(feedback_router)

    return app


app = create_app()