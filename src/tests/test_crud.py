import pytest
import pytest_asyncio
from neo4j import AsyncGraphDatabase, GraphDatabase

from src.config import settings


@pytest.fixture(scope="session")
def config():
    from dotenv import load_dotenv

    load_dotenv()
    return settings.Settings()


# Test a sync Neo4j database connection
@pytest.fixture(scope="session")
def sync_connection(config):
    URI = f"bolt://{config.neo4j_service}:7687"
    AUTH = (config.neo4j_user, config.neo4j_password)
    with GraphDatabase.driver(URI, auth=AUTH) as driver:
        with driver.session(database="neo4j") as session:
            yield session


# Test an async Neo4j database connection
@pytest_asyncio.fixture
async def async_connection(config):
    URI = f"bolt://{config.neo4j_service}:7687"
    AUTH = (config.neo4j_user, config.neo4j_password)
    async with AsyncGraphDatabase.driver(URI, auth=AUTH) as driver:
        async with driver.session(database="neo4j") as session:
            yield session


def test_sync_transactions(sync_connection):
    # Merge dummy node
    merge_query = "MERGE (t:Test) RETURN count(t) AS res"
    response = sync_connection.run(merge_query)
    result = response.single()
    assert result.get("res") == 1
    # Delete dummy node
    delete_query = "MATCH (t:Test) DELETE t"
    response = sync_connection.run(delete_query)
    # Check if dummy node was deleted
    match_query = "MATCH (t:Test) RETURN count(t) AS res"
    response = sync_connection.run(match_query)
    result = response.single()
    assert result.get("res") == 0


@pytest.mark.asyncio
async def test_async_transactions(async_connection):
    # Merge dummy node
    merge_query = "MERGE (t:Test) RETURN count(t) AS res"
    response = await async_connection.run(merge_query)
    result = await response.single()
    assert result.get("res") == 1
    # Delete dummy node
    delete_query = "MATCH (t:Test) DELETE t"
    response = await async_connection.run(delete_query)
    # Check if dummy node was deleted
    match_query = "MATCH (t:Test) RETURN count(t) AS res"
    response = await async_connection.run(match_query)
    result = await response.single()
    assert result.get("res") == 0
