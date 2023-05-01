# Data ingestion

This section shows how to effectively bulk-ingest large amounts of data into Neo4j using Python.

## Best practices

### Data validation via Pydantic

Because Neo4j doesn't enforce data types prior to runtime, data validation is done via [Pydantic](https://docs.pydantic.dev/latest/). It is highly recommended to perform validation this way prior to ingesting the data into Neo4j so that queries perform as expected, and there are no errors or unexpected issues in production.

- Number types (like integers and floats) are coerced prior to ingestion
- Fields are renamed when required (`designation` is renamed to `vineyard` for clarity)
- Default values are set using validators (If `country` field doesn't exist, a default value of "Unknown" is assigned)


### Create indexes and constraints

To efficiently ingest large amounts of data into Neo4j, as the graph keeps getting larger and larger, it helps greatly to set up indexes and constraints beforehand. Typically, constraints are set on items that we expect to be unique, such as an ID, or a country name.


### Batch transactions with `UNWIND`

Each transaction with the database is expensive due to network overhead, so, to speed up performance, batched transactions are performed.

- The validated data is divided up into batches, or "chunks"
- Each chunk is roughly 10k-20k records (where each "record" is a type-validated dict, coming from Pydantic)
- The chunks (lists of dicts) can be fed into Neo4j via the sync or async driver, and easily `UNWIND`ed in Cypher
- `UNWIND`, as the name suggests, expands a list of dicts into rows, each of which provides all the information that Neo4j needs to build the nodes and edges in the graph

💡 **Tip**: Submitting a large list of dicts, 10k-20k in length, to `UNWIND` in Cypher, can improve performance massively compared to submitting each record one at a time (due to bolt network and Python overheads)

A more detailed blog post on these best practices will be published soon!
