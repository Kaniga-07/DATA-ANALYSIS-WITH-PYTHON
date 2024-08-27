import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder
from textblob import TextBlob

# Load the CSV file
file_path = 'E:/MAINFLOW_INTERN/TASK_6/disney_plus_titles.csv'
df = pd.read_csv(file_path)

# Sentiment Analysis
df_cleaned = df.dropna(subset=['description']).copy()
df_cleaned['sentiment_polarity'] = df_cleaned['description'].apply(lambda x: TextBlob(x).sentiment.polarity)

# Plotting the sentiment distribution
plt.figure(figsize=(10, 6))
plt.hist(df_cleaned['sentiment_polarity'], bins=20, color='purple', edgecolor='black')
plt.title("Sentiment Polarity Distribution of Disney Plus Titles' Descriptions", fontsize=16)
plt.xlabel("Sentiment Polarity", fontsize=12)
plt.ylabel("Frequency", fontsize=12)
plt.grid(True)
plt.show()  # Show first plot

# Clustering based on genres
tfidf_vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf_vectorizer.fit_transform(df['listed_in'].fillna(''))

num_clusters = 5
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
kmeans.fit(tfidf_matrix)
df['genre_cluster'] = kmeans.labels_

# Plotting the genre clusters distribution
plt.figure(figsize=(10, 6))
df['genre_cluster'].value_counts().plot(kind='bar', color='skyblue')
plt.title("Distribution of Genre Clusters", fontsize=16)
plt.xlabel("Cluster", fontsize=12)
plt.ylabel("Number of Titles", fontsize=12)
plt.grid(True)
plt.show()  # Show second plot
