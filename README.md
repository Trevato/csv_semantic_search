# csv_semantic_search
Semantic search app using streamlit and txtai.

To use the app, upload a csv that you would like to search. Embeddings will index the rows of the csv. Enter a plain text query and get the best results!

## How it works

Pandas is used to read the csv file and each row is converted to a string creating a 1-dimensional array. Each string in this dataframe recieves a high dimension embedding (1D vector of floats) using [txtai](https://github.com/neuml/txtai) embeddings. To save compute, the data is hashed and a pickle file is created so that the data doesn't need to be reindexed. Lastly, the user enters a query to search the data which uses [Approximate Nearest Neighbor](https://en.wikipedia.org/wiki/Nearest_neighbor_search#:~:text=An%20approximate%20nearest%20neighbor%20search%20algorithm%20is%20allowed,is%20almost%20as%20good%20as%20the%20exact%20one.) in the backend. (Implemented within the txtai search function)

## Run locally

*Run it yourself to save me some resources :)*

**Note: Nvidia drivers must be configured properly for GPU access.**

### Just python:

```
$ git clone https://github.com/Trevato/csv_semantic_search.git
$ pip install requirements.txt
$ streamlit run app.py
```

### docker-compose

```
$ docker-compose build --up
```
