import pytest


def test_sync_transactions(sync_connection):
    # Merge dummy node
    query = "MERGE (t:Test) RETURN count(t) AS res"
    response = sync_connection.run(query)
    result = response.single()
    assert result.get("res") == 1
    # Delete dummy node
    delete_query = "MATCH (t:Test) DELETE t"
    response = sync_connection.run(delete_query)
    # Check if dummy node was deleted
    match_query = "MATCH (t:Test) RETURN count(t) AS res"
    result = response.single()
    assert result is None


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
    result = await response.single()
    assert result is None
