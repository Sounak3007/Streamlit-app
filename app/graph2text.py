import os
from openai import OpenAI

api_key = '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'
client = OpenAI(api_key=api_key)

system = f"""
You are an assistant that helps to generate text to form nice and human understandable answers based.
The latest prompt contains the information, and you need to generate a human readable response based on the given information. The prompt might contain tabular data so format it accordingly.
Make it sound like the information are coming from an AI Assistant, but don't add any information.
The data is from India's National Tuberculosis Management system called Ni-kshay or Nikshay.
Summarize or Categorize the results if asked for. If summary is asked for in the prompt and no data is explicitly provided, summarize the last generated response.
If categorization by Severity is asked, categorize the text data for impact on a person's health and well being.
"""
# system = f"""
# You are an assistant that helps to generate text to form nice and human understandable answers based.
# The latest prompt contains the information, and you need to generate a human readable response based on the given information.
# Make it sound like the information are coming from a 5 year old, and try to sound funny.
# Summarize the results if asked for.
# """
#Do not add any additional information that is not explicitly provided in the latest prompt.
#I repeat, do not add any information that is not explicitly given.


def generate_response(messages):
    messages = [
        {"role": "system", "content": system}
    ] + messages
    print(messages)

    # Make a request to OpenAI
    completions = client.chat.completions.create(
        model="gpt-3.5-turbo-16k",
        messages=messages,
    )
    print("graphtotext")
    response = completions.choices[0].message.content
    print(response)
    # If the model apologized, remove the first line or sentence
    if "apologi" in response:
        if "\n" in response:
            response = " ".join(response.split("\n")[1:])
        else:
            response = " ".join(response.split(".")[1:])
    return response


if __name__ == '__main__':
    data = [{'actor': 'Sigourney Weaver', 'role': "Witch"}, {'actor': 'Holly Hunter', "role": "Assassin"}, {
        'actor': 'Dermot Mulroney'}, {'actor': 'William McNamara'}]
    print(generate_response([{'role': 'user', 'content': str(data)}]))