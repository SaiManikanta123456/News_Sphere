# one.py
import streamlit as st
from two import l1, label_mapping_results
from three import summary
import pickle
from sentence_transformers import SentenceTransformer
import pandas as pd

st.header("News Brooooo😎😎")

df = pd.DataFrame(columns=['Label', 'Category', 'Sentence'])
# for label, sentences in label_mapping_results.items():
#     print(f"Label {label}: {sentences}")

for label, sentences in label_mapping_results.items():
    category = None
    if label == 0:
        category = 'Automobiles'
    elif label == 1:
        category = 'Entertainment'
    elif label == 2:
        category = 'Politics'
    elif label == 3:
        category = 'Science'
    elif label == 4:
        category = 'Sports'
    elif label == 5:
        category = 'Technology'
    elif label == 6:
        category = 'World'
    for sentence in sentences:
        df = df.append({'Label': label, 'Category': category, 'Sentence': sentence}, ignore_index=True)

for category in df['Category'].unique():
        
    st.header(category)
    
    # Filter sentences for the current category
    category_df = df[df['Category'] == category]
    
    # Display sentences for the current category
    for index, row in category_df.iterrows():
        st.write(row['Sentence'])
    
    # Add a horizontal line to separate categories
    st.write("---")

st.subheader("SUMMARY")
st.write(summary)
