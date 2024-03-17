
# Data Preparation
import zipfile
import os

with zipfile.ZipFile('netflix_dataset.zip', 'r') as zip_ref
    zip_ref.extractall('Nexflix_shows_movies')

# Check if extraction was successful
print(os.listdir('Netflix_shows_movies'))





# Data Cleansing
import pandas as pd

# Load the dataset
netflix_data = pd.read_csv('Netflix_shows_movies/netflix_data.csv')

# Check for missing values
missing_values = netflix_data.isnull().sum()
print(missing_values)

# Handle missing values based dropping or imputing





# Data Exploration
# Describe the dataset
data_description = netflix_data.describe()
print(data_description)

# Perform statistical analysis
statistical_analysis = netflix_data.groupby('type').agg({'rating': ['mean', 'std']})
print(statistical_analysis)





# Data Visulaisation
import seaborn as sns
import matplotlib.pyplot as plt

# Visualization: Most watched genres
plt.figure(figsize=(10, 6))
sns.countplot(x='listed_in', data=netflix_data, order=netflix_data['listed_in'].value_counts().index[:10])
plt.xticks(rotation=45)
plt.title('Top 10 Most Watched Genres on Netflix')
plt.xlabel('Genre')
plt.ylabel('Count')
plt.show()

# Visualization: Ratings distribution
plt.figure(figsize=(8, 6))
sns.histplot(netflix_data['rating'], bins=10, kde=True)
plt.title('Distribution of Ratings on Netflix')
plt.xlabel('Rating')
plt.ylabel('Frequency')
plt.show()





# R Intergratioin
# Export the dataset to CSV for R
netflix_data.to_csv('netflix_data_for_R.csv', index=False)

