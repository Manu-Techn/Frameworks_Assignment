# --------------------------------
# PART 1: DATA LOADING
# --------------------------------

import pandas as pd
import zipfile

df = None

# Load a sample of the dataset
try:
    df = pd.read_csv("metadata.csv.zip", nrows=1000)
    print("Direct ZIP read successful!")
    print(df.head())
except Exception as e1:
    print("Direct ZIP read failed:", e1)
    # Try reading the zip file explicitly
    try:
        with zipfile.ZipFile("metadata.csv.zip", "r") as z:
            csv_name = z.namelist()[0]  # first file inside zip
            with z.open(csv_name) as f:
                df = pd.read_csv(f, nrows=1000)
                print("Explicit ZIP read successful!")
                print(df.head())
    except Exception as e2:
        print("Both methods failed:", e2)

# Only continue if df was successfully loaded
if df is not None:
    print("\n--- First 5 rows ---")
    print(df.head())

    print("\n--- Shape (rows, columns) ---")
    print(df.shape)

    print("\n--- Data types ---")
    print(df.dtypes)

    print("\n--- Missing values ---")
    print(df.isnull().sum().sort_values(ascending=False).head(20))

    print("\n--- Summary statistics ---")
    print(df.describe())

# --------------------------------
# PART 2: DATA CLEANING
# --------------------------------

import pandas as import pd

# load 1000 rows from the csv file
df = pd.read_csv("metadata.csv.zip", nrows=1000)

# First 5 rows
print("\n--- First 5 rows ---")
print(df.head())

# Shape of the Dataset
print("\n---Shape (rows, columns) ---")
print(df.shape)

# Data types
print("\n--- Data types ---")
print(df.dtypes)

# Missing values
print("\n--- Missing values  (top 20) ---")
print(df.isnull().sum().sort_values(ascending=False).head(20))

# Summary statistics
print("\n--- Summary statistics ---")
print(df.describe())

# ---------------------------------
# PART 3: DATA ANALYSIS AND VISUALIZATION
# ---------------------------------

import matplotlib.pypilot as plt
import seaborn as sns
from collections import Counter
from wordcloud import WordCloud

# Count papers by publication year
year_counts = diff['year'].value_counts().sort_index()
print(year_counts)

plt.figure(figsize=(8, 5))
sns.barplot(x=year_counts.index, y=year_counts.values, color="skyblue")
plt.title("Publications by Year")
plt.xlabel("Year")
plt.ylabel("Number of publications")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Identify top journals
top_journals = dff['journal'].value_counts().head(10)
print("\n--- Top 10 Journals ---")
print(top_journals)

plt.figure(figsize=(10, 6))
sns.barplot(y=top_journals.index, x=top_journals.values, palette="virdis")
plt.title("Top 10 Journals Publishing COVID-19 Research")
plt.xlabel("Number of papers")
plt.ylabel("Journal")
plt.tight_layout()
plt.show()

# Simple word frequency analysis
titles = df['title'].dropna().str.cat(sep=" ").lower()
words = [w for w in titles.split() if len(w) > 3]
word_freq = Counter(words).most_common(20)

print("\n--- Most frequent words in paper titles ---")
print(words_freq)

# Visualizations plot number 
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(" ".join(words))
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title("Word Cloud of Paper Titles")
plt.show()

# Distribution of paper by source
source_counts = dff['source_x'].value_counts().head(10)
print("\n--- Top 10 Sources ---")
print(source_counts)

plt.figure(figsize=(10, 6))
sns.barplot(y=source_counts.index, x=source_counts.values, palette="magma")
plt.title("Top 10 Sources of COVID-19 Research Papers")
plt.xlabel("Number of papers")
plt.ylabel("Source")
plt.tight_layout()
plt.show()


