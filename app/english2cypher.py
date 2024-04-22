import os
from retry import retry
from neo4j_driver import get_schema
from training import examples
from openai import OpenAI

api_key = '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'
client = OpenAI(api_key=api_key)

schema = get_schema()

system = f"""
You are an assistant with an ability to generate Cypher queries for neo4j graph database based off example Cypher queries and your own knowledge of syntax.
The data is from India's National Tuberculosis Management system called Ni-kshay or Nikshay.
Below is the information about the neo4j graph database that will be queried:
Schema: {schema}

The Label Episode is pertaining to Patients and the Label Comment is pertaining to comments from these Patients.
In this context 'Stage' refers to the property 'stage' in Episode Nodes and has values such as 'PRESUMPTIVE_OPEN', 'PRESUMPTIVE_CLOSED', 'DIAGNOSED_ON_TREATMENT', 'DIAGNOSED_NOT_ON_TREATMENT', 'DIAGNOSED_NOT_ON_TREATMENT_CLOSED', 'DIAGNOSED_OUTCOME_ASSIGNED'
A diagnosed patient will have the following values for 'Stage' - DIAGNOSED_ON_TREATMENT, DIAGNOSED_NOT_ON_TREATMENT, DIAGNOSED_NOT_ON_TREATMENT_CLOSED, DIAGNOSED_OUTCOME_ASSIGNED
'type of case' refers to the property 'type_of_case' in Episode Nodes and has values 'NEW','RETREATMENT', 'PMDT', 'TPT (TB Preventive Treatment)'.
The terms 'Drug resitant tb' or 'DRTB' are equivalent to patients having property 'type_of_case' as PMDT.

Given below are the additional graph properties: property name, and list of their synonyms that can be used in a question
notification_date, [diagnosis date, notification date, diagnosed in or after]
stage, [stage, treatment stage]

Example Cypher queries are: \n {examples} \n

Inform the user when you can't infer the cypher statement due to the lack of context of the conversation and state what is the missing context.
Parts of the prompt for categorization of comments or assigning severity by a provided logic should are to be ignored. Find the closest syntactically correct cypher query
"""


###Do not response with any explanation or any other information except the Cypher query.
##You do not ever apologize and strictly generate cypher statements based of the provided Cypher examples.
##Do not provide any Cypher statements that can't be inferred from Cypher examples.
##You need to update the database using an appropriate Cypher statement when a user mentions their likes or dislikes, or what they watched already.

@retry(tries=2, delay=5)
def generate_cypher(messages):
    messages = [
                   {"role": "system", "content": system}
               ] + messages
    print(messages)
    # Make a request to OpenAI
    completions = client.chat.completions.create(
        model="gpt-3.5-turbo-16k",
        messages=messages,
    )
    response = completions.choices[0].message.content

    # Sometime the models bypasses system prompt and returns
    # data based on previous dialogue history
    if not "MATCH" in response and "{" in response:
        raise Exception(
            "GPT bypassed system message and is returning response based on previous conversation history" + response)
    # If the model apologized, remove the first line
    if "apologi" in response:
        response = " ".join(response.split("\n")[1:])
    # Sometime the model adds quotes around Cypher when it wants to explain stuff
    if "`" in response:
        response = response.split("```")[1].strip("`")
    print(response)
    return response


if __name__ == '__main__':
    print(generate_cypher([{'role': 'user', 'content': 'Who are you?'},
                           {'role': 'assistant', 'content': 'I am Ni-kshay prism'},
                           {'role': 'user',
                            'content': 'What data can you access?'}
                           ]))