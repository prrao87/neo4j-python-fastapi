from config import settings
from neo4j import GraphDatabase, AsyncGraphDatabase
import pytest_asyncio
import pytest


@pytest.fixture(scope="session")
def config():
    from dotenv import load_dotenv
    load_dotenv()
    return settings.Settings()


# Test a sync Neo4j database connection
@pytest.fixture
def sync_connection(config):
    URI = f"bolt://{config.neo4j_url}:7687"
    AUTH = (config.neo4j_user, config.neo4j_password)
    with GraphDatabase.driver(URI, auth=AUTH) as driver:
        with driver.session(database="neo4j") as session:
            yield session


# Test an async Neo4j database connection
@pytest_asyncio.fixture
async def async_connection(config):
    URI = f"bolt://{config.neo4j_url}:7687"
    AUTH = (config.neo4j_user, config.neo4j_password)
    async with AsyncGraphDatabase.driver(URI, auth=AUTH) as driver:
        async with driver.session(database="neo4j") as session:
            yield session