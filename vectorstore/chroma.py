from typing import List

from langchain.vectorstores import Chroma
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain.schema.document import Document

embedding_function = SentenceTransformerEmbeddings(
    model_name="all-MiniLM-L6-v2")

db = Chroma(embedding_function=embedding_function)


def save_documents(docs: List[Document]) -> None:
    db.add_documents(docs)


def similarity_query(query: str) -> List[Document]:
    return db.similarity_search(query)
