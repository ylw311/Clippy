import validators
import uuid


def is_url(text):
    return validators.url(text)




def create_message(prompt):
    return {
        "prompt": prompt,
        "id": uuid.uuid4().hex  # Using .hex to get a string representation of the UUID
    }

