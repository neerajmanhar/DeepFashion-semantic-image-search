from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
from app.model_loader import load_model, load_index
from app.search_engine import search
from PIL import Image
import io
import os

app = FastAPI()

model = load_model()
index, image_paths = load_index("data/vector.index")

@app.get("/")
def root():
    return {"message": "DeepFashion Search API is working!"}

@app.post("/search/image")
async def search_by_image(file: UploadFile = File(...)):
    img = Image.open(io.BytesIO(await file.read())).convert("RGB")
    results = search(img, model, index, image_paths)
    return {"results": results}

@app.post("/search/text")
async def search_by_text(query: str):
    results = search(query, model, index, image_paths)
    return {"results": results}

@app.get("/images/{image_path:path}")
def serve_image(image_path: str):
    full_path = os.path.join("data", image_path)
    return FileResponse(full_path)
