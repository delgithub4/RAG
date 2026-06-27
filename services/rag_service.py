from loaders.pdf_loader import PDFLoader
from loaders.text_loader import TextLoader
from chunking.splitter import TextSplitter

class RAGService:

    def __init__(self):

        self.pdf = PDFLoader()

        self.text = TextLoader()

        self.splitter = TextSplitter()

    def chunk_document(
        self,
        text
    ):

        return self.splitter.split(text)
    
    def load_document(
        self,
        filename
    ):

        if filename.endswith(".pdf"):

            return self.pdf.load(filename)

        if filename.endswith(".txt"):

            return self.text.load(filename)

        return "Unsupported document."
