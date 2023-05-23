# Neo4j for Pythonistas

This repo contains code for the methods described in this series of blog posts:

1. [Neo4j for Pythonistas: Part 1](https://thedataquarry.com/posts/neo4j-python-1/)
   * Using Pydantic and async Python to build a graph in Neo4j

## Goals

The aim of this code is to build a Neo4j graph via its [officially maintained Python client](https://github.com/neo4j/neo4j-python-driver), using either the sync or async database drivers. The async driver offers support for using Python's `asyncio` coroutine-based asynchronous, concurrent workflows, which can be beneficial in certain scenarios. Both sync and async code is provided in `src/ingest` as a starter template to bulk-ingest large amounts of data into Neo4j in batches, so as to be as efficient as possible. Code will be added in three parts:


1. Bulk data ingestion into Neo4j using Pydantic and async Python
2. Building a RESTful API on top of the Neo4j graph via [FastAPI](https://fastapi.tiangolo.com/)
3. Building a GraphQL API on top of the Neo4j graph via FastAPI and [Strawberry](https://strawberry.rocks/)

There are lots of clever ways one can write an API on top of Neo4j, but the main focus of this repo is to keep code readable, and the logic simple and easy enough to extend for future use cases as they arise.


## Requirements

### Install Python dependencies

Install Python dependencies in a virtual environment using `requirements.txt` as follows. All code in this repo has been tested on Python 3.11.

```
# Setup the environment for the first time
python -m venv neo4j_venv

# Activate the environment (for subsequent runs)
source neoj_venv/bin/activate

python -m pip install -r requirements.txt
```


### Install and run Docker

* [Download Docker](https://docs.docker.com/get-docker/) and run the Docker daemon
* Use the provided `docker-compose.yml` to set up and run the database in a container
  * This ensures reproducibility and ease of setup, regardless of the platform used.
* Copy the file `.env.example` and rename it to `.env`.
* Fill in the `NEO4J_PASSWORD` field in `.env` to a non-null value -- this will be the password used to log into the Neo4j database running on `localhost`.

To start the database service, run Docker in detached mode via the compose file.

```sh
docker compose up -d
```

This command starts a persistent-volume Neo4j database so that any data that's ingested persists on the local system even after Docker is shut down.

Tear down the database process and containers at any time using the following command:

```
docker compose down
```

## Dataset

The [wine reviews dataset](./data/) provided in this repo is a newline-delimited JSON-formatted version of the version obtained from Kaggle datasets.


## Run tests

Once the data is ingested into Neo4j, the APIs and schemas can be tested via `pytest` to ensure that endpoints behave as expected. 

> 💡 **Note:** Run the tests **inside the Docker container** as FastAPI communicates with the Neo4j service via its own network inside the container.

To enter the Docker container, in the following example, the name of the running container obtained via `docker ps` is `neo4j-python-fastapi-fastapi-1`.

```
docker exec -it neo4j-python-fastapi-fastapi-1 bash
pytest -v
```

The first line runs an interactive bash shell inside the container, and the second runs the tests in verbose mode. Assuming that the data has been ingested into the database, the tests should pass and return something like this.

```
======================== test session starts ========================
platform linux -- Python 3.11.3, pytest-7.3.1, pluggy-1.0.0 -- /usr/local/bin/python
cachedir: .pytest_cache
rootdir: /wine
plugins: asyncio-0.21.0, anyio-3.6.2
asyncio: mode=Mode.STRICT
collected 7 items                                                   

src/api/test_main.py::test_search PASSED                      [ 14%]
src/api/test_main.py::test_top_by_country PASSED              [ 28%]
src/api/test_main.py::test_top_by_province PASSED             [ 42%]
src/api/test_main.py::test_most_by_variety PASSED             [ 57%]
src/tests/test_crud.py::test_sync_transactions PASSED         [ 71%]
src/tests/test_crud.py::test_async_transactions PASSED        [ 85%]
src/tests/test_schemas.py::test_wine_schema PASSED            [100%]

========================= 7 passed in 0.45s =========================
```