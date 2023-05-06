from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from functools import lru_cache

from fastapi import FastAPI
from neo4j import AsyncGraphDatabase

from src.config import settings
from src.api.routers import rest


@lru_cache()
def get_settings() -> settings.Settings:
    # Use lru_cache to avoid loading .env file for every request
    config = settings.Settings()
    return config


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """Async context manager for MongoDB connection."""
    settings = get_settings()
    URI = f"bolt://{settings.neo4j_service}:7687"
    AUTH = (settings.neo4j_user, settings.neo4j_password)
    async with AsyncGraphDatabase.driver(URI, auth=AUTH) as driver:
        async with driver.session(database="neo4j") as session:
            app.session = session
            print("Successfully connected to wine reviews Neo4j DB")
            yield
            print("Successfully closed wine reviews Neo4j connection")


app = FastAPI(
    title="REST API for wine reviews on Neo4j",
    description=(
        "Query from a Neo4j database of 130k wine reviews from the Wine Enthusiast magazine"
    ),
    version=get_settings().tag,
    lifespan=lifespan,
)


@app.get("/", include_in_schema=False)
async def root():
    return {
        "message": "REST API for querying Neo4j database of 130k wine reviews from the Wine Enthusiast magazine"
    }


# Attach routes
app.include_router(rest.router, prefix="/v1/rest", tags=["rest"])
