from fastapi import FastAPI, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from services.file_service import FileService
from services.gemini_service import GeminiService
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(debug=True)
file_service = FileService()
gemini_service = GeminiService()

@app.post("/v1/pdf")
async def upload_file(file: UploadFile):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are supported.")
    try:
        file_id, file_path = file_service.save_file(await file.read())

        return JSONResponse(
            content={
                "message": "PDF uploaded successfully.",
                "file_id": file_id,
                "file_path": file_path,
            },
            status_code=200,
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"File upload error: {str(e)}")

@app.get("/v1/chat/{file_id}")
async def query_pdf(file_id: str, question: str):
    if file_id not in file_service.data_store:
        raise HTTPException(status_code=404, detail="File ID not found.")
    try:
        text = file_service.data_store[file_id]["text"]
        answer = gemini_service.query(text, question)
        return {"answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Query error: {str(e)}")
