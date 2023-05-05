# Neo4j: Python and FastAPI starter code

This repo provides code to build a Neo4j graph via its [officially maintained Python client](https://github.com/neo4j/neo4j-python-driver), using either the sync or async database drivers. The async driver offers support for using Python's `asyncio` coroutine-based asynchronous, concurrent workflows, which can be beneficial in certain scenarios. Both sync and async code is provided in `src/ingest` as a starter template to bulk-ingest large amounts of data into Neo4j in batches, so as to be as efficient as possible.

## Goals

The aim of this repo is to showcase how to build and maintain a data engineering workflow using Python, Pydantic and FastAPI. Code will be added in three parts.

1. Bulk data ingestion into Neo4j
2. Building a RESTful API on top of the Neo4j graph via [FastAPI](https://fastapi.tiangolo.com/)
3. Building a GraphQL API on top of the Neo4j graph via FastAPI and [Strawberry](https://strawberry.rocks/)

A series of blog posts will also be published, going through the concepts involved. Stay tuned!


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
* Use the provided `docker-compose.yml` to install and run the database in a container
  * This ensures reproducibility and ease of setup, regardless of the platform used.
* Copy the file `.env.example` and rename it to `.env`.
* Fill in the `NEO4J_PASSWORD` field in `.env` to a non-null value -- this will be the password used to log into the Neo4j database running on `localhost`.

To start the database service, run Docker in detached mode via the compose file.

```sh
docker compose up -d
```

This command starts a persistent-volume Neo4j database so that any data that's ingested persists on the local system even after Docker is shut down.

Tear down the database process and containers at any time using the following command.

```
docker compose down
```

## Dataset

The [wine reviews dataset](./data/) provided in this repo is a newline-delimited JSON-formatted version of the version obtained from Kaggle datasets.
