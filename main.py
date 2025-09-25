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

# Make a graph to show movies by a few directors
directors = ['Ridley Scott', 'Martin Scorsese', 'Steven Spielberg', 'Quentin Tarantino']
counts = []

# Loop through each director and count their movies
for director in directors:
    dir_movies = df[(df['type'] == 'Movie') & (df['director'] == director)]
    counts.append(len(dir_movies))

# Create the bar chart
plt.figure(figsize=(10, 6))  # Make it a bit bigger
plt.bar(directors, counts, color=['blue', 'green', 'red', 'purple'])
plt.title('Number of Movies on Netflix by Selected Directors')
plt.xlabel('Directors')
plt.ylabel('Number of Movies')
plt.xticks(rotation=45)  # Rotate labels for readability

# Save the graph to charts folder
chart_file = 'charts/director_movies.png'
plt.savefig(chart_file)
print(f"Graph saved to {chart_file}")

# Show it 
plt.show()