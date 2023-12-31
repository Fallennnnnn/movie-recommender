# -*- coding: utf-8 -*-
"""Movie Recommender System.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10wZ3ogcu4YENSZJEo9eGrQxG1ziP0ij-

# **Movie Recommender System**

# Data Load and Understanding

## Import necessary libraries
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from surprise import Dataset, Reader, KNNBasic
from surprise.model_selection import train_test_split
from surprise import accuracy
from sklearn.metrics.pairwise import linear_kernel
from sklearn.preprocessing import MinMaxScaler
from sklearn.feature_extraction.text import TfidfVectorizer

"""## Load the dataset"""

url = "https://raw.githubusercontent.com/Fallennnnnn/movie-recommender/main/Dataset/mymoviedb.csv"
movies = pd.read_csv(url, lineterminator='\n')

"""## Check dataset"""

movies.head()

"""**Tabel 1**

Mengecek dataset didalam data csv

## Exploratory Data Analysis
"""

movies.info()

movies.columns

movies.describe()

"""**Tabel 2**

Melakukan pengecekan informasi dari dataset

### Visualize Table
"""

# Visualize the distribution of movie ratings (Vote_Average)
plt.figure(figsize=(8, 6))
sns.histplot(data=movies, x='Vote_Average', bins=30, kde=True)
plt.title('Distribution of Movie Ratings')
plt.xlabel('Vote_Average')
plt.ylabel('Frequency')
plt.show()

"""**Gambar 1.**
Dapat dilihat dari Gambar 1 visualisasi rata rata rating dari film berada pada 6 hingga 8
"""

# Visualize the scatter plot of ratings vs. popularity
plt.figure(figsize=(8, 6))
sns.scatterplot(data=movies, x='Vote_Average', y='Popularity')
plt.title('Ratings vs. Popularity of Movies')
plt.xlabel('Vote_Average')
plt.ylabel('Popularity')
plt.show()

"""**Gambar 2.**

Gambar tersebut menunjukkan scatter plot dari peringkat dan popularitas film. Peringkat adalah nilai dari 1 hingga 10 yang diberikan oleh pengguna untuk film tersebut, sedangkan popularitas adalah jumlah pengguna yang telah menonton film tersebut. Dari gambar tersebut, dapat dilihat bahwa terdapat hubungan positif antara peringkat dan popularitas. Artinya, film-film dengan peringkat yang lebih tinggi juga cenderung lebih populer.
"""

# Visualize the distribution of movie genres
genre_counts = movies['Genre'].str.split(',').explode().str.strip().value_counts()
plt.figure(figsize=(12, 8))
sns.barplot(x=genre_counts.values, y=genre_counts.index, orient='h')
plt.title('Distribution of Movie Genres')
plt.xlabel('Number of Movies')
plt.ylabel('Genre')
plt.show()

"""**Gambar 3**

Pada gambar 3 diatas merupakan distribusi jumlah film berdasarkan genrenya dimana film dengan genre terbanyak adalah drama, comedy, dan action
"""

# Sort the dataset by popularity in descending order to get the most popular movies
top_popular_movies = movies.sort_values(by='Popularity', ascending=False).head(10)

# Create a bar plot to visualize the top-rated movies based on their titles
plt.figure(figsize=(12, 8))
sns.barplot(data=top_popular_movies, x='Popularity', y='Title', palette='viridis')
plt.title('Top 10 Most Popular Movies by Title')
plt.xlabel('Popularity')
plt.ylabel('Movie Title')
plt.xticks(rotation=0)
plt.show()

"""**Gambar 4**

Dapat dilihat pada gambar diatas film dengan popularitas tertinggi adalah **Spider Man No Way Home** disusul dengan **The Batman** dan **No Exit**
"""

# Convert the 'Release_Date' column to a datetime object
movies['Release_Date'] = pd.to_datetime(movies['Release_Date'])

# Extract year and month from the release date
# Filter the dataset to include only releases between 2000 and 2024
movies_filtered = movies[(movies['Release_Date'].dt.year >= 2000) & (movies['Release_Date'].dt.year <= 2024)]
movies['Release_Month'] = movies['Release_Date'].dt.month

# Plot the distribution of movie releases by year
plt.figure(figsize=(12, 6))
sns.countplot(data=movies_filtered, x='Release_Year', palette='viridis')
plt.title('Distribution of Movie Releases by Year')
plt.xlabel('Release Year')
plt.ylabel('Number of Movies')
plt.xticks(rotation=45)
plt.show()

# Plot the distribution of movie releases by month
plt.figure(figsize=(10, 6))
sns.countplot(data=movies, x='Release_Month', palette='viridis')
plt.title('Distribution of Movie Releases by Month')
plt.xlabel('Release Month')
plt.ylabel('Number of Movies')
plt.xticks(rotation=45)
plt.show()

"""**Gambar 5**

Dapat dilihat pada visualisasi diatas adalah distribusi jumlah film berdasarkan waktu rilisnya dan film terbanyak rilis di tahun 2021 dan untuk bulan rilis teranyak pada bulan 10

# Data Preparation
"""

# Check Null Values
movies.isnull().sum()

# Check Duplicate
movies.duplicated().any()

# Check column correlation
correlation_matrix = movies.corr()
plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix')
plt.show()

"""## Feature Engineering"""

# Drop Unecessary column
movies = movies.drop(['Poster_Url'], axis=1)

# Assuming 'Genre' is a list of genres separated by '|'
movies['Genres'] = movies['Genre'].str.split('|')

# Create a TF-IDF vectorizer for movie overviews
tfidf_vectorizer = TfidfVectorizer(stop_words='english')
movies['Overview'] = movies['Overview'].fillna('')
tfidf_matrix = tfidf_vectorizer.fit_transform(movies['Overview'])

movies.info()

"""# Modelling and Evaluation

## Content-Based Filtering
"""

# Calculate cosine similarity between movie overviews
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# Function to get movie recommendations based on movie title
def get_content_based_recommendations(title, cosine_sim=cosine_sim):
    # Check if the title is in the 'Title' column
    if title not in movies['Title'].values:
        return "Movie title not found in the dataset."

    # Get the index of the movie title
    idx = movies.index[movies['Title'] == title].tolist()[0]

    # Calculate similarity scores
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get top 10 similar movies
    sim_scores = sim_scores[1:11]
    movie_indices = [i[0] for i in sim_scores]

    # Retrieve recommended movies' titles and genres
    recommended_movies = movies[['Title', 'Genre']].iloc[movie_indices]

    return recommended_movies

# Get content-based recommendations for a movie title
content_based_rec = get_content_based_recommendations('Spider-Man: No Way Home')
content_based_rec

"""## Hybrid Recommendation"""

# Sort movies by popularity (e.g., 'Popularity' or 'Vote_Count')
popularity_based_rec = movies.sort_values(by='Popularity', ascending=False)['Title'].head(10)
print(popularity_based_rec)

# Function to get hybrid recommendations with a limit of 10 recommendations
def get_hybrid_recommendations(title):
    content_rec = get_content_based_recommendations(title)
    popularity_rec = movies.sort_values(by='Popularity', ascending=False)[['Title', 'Genre']].head(10)
    hybrid_rec = content_rec.append(popularity_rec).drop_duplicates().head(10)
    return hybrid_rec

# Get hybrid recommendations for a movie title
hybrid_rec = get_hybrid_recommendations('The Commando')
hybrid_rec