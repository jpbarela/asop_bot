# embeddings

This README contains information on the `embeddings` package that processes the ASOPs in vector embeddings that can be
used to provide relevant context in `asop_bot`.

## Pipeline strategy

The current pipeline strategy is simple:

1. Download the ASOPs in a local folder
2. Split the ASOPs into pages and embed the pages into the vector store

## Invoking the Pipeline

The pipeline is built around a pair of command line commands:

1. `download` which downloads the ASOPs to a local folder
2. `process` which converts all of the local

These commands can be invoked locally like

```
    poetry run python embeddings download.
```

## Subpackages

A brief description of each subpackage is provided below

### page_objects

The `page_objects` package provides an abstraction layer over ABCD webpage that lists ASOPs.

The key function in this package is currently `pdf_links` which returns a list of all the links to the PDF versions of
the ASOPs.

### pipeline

The actual package for converting downloaded PDFs into a vector database.

The key function in this package is `process` which transforms all of the locally downloaded files into a database of
vector embeddings.
