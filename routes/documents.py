from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File
from services.rag_service import RAGService

router = APIRouter(
    prefix="/documents",
    tags=["Documents"]
)

rag = RAGService()

@router.post("/upload")
async def upload_document(
    file: UploadFile = File(...)
):
    content = await file.read()
    with open(
        file.filename,
        "wb"
    ) as document:
        
        document.write(content)

    text = rag.load_document(
        file.filename
    )

    chunks = rag.chunk_document(
        text
    )

    vectors = rag.embed_chunks(
    chunks
    )

    return {

        "filename": file.filename,

        "characters": len(text)

        "chunks": len(chunks)

        "embeddings": len(vectors)

    }
