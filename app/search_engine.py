import numpy as np
from PIL import Image
import os

def normalize(vec):
    return vec / np.linalg.norm(vec)

def search(query, model, index, image_paths, top_k=5):
    # Case 1: if query is an image path and file exists
    if isinstance(query, str) and os.path.isfile(query):
        query = Image.open(query).convert('RGB')
    
    # Case 2: if it's still a string (assume it's text)
    elif isinstance(query, str):
        pass  # it's a text prompt, use as-is
    
    # Case 3: If it's already an Image (like from upload)
    else:
        query = query  # do nothing
    
    # Generate embedding
    vec = model.encode(query, convert_to_numpy=True).astype(np.float32)
    vec = normalize(vec)

    D, I = index.search(vec.reshape(1, -1), top_k)
    return [image_paths[i] for i in I[0]]
