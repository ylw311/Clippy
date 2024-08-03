from langchain_openai import ChatOpenAI
import subprocess
import os
from dotenv import load_dotenv

load_dotenv()


def run_matlab_code(code, logging):
    current_directory = os.path.dirname(__file__)
    output_file_path = os.path.join(current_directory, "res.m")

    try:
        with open(output_file_path, "w") as file:
            file.write(code)
        logging.info(f"Response successfully written to {output_file_path}")

        matlab = os.getenv("MATLAB_PATH")

        # subprocess.run([matlab, "-batch", f"run('{output_file_path}')"], check=True)
        subprocess.run([matlab, "-r", f"run('{output_file_path}');"], check=True)
        logging.info("MATLAB code executed successfully.")

    except FileNotFoundError as e:
        logging.info(f"An error occurred: {e}")


def start(instruction: str, logging):
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
            "You are an expert MATLAB coding assistant. Your task is to convert a given instruction into complete, runnable MATLAB code. The code should be functional without requiring any modifications, this means do not return code that requires input of an API key. Return the MATLAB code directly, do not return it in a code block or include any additional text or explanations.",
        ),
        ("human", instruction),
    ]
    res = llm.invoke(messages)

    run_matlab_code(res.content, logging)
