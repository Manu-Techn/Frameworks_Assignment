# ---------------------------------
# PART 4: STREAMLIT APP
# ---------------------------------

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Load the dataset
df = pd.read_csv("metadata.csv.zip")

# Convert publish time to date time and extract year
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
df['year'] = df['publish_time'].dt.year

# Streamlit layout
st.title("CORD-19 Data Explorer")
st.write("An interactive exploration of COVID-19 research papers.")

# Show sample data
st.subheader("Sample Data")
st.dataframe(df.head(20))

# Interactive filter
min_year = int(df['year'].min())
max_year = int(df['year'].max())
year_range = st.slider("Select publication year range", min_year, max_year, (2020, 2021))

filtered_df = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

# publications over time
st.subheader("Publications Over Time")
year_counts = filtered_df['year'].value_counts().sort_index()
fig, ax = plt.subplots()
sns.barplot(x=year_counts.index, y=year_counts.values, ax=ax)
ax.set_title("Number of publications per Year")
st.pyplot(fig)

# Top journals
st.subheader("Top Journals")
top_journals = filtered_df['journal'].value_counts().head(10)
fig, ax = plt.subplots()
sns.barplot(y=top_journals.index, x=top_journals.values, ax=ax)
ax.set_title("Top 10 Journals by Publication Count")
st.pyplot(fig)

# Word Cloud of Titles
st.subheader("Word Cloud of Paper Titles")
text = " ".join(title for title in filtered_df['title'].dropna())
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
fig, ax = plt.subplots(figsize=(10, 5))
ax.imshow(wordcloud, interpolation="bilinear")
ax.axis("off")
st.pyplot(fig)

# Distribution by Source
st.subheader("Distribution by Source")
source_counts = filtered_df['source_x'].value_counts()
fig, ax = plt.subplots()
sns.barplot(y=source_counts.index, x=source_counts.values, ax=ax)
ax.set_title("Publications by Source")
st.pyplot(fig)



