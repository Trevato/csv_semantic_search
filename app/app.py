import streamlit as st
import pandas as pd
import hashlib
import pickle
import os

from txtai.embeddings import Embeddings

embeddings = Embeddings({"path": "sentence-transformers/nli-mpnet-base-v2"})

if not os.path.exists("ebedding_storage/"):
    os.makedirs("embedding_storage/")


def create_1d_string_list(data, cols):
    data_rows = data[cols].astype(str).values
    return [" ".join(row) for row in data_rows]


def get_data_hash(data):
    data_str = data.to_string()
    return hashlib.md5(data_str.encode()).hexdigest()


def load_embeddings_from_db(data_hash):
    try:
        with open(f"./embedding_storage/{data_hash}.pkl", "rb") as f:
            print(f)
            return pickle.load(f)
    except FileNotFoundError:
        return None


def save_embeddings_to_db(data_hash, embeddings):
    with open(f"./embedding_storage/{data_hash}.pkl", "wb") as f:
        pickle.dump(embeddings, f)


@st.cache_data
def index_data(data):
    data_hash = get_data_hash(data)
    cached_embeddings = load_embeddings_from_db(data_hash)
    if cached_embeddings is not None:
        return cached_embeddings

    data_1d = create_1d_string_list(data, data.columns)
    embeddings.index([(uid, text, None) for uid, text in enumerate(data_1d)])

    save_embeddings_to_db(data_hash, embeddings)

    return embeddings


st.title("CSV File Query App")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file, encoding_errors="ignore")
    st.write("Data Preview:")
    st.write(data.head())

    embeddings = index_data(data)

    query = st.text_input("Enter Query", "")

    if query:
        try:
            st.write("Top 5:")
            result_ids = [uid for uid, _ in embeddings.search(query, 5)]
            result_df = data.loc[result_ids].reset_index(drop=True)
            st.write(result_df)
        except Exception as e:
            st.error(f"An error occurred: {e}")
