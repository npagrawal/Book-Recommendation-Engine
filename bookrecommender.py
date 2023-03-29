import streamlit as st
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


# load model
# with open('vec.pkl', 'rb') as vec:
#     vec = pickle.load(vec)

# # load vectorizer
# with open('count_matrix.pkl', 'rb') as count_matrix:
#     count_matrix = pickle.load(count_matrix)

books_vector = pd.read_csv("countvec_df2.csv")


    
# count vectorizer-based recommender
# def VibesBookRecommender(book_name, cosine_sim = cosine_sim):
#     recommended_books = []
#     idx = indices[indices == book_name].index[0]
#     score_series = pd.Series(cosine_sim[idx]).sort_values(ascending = False)
#     top_5_indices = list(score_series.iloc[1:6].index)
    
#     for i in top_5_indices:
#         titles = list(df_bagofwords["title"])[i]
#         authors = list(df_bagofwords["author"])[i]
#         recommended_books.append(f"{titles} by {authors}")
        
#     return recommended_books



st.title("Book Recommender")
st.write("Give me a book title and I'll give you five to read next!")

author = st.multiselect(label = "author", options = books_vector["author"])

titles = st.multiselect(label = "titles", options = books_vector.loc[books_vector['author'] == author,'title'])
    
# go = st.button('press for rec')

# if go:

#     book = books_vector.loc[(books_vector["author"] == author) & (books_vector["title"] == titles)]
#     cosine_sim = cosine_similarity(book, books_vector.loc[(df1["author"] != author) & (books_vector["title"] != titles)])
#     book_index = np.argmax(cosine_sim,axis=1)
#     go = st.button('press for rec') 


#     st.dataframe(books_vector[book_index][['author','title']])                              
