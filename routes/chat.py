from fastapi import APIRouter

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)


@router.post("/ask")
def ask(
    question: str
):

    return {

        "question": question,

        "answer": "Coming soon..."

    }
