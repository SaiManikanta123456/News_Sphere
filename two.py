import requests
from sentence_transformers import SentenceTransformer
import pickle
import numpy


l=[]

NEWS_API_KEY = "f2b3464c517f4f7384f0c11efd906bd4"  # Replace with your actual News API key

def get_top_headlines():
    url = f'https://newsapi.org/v2/top-headlines?apiKey={NEWS_API_KEY}&country=in'
    response = requests.get(url)
    data = response.json()
    return data['articles']

articles = get_top_headlines()
c=0

for article in articles:
    c = c + 1
    description = article.get('description')
    if description is not None:
        l.append(description)

    if c == 30:
        break

l1=[]
for i in l:
    try:
        # print(i.encode('ascii', 'ignore').decode('ascii'))
        l1.append(i.encode('ascii', 'ignore').decode('ascii'))
    except UnicodeEncodeError:
        pass


with open(r'D:\python\Face1\Mini_Project\svm_classifier.pkl', 'rb') as file:
    loaded_svm_classifier = pickle.load(file)

def get_embedding(text):
    model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
    text_embedding = model.encode([text])[0]
    return text_embedding

def classify_text(text, svm_classifier):
    text_embedding = get_embedding(text)
    text_embedding_reshaped = text_embedding.reshape(1, -1)
    predicted_label = svm_classifier.predict(text_embedding_reshaped)[0]
    return predicted_label

def create_label_mapping(news_headlines, svm_classifier):
    label_mapping = {}
    for headline in news_headlines:
        predicted_label = classify_text(headline, svm_classifier)
        if predicted_label not in label_mapping:
            label_mapping[predicted_label] = [headline]
        else:
            label_mapping[predicted_label].append(headline)
    return label_mapping

label_mapping_results = create_label_mapping(l1, loaded_svm_classifier)




