# For handling file uploads and text extraction
# We use PyMuPDF for PDF text extraction

import pymupdf

def extract_text_from_pdf(pdf_path):
    try:
        with pymupdf.open(pdf_path) as pdf:
            text = ""
            for page in pdf:
                text += page.get_text()
        return text
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return ""

# Loads text from a .txt file.
def load_text_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except Exception as e:
        print(f"Error reading text file: {e}")
        return ""
