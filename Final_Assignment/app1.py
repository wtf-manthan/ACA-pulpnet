import streamlit as st
from transformers import pipeline
from sentence_transformers import SentenceTransformer, util

qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")

embedder = SentenceTransformer('all-MiniLM-L6-v2')

with open("iitk_vox_articles_fin.txt", "r", encoding="utf-8") as f:
    articles = f.read().split('---')

article_embeddings = embedder.encode(articles, convert_to_tensor=True)

def get_top_articles(query, k=3):
    query_embedding = embedder.encode(query, convert_to_tensor=True)
    similarities = util.cos_sim(query_embedding, article_embeddings)[0]
    top_indices = similarities.argsort(descending=True)[:k]
    return [articles[i] for i in top_indices]

st.title("IITK VoxPopuli Chatbot")
st.write("Ask anything related to IITK Vox articles!")

user_question = st.text_input("Type your question:")

if user_question:
    st.write("Fetching answer...")
    top_contexts = "\n".join(get_top_articles(user_question, k=25))
    answer = qa_pipeline(question=user_question, context=top_contexts)

    st.subheader("Answer:")
    st.write(answer['answer'])