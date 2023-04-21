from txtai.embeddings import Embeddings

embeddings = Embeddings({"path": "sentence-transformers/nli-mpnet-base-v2"})


def search(data, q, n=5):
    embeddings.index([(uid, text, None) for uid, text in enumerate(data)])

    return embeddings.search(q, n)
