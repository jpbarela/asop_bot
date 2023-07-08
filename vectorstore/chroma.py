from typing import List

from langchain.vectorstores import Chroma
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain.schema.document import Document

from pathlib import Path
import os

embedding_function = SentenceTransformerEmbeddings(
    model_name="all-MiniLM-L6-v2")

persist_folder = str(Path(__file__).parent.joinpath("chroma_data"))

if os.environ.get("TESTING"):
    persist_folder = None

db = Chroma(embedding_function=embedding_function,
            persist_directory=persist_folder)


def save_documents(docs: List[Document]) -> None:
    db.add_documents(docs)


def similarity_query(query: str) -> List[Document]:
    return db.similarity_search(query)
