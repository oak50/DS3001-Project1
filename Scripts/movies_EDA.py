# perform EDA

# import pandas & load dataset
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# load dataset into dataframe
df = pd.read_csv('Data/movie_dataset.csv',low_memory=False)

# Look at first few rows
df_head = df.head()
print(df_head)

# print list of column names
print(df.columns.tolist())
column_count = df.columns.tolist()
print("\n")
print("original number of variables: \n", len(column_count))

# Conduct EDA:

# DIRECTORS

# Create a table showing the number of movies directed by each director
director_counts = df['director'].value_counts().to_frame().reset_index()
director_counts.columns = ['Director', 'Number of Movies Directed']
print(director_counts)
print( '\n' )

# Create descriptive statistics table for movies per director:
director_counts = df['director'].value_counts()
descriptive_stats = director_counts.describe()
print("Descriptive Statistics for Number of Movies Per Director:")
print(descriptive_stats)
print( '\n' )

# Create a histogram showing the distribution of movies directed per director:
director_counts = df['director'].value_counts()
distribution = director_counts.value_counts().sort_index()
plt.figure(figsize=(10, 6))
plt.bar(distribution.index, distribution.values, color='skyblue')
plt.xlabel('Number of Movies Directed (Movie Count)')
plt.ylabel('Number of Directors (Director Count)')
plt.title('Distribution of Movies Directed Per Director')
plt.xticks(range(0, 28))
plt.show()
plt.savefig( "EDA_plots/movies_per_director_histogram.png" )
print( '\n' )


# MOVIE RUNTIME IN MINUTES

# Descriptive statistics for runtime:
runtime_table = df[ "runtime" ].describe()
print( "Descriptive statistics for movie runtime: \n", runtime_table )

# Histogram for runtime:
plt.figure(figsize=(10, 6))
plt.hist(df['runtime'], bins=50, color='skyblue', edgecolor='black')
plt.xlabel('Movie Runtime (minutes)')
plt.ylabel('Number of Movies')
plt.title('Distribution of Movie Runtimes')
plt.show()
plt.savefig( "EDA_plots/movie_runtime_histogram.png" )

# Scatterplot for runtime vs. average rating:
plt.figure(figsize=(10, 6))
plt.scatter(df['runtime'], df['vote_average'], color='skyblue', edgecolor='black')
plt.xlabel('Movie Runtime (minutes)')
plt.ylabel('Average rating by Users')
plt.title('Scatter Plot of Movie Rating vs. Runtime')
plt.grid(True)
plt.show()
plt.savefig( "EDA_plots/movie_runtime_vs_rating_scatter.png" )
# scatterplot appears nonlinear, minimal correlation between runtime and user rating. Let's run a correlation:

runtime_rating_correlation = df['runtime'].corr(df['vote_average'])
print(f"Correlation between Movie Runtime and User Rating: {runtime_rating_correlation:.2f}")
# movie rating and runtime have a positive correlation of 0.38





