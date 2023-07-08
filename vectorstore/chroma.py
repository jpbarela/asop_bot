from typing import List

from langchain.vectorstores import Chroma
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain.schema.document import Document
import chromadb
from chromadb.config import Settings

from pathlib import Path
import os

embedding_function = SentenceTransformerEmbeddings(
    model_name="all-MiniLM-L6-v2")

persist_folder = str(Path(__file__).parent.joinpath("chroma_data"))

if os.environ.get("TESTING"):
    persist_folder = None

client = chromadb.Client(
    Settings(chroma_db_impl='duckdb+parquet', persist_directory=persist_folder))

collection_name = "asops"


def count() -> int:
    collection = client.get_collection(name=collection_name)
    return collection.count()


def delete_store() -> None:
    client.reset()
    client.create_collection(collection_name)


def save_documents(docs: List[Document]) -> None:
    db = _get_chroma_db()
    db.add_documents(docs)


def similarity_query(query: str) -> List[Document]:
    db = _get_chroma_db()
    return db.similarity_search(query)


def _get_chroma_db():
    return Chroma(collection_name=collection_name,
                  embedding_function=embedding_function,
                  persist_directory=persist_folder,
                  client=client)
