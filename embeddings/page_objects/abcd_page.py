from typing import List

from bs4 import BeautifulSoup


class AbcdPage():
    """
        A page representing the Actuarial Board for Counseling and Discipline ASOP page
    """

    def __init__(self, content):
        self._content = BeautifulSoup(content, "html.parser")

    def pdf_links(self) -> List[str]:
        """
            Returns a list of urls to PDF versions of the ASOPs
        """
        pdf_links = self._content.find_all("a", string="Download PDF")
        return [pdf_link["href"] for pdf_link in pdf_links]
