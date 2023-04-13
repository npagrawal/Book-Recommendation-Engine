"""A streamlit app to provide book recommendations."""

import streamlit as st
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import KMeans
from sklearn import neighbors

# Load the data
features = pd.read_csv("data/countvec_df2.csv")
df = pd.read_csv("data/titles.csv")
df = df.sort_values(["author", "title"], ascending=(True, True))

# fit KNN model
model = neighbors.NearestNeighbors(n_neighbors=6, algorithm='ball_tree')
model.fit(features)
dist, idlist = model.kneighbors(features)

# define function
def VibesBookRecommender(book_name, cosine_sim = cosine_sim):
    recommended_books = []
    idx = indices[indices == book_name].index[0]
    score_series = pd.Series(cosine_sim[idx]).sort_values(ascending = False)
    top_5_indices = list(score_series.iloc[1:6].index)
    
    for i in top_5_indices:
        titles = list(df_bagofwords["title"])[i]
        authors = list(df_bagofwords["author"])[i]
        recommended_books.append(f"{titles} by {authors}")
        
    return recommended_books  


st.title("Book Recommender")
st.write("Give me a book title you like and I'll give you five to read next!")

# Create the dropdown menus
authors = df.author.unique()
selected_author = st.selectbox("Choose an author", authors)
titles = df[df.author == selected_author].title.unique()
selected_title = st.selectbox("Now pick a book", titles)

# Call the Recommender function with the selected product and display the results
results = VibesBookRecommender(selected_title, cosine_sim = cosine_sim)
if len(results) == 0:
    st.write("No similar books found.")
else:
    st.write("Add these to your TBR")
    for title in results:
        st.write(title)