import streamlit as st
import pandas as pd
import sem_search

st.title("CSV File Query App")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file, encoding_errors="ignore")
    st.write("Data Preview:")
    st.write(data.head())

    col_options = list(range(data.shape[1]))
    col = st.selectbox("Select a Column", col_options)

    query = st.text_input("Enter Query", "")

    if query:
        try:
            st.write("Top 5:")
            st.write(
                [
                    data.iloc[uid, col]
                    for uid, _ in sem_search.search(
                        data.iloc[:, col].astype(str), query, 5
                    )
                ]
            )
        except Exception as e:
            st.error(f"An error occurred: {e}")
