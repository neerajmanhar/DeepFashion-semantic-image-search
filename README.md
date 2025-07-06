# 👗 DeepFashion Semantic Image Search

A simple yet powerful fashion search engine that uses CLIP embeddings and FAISS to find visually and semantically similar fashion images from the [DeepFashion dataset](https://www.kaggle.com/datasets/pawakapan/deepfashion)      .

Built with:
- 🧠 SentenceTransformer (`clip-ViT-B-32`)
- 🔍 FAISS (HNSW index)
- ⚡ FastAPI (backend)
- 🌐 Streamlit (frontend)

## 📸 Demo

<p align="center">
  <img src="demo/demo.gif" alt="UI Demo" width="700">
</p>

---

## 📂 Project Structure

```

DeepFashion-semantic-image-search/
│
├── app/                     # FastAPI backend
│   ├── main.py              # API endpoints
│   └── search_engine.py     # Search logic
│
├── frontend/                # Streamlit frontend
│   └── app.py
│
├── data/                    # Downloaded files
│   ├── vector.index
│   └── vector.index.paths
│   └── img/..               # Deepfashion dataset
│
├── embeddings/              
│   └── embeddings.ipynb     # Embedding creation notebook
│
├── demo/
│   └── demo.gif             
│
├── requirements.txt
└── README.md

````

---

## 🛠️ Embedding Creation (in Kaggle)

- The image embeddings were generated using the `clip-ViT-B-32` model from `sentence-transformers`.
- Images were loaded recursively from the DeepFashion dataset on Kaggle.
- The notebook used to create the FAISS index is located at:  
  `embeddings/embeddings.ipynb`

After creation:
- `vector.index` and `vector.index.paths` were downloaded
- These are loaded locally during backend startup for fast search

---

## 🚀 How to Run Locally

1. **Clone the repo**

```bash
git clone https://github.com/neerajmanhar/DeepFashion-semantic-image-search.git
cd DeepFashion-semantic-image-search
````

2. **Install dependencies**

```bash
python -m venv fashionenv
source fashionenv/bin/activate  # or .\fashionenv\Scripts\activate on Windows
pip install -r requirements.txt
```

3. **Run FastAPI backend**

```bash
cd app
uvicorn main:app --reload
```

4. **Run Streamlit frontend**

```bash
cd ../frontend
streamlit run app.py
```

---

## 📬 Contact

Made by [Neeraj Manhar](https://github.com/neerajmanhar) — feel free to connect!
[LinkedIN](https://www.linkedin.com/in/neerajmanhar/)

---

