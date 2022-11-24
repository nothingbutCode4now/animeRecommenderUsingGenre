import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.feature_extraction.text import TfidfVectorizer
import re

anime = pd.read_csv("A.csv")
anime_rating = pd.read_csv('rating.csv')

anime_rating.drop_duplicates(keep='first',inplace=True)
anime.drop_duplicates(keep='first',inplace=True)

for i in anime['name']:
  re.sub('&','and',i)
  re.sub('"', '', i)
  re.sub('.hack//', '', i)
  re.sub("A's", '', i)
  re.sub("'", '', i)
  re.sub("I'","I\'",i)

anime_rating = anime_rating[~(anime_rating.rating == -1)]

tf = TfidfVectorizer()
tf.fit(anime['genre'].values.astype('U'))
tfidf_matrix = tf.fit_transform(anime['genre'].values.astype('U'))


mat = pd.DataFrame(tfidf_matrix.todense(), columns=tf.get_feature_names(),index=anime.name)

from sklearn.metrics.pairwise import cosine_similarity
cosine_sim = cosine_similarity(tfidf_matrix) 

cosine_sim_df = pd.DataFrame(cosine_sim, index=anime['name'], columns=anime['name'])

def recc(name, k, similarity_data=cosine_sim_df, items=anime[['name', 'genre']]):
    index = similarity_data.loc[:,name].to_numpy().argpartition(
        range(-1, -k, -1))
    
    closest = similarity_data.columns[index[-1:-(k+2):-1]]

    closest = closest.drop(name, errors='ignore')
 
    return pd.DataFrame(closest).merge(items).head(k)


st.title("Get Recommendations for an Anime")
ip = st.text_input("Enter the Anime name here")
ip2 = st.number_input("enter number of recommendations required")
op = recc(ip,int(ip2))
st.title(op)
