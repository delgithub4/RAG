from pypdf import PdfReader


class PDFLoader:

    def load(self, path):

        reader = PdfReader(path)

        text = ""

        for page in reader.pages:

            text += page.extract_text()

        return text
