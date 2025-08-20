from fastapi import APIRouter
from services.pdf_service import generate_pdf_from_images

router = APIRouter()

@router.get("/generate")
def generate_pdf():
    """
    Generate a PDF from images in the configured folder
    """
    response = generate_pdf_from_images()
    return response
