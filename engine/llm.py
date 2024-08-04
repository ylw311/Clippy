from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from utils.embeddings import text_to_embedding, get_top_k_similar_embeddings
import pyperclip

load_dotenv()

def query_llm(text: str):
    # sample: Write a matlab code that prints hi nathan in terminal  Write a matlab code that prints hi nathan in terminal
    llm = ChatOpenAI(
        model="gpt-4o",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
    )

    messages = [
        (
            "system",
            "Given the user's text, you are to provide a response that is relevant to the user's text. This could either be summarization or a response to a question",
        ),
        ("human", text),
    ]
    res = llm.invoke(messages)
    
    return res.content


def query_llm(prompt, collection):

    prompt_embedding = text_to_embedding(prompt)

    # Retrieve the top 5 similar documents
    top_documents = get_top_k_similar_embeddings(prompt_embedding, collection)

    # Extract text from the top documents
    context = " ".join([doc["text"] for doc in top_documents])

    full_prompt = f"{context}\n\n{prompt}"

    llm = ChatOpenAI(
        model="gpt-4o",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
    )

    response = llm.generate(full_prompt)

    # Copy the response to the clipboard
    pyperclip.copy(response)

    return response

