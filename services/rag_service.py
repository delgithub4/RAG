from loaders.pdf_loader import PDFLoader
from loaders.text_loader import TextLoader


class RAGService:

    def __init__(self):

        self.pdf = PDFLoader()

        self.text = TextLoader()

    def load_document(
        self,
        filename
    ):

        if filename.endswith(".pdf"):

            return self.pdf.load(filename)

        if filename.endswith(".txt"):

            return self.text.load(filename)

        return "Unsupported document."
