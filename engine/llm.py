from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

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

