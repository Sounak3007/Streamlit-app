import os
import openai
import streamlit as st
from streamlit_chat import message

from neo4j_driver import run_query
from english2cypher import generate_cypher
from graph2text import generate_response

USER_ID = "DataDynamo"

# On the first execution, we have to create a user node in the database.
run_query("""
MERGE (u:User {id: $userId})
""", {'userId': USER_ID})

st.set_page_config(layout="wide")

#with header:
header = st.header('Data Dynamo')
st.title("Natural language querying interface")

def generate_context(prompt, context_data='generated'):
    context = []
    # If any history exists
    if st.session_state['generated']:
        # Add the last n exchanges
        size = len(st.session_state['generated'])
        for i in range(max(size-2, 0), size):
            context.append(
                {'role': 'user', 'content': st.session_state['user_input'][i]})
            context.append(
                {'role': 'assistant', 'content': st.session_state[context_data][i]})
    # Add the latest user prompt
    context.append({'role': 'user', 'content': str(prompt)})
    print(context) ## Added to review context
    return context


# Generated natural language
if 'generated' not in st.session_state:
    st.session_state['generated'] = []
# Neo4j database results
if 'database_results' not in st.session_state:
    st.session_state['database_results'] = []
# User input
if 'user_input' not in st.session_state:
    st.session_state['user_input'] = []
# Generated Cypher statements
if 'cypher' not in st.session_state:
    st.session_state['cypher'] = []

def get_text():
    input_text = st.text_input(
        "Enter your question here", "", key="input")
    return input_text


# Define columns
col1, col2 = st.columns([3, 1])
# with col2:
#     another_placeholder = st.empty()
with col1:
    placeholder = st.empty()
# with col3:
#     placeholder_graph = st.empty()
user_input = get_text()


if user_input:
    cypher = generate_cypher(generate_context(user_input, 'database_results'))
    # If not a valid Cypher statement
    if not "MATCH" in cypher:
        print('No Cypher was returned')
        st.session_state.user_input.append(user_input)
        st.session_state.generated.append(
            cypher)
        st.session_state.cypher.append(
            "No Cypher statement was generated")
        st.session_state.database_results.append("")

    elif str.lower(user_input).find('summar')>-1 :
        # Query the database, user ID is hardcoded
        results = run_query(cypher, {'userId': USER_ID})
        # Harcode result limit to 50
        results = results
        # Graph2text
        answer = generate_response(generate_context(
            f"Question was {user_input} and response should summarize in a paragraph the output that is here: {str(results)}"))
        st.session_state.database_results.append(str(results))
        st.session_state.user_input.append(user_input)
        st.session_state.generated.append(answer),
        st.session_state.cypher.append(cypher)

    elif str.lower(user_input).find('categor')>-1 :
        # Query the database, user ID is hardcoded
        results = run_query(cypher, {'userId': USER_ID})
        # Harcode result limit to 50
        results = results[:50]
        # Graph2text

        answer = generate_response(generate_context(
            f"Question was {user_input} and the response should use information that is given here: {str(results)} and then categorize"))
        st.session_state.database_results.append(str(results))
        st.session_state.user_input.append(user_input)
        st.session_state.generated.append(answer),
        st.session_state.cypher.append(cypher)

    else:
        # Query the database, user ID is hardcoded
        results = run_query(cypher, {'userId': USER_ID})
        # Harcode result limit to 10
        results = results
        print('line126')
        # print(type(results))
        print(results)
        # Graph2text
        answer = generate_response(generate_context(
            f"Question was {user_input} and the response should include only information that is given here: {str(results)} or a summary of this if asked for"))
        st.session_state.database_results.append(str(results))
        st.session_state.user_input.append(user_input)
        st.session_state.generated.append(answer),
        st.session_state.cypher.append(cypher)
    print('session_state')
    print(st.session_state.generated)
# Message placeholder
with placeholder.container():
    if st.session_state['generated']:
        size = len(st.session_state['generated'])
        # Display only the last three exchanges
        for i in range(max(size-3, 0), size):
            message(st.session_state['user_input'][i],
                    is_user=True, key=str(i) + '_user')
            message(st.session_state["generated"][i], key=str(i))
            # fig, ax = plt.subplots()
            # ax.hist(results, bins=20)
            # st.pyplot(fig)
        # if size > 3:
        #     # for j in range(1, size-3):
        #     st.session_state = st.session_state[-3:]
# Generated Cypher statements
# with another_placeholder.container():
#     if st.session_state['cypher']:
#         st.text_area("Latest generated Cypher statement",
#                      st.session_state['cypher'][-1], height=240)

# Generated Cypher statements
# with placeholder_graph.container():
#     # if st.session_state['generated']:
#     #     size = len(st.session_state['generated'])+10
#     #     Display only the last three exchanges
#     #     for i in range(max(size-3, 0), size):
#     #         message(st.session_state['user_input'][i],
#     #                 is_user=True, key=str(i) + '_user')
#     #         message(st.session_state["generated"][i], key=str(i))
#     #     Data to plot
#     cypher = generate_cypher(generate_context(user_input, 'database_results'))
#     results = run_query(cypher, {'userId': USER_ID})
#     print(results)
#     arr = np.random.normal(1, 1, size=100)
#     fig, ax = plt.subplots()
#     ax.hist(results, bins=20)
#     st.pyplot(fig)
