from fastapi import FastAPI

from routes.documents import router as document_router
from routes.chat import router as chat_router

app = FastAPI(
    title="RAG",
    version="1.0.0"
)

app.include_router(document_router)
app.include_router(chat_router)


@app.get("/")
def home():

    return {
        "service": "RAG",
        "status": "running"
    }
