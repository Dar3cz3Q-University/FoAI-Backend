import fitz
from fastapi import UploadFile

async def extract_text_from_pdf(file: UploadFile) -> str:
    content = await file.read()
    with fitz.open(stream=content, filetype="pdf") as doc:
        text = ""
        for page in doc:
            text += page.get_text()
    return text
