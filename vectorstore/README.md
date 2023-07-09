# vectorstore

The `vectorstore` package is an abstraction over the vector database to enable the rest of the system to treat the
vector store as black box.

## Current Implementation

The current implementation of a vector store uses [Chroma](https://docs.trychroma.com/) and a sentence transformer
model for the embeddings. This combination is best for prototyping and can be run on modern laptops without difficulty.
The current embedding model is `all-MiniLM-L6-v2` which is capable of running efficiently on a laptop.

## Documentation

Each external function is documented in the `chroma.py` file.
