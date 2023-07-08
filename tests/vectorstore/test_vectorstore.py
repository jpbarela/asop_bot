from vectorstore import save_documents, similarity_query
from langchain.schema.document import Document


def test_round_trip() -> None:
    test_document = Document(page_content="A document")
    save_documents([test_document])
    docs = similarity_query("What is a document?")
    assert len(docs) == 1
    assert docs[0] == test_document
