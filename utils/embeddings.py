from langchain.embeddings import OpenAIEmbeddings
import os

# Initialize the embeddings model
def get_embedding_model():
    return OpenAIEmbeddings()  # Adjust to your specific model

def text_to_embedding(text):
    model = get_embedding_model()
    embedding = model.embed_text(text)
    return embedding
