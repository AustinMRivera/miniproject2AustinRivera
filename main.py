# INF601 - Advanced Programming in Python
# Austin Rivera
# Mini Project 2

import pandas as pd
import matplotlib.pyplot as plt

# I'll add the code here step by step. First, loading the data.

# Load the data from the CSV file
# I chose this dataset because it's easy to work with and has director info.
data_file = 'data/netflix_titles.csv'
df = pd.read_csv(data_file)

# Print a quick check to see if it loaded okay
print(df.head())  # Just the first few rows to verify

# Now, filter for movies directed by Ridley Scott
ridley_movies = df[(df['type'] == 'Movie') & (df['director'] == 'Ridley Scott')]

# Count how many there are
count = len(ridley_movies)

# Print the answer
print(f"There are {count} movies directed by Ridley Scott on Netflix.")

# List them out to see the titles
print("The movies are:")
print(ridley_movies['title'])

