from fastapi import FastAPI
from controllers.pdf_controller import router as pdf_router

app = FastAPI()

# include routes
app.include_router(pdf_router, prefix="/pdf", tags=["PDF Service"])