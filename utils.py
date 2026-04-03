# utils.py
from pypdf import PdfReader

def extract_text_from_pdf(file) -> str:
    """Extract text from an uploaded PDF file-like object."""
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text
    return text