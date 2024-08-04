from langchain_community.embeddings import OpenAIEmbeddings
from db.mongodb_vector_embedding import get_mongo_collection
import numpy as np
import os

# Initialize the embeddings model
def get_embedding_model():
    return OpenAIEmbeddings()

# convert text to embedding
def text_to_embedding(text):
    model = get_embedding_model()
    embedding = model.embed_text(text)
    return embedding


# not sure if langchain has this already set up (will do this manually)
def cosine_similarity(vec1, vec2):

    # regular dot product of two vectors
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))


def get_top_k_similar_embeddings(query_embedding, collection, k=5):
    collection = get_mongo_collection()

    documents = collection.find()  
    similarities = []

    # Calculate the cosine similarity between the query embedding and each document embedding
    for doc in documents:
        embedding = np.array(doc["embedding"])
        similarity = cosine_similarity(query_embedding, embedding)
        similarities.append((doc, similarity))

    # Sort the documents by similarity
    similarities.sort(key=lambda x: x[1], reverse=True)

    # Get the top k most similar documents
    top_k_documents = [doc for doc, _ in similarities[:k]]

    return top_k_documents
