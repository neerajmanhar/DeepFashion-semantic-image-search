import streamlit as st
import requests

# Set up the page
st.set_page_config(page_title="DeepFashion Search", layout="wide")
st.title("👗 DeepFashion Semantic Search")

# Constants
BACKEND_URL = "http://localhost:8000"
PATHS_FILE = "data/vector.index.paths"

# Helper to render results horizontally
def render_results(results, title):
    st.markdown(f"### {title}")
    cols = st.columns(len(results))
    for col, r in zip(cols, results):
        with col:
            st.image(f"{BACKEND_URL}/images/{r}", use_container_width=True)
            st.caption(r)

# ------------------------ Text Query ------------------------
st.header("🧠 Search by Text")
query = st.text_input("Describe your desired fashion item (e.g. 'floral summer dress')")
if st.button("Search"):
    if query.strip():
        res = requests.post(f"{BACKEND_URL}/search/text", params={"query": query})
        results = res.json()["results"]
        render_results(results, f"🧠 Results for: *{query}*")
    else:
        st.warning("Please enter a valid query.")

# ------------------------ Image Upload ------------------------
st.header("📤 Search by Image")
uploaded = st.file_uploader("Upload a fashion image", type=["jpg", "jpeg", "png"])
if uploaded and st.button("Search by Image"):
    st.markdown("#### ✅ You uploaded:")
    st.image(uploaded, width=250)
    
    res = requests.post(f"{BACKEND_URL}/search/image", files={"file": uploaded.getvalue()})
    results = res.json()["results"]
    render_results(results, "📸 Results for uploaded image")
