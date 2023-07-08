import pathlib

from embeddings.page_objects import AbcdPage


def test_pdf_links() -> None:
    dir = pathlib.Path(__file__).parent.resolve()
    f = open(dir.joinpath("abcd.html"), "r")
    page = AbcdPage(f.read())
    f.close()

    results = page.pdf_links()
    assert len(results) == 57
    assert results[0] == "http://www.actuarialstandardsboard.org/wp-content/uploads/2013/10/asop001_170.pdf"
