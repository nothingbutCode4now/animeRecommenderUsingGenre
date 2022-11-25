# animeRecommenderUsingGenre
Recommend similar anime based on genre-similarity, upon providing an anime name. Genres are first obtained from anime dataset, 
to which TF IDF fit_transform is applied. To this matrix, similarity between genres is computed using Cosine Similarity between each anime to 
every other anime. Finally, top ‘k’ anime that have highest similarity values are fetched and displayed. 

Data set used for anime detais : https://www.kaggle.com/datasets/CooperUnion/anime-recommendations-database

NOTE1: This project uses Content Based filtering for recommendation. Collabortaive filtering can also be used
https://analyticsindiamag.com/collaborative-filtering-vs-content-based-filtering-for-recommender-systems/

TFIDF vectorizer was used to generate vector values which are then operated upon by cosine similarity.
https://medium.com/@cmukesh8688/tf-idf-vectorizer-scikit-learn-dbc0244a911a
https://www.geeksforgeeks.org/cosine-similarity/


NOTE2: Tried building streamlit web app for the same, but struck due to an error.Working on it. WIll fix asap.

Comments are mentioned in the colab book for ease of understanding. Please refer.
Thank You.

