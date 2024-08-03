from langchain_openai import ChatOpenAI
import subprocess
import os
from dotenv import load_dotenv


load_dotenv()

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
        "You are a helpful assistant that takes an instruction and writes a working matlab code for it. The matlab code should be complete and runnable. Return the code directly with no code block formatting, do not return any other information.",
    ),
    ("human", "Write a matlab code that prints 'Hello, World!' to the console."),
]
res = llm.invoke(messages)

current_directory = os.path.dirname(__file__)
output_file_path = os.path.join(current_directory, "res.m")

try:
    with open(output_file_path, "w") as file:
        file.write(res.content)
    print(f"Response successfully written to {output_file_path}")

    matlab = os.getenv("MATLAB_PATH")

    subprocess.run([matlab, "-batch", f"run('{output_file_path}')"], check=True)
    print("MATLAB code executed successfully.")


except FileNotFoundError as e:
    print(f"An error occurred: {e}")
