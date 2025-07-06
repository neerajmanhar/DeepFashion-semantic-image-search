import faiss
from sentence_transformers import SentenceTransformer

def load_model():
    return SentenceTransformer("clip-ViT-B-32")

def load_index(index_path):
    index = faiss.read_index(index_path)
    with open(index_path + '.paths', 'r') as f:
        paths = [line.strip() for line in f.readlines()]
    return index, paths
