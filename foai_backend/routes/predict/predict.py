from fastapi import HTTPException, APIRouter, UploadFile, File
from typing import List
from foai_model.preprocessing import clean_resume
from foai_model.predict import predict
from foai_backend.utils import extract_text_from_pdf

router = APIRouter(tags=["Predict"])


@router.post("/predict")
async def predict_endpoint(files: List[UploadFile] = File(...)):
    results = []

    for file in files:
        if not file.filename.endswith(".pdf"):
            raise HTTPException(
                status_code=400, detail=f"{file.filename} is not a PDF file"
            )
        content = await extract_text_from_pdf(file)

        cleanedContent = clean_resume(content)
        result = predict(cleanedContent)

        results.append(
            {
                "filename": file.filename,
                "result": result,
            }
        )

    return results
