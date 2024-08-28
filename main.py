import streamlit as st
from pathlib import Path
import os
import sqlite3
import google.generativeai as genai
from dotenv import load_dotenv, find_dotenv
from langchain_community.utilities.sql_database import SQLDatabase
from sqlalchemy import create_engine
from langchain_community.agent_toolkits.sql.base import create_sql_agent
from langchain.agents.agent_types import AgentType
from langchain_community.callbacks.streamlit import StreamlitCallbackHandler
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv(find_dotenv())
os.environ['LANGCHAIN_TRACING_V2'] = 'true'
os.environ['LANGCHAIN_ENDPOINT'] = 'https://api.smith.langchain.com'
os.environ['LANGCHAIN_PROJECT'] = 'SQL-Toolkits'
os.environ['LANGCHAIN_API_KEY'] = os.getenv("LANGCHAIN_API_KEY")

genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
# Initialize the Language Model
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

# Set up Streamlit page configuration
st.set_page_config(page_title="An AI-powered solution for retail management")
st.title("An AI-powered solution for retail management")

# Introduction to Classic Models Inc.
st.markdown("""
**Classic Models Inc.** is a manufacturer of small-scale models of cars, motorcycles, planes, ships, trains, and more. Their products are sold in toy and gift stores globally. The company has offices worldwide and employs dozens of people. Each customer of Classic Models Inc. is typically a toy or gift store with an assigned sales representative who manages their orders and accounts. 

The company handles multiple aspects of business operations such as managing customer details, processing orders, tracking payments, and maintaining employee records. 

This tool is designed to interact with Classic Models Inc.'s SQL database to facilitate smooth day-to-day operations and to assist in making informed decisions.
""")

# Set the SQLite database file path
dbfilepath = (Path(__file__).parent / "ClassicModels.db").absolute()


@st.cache_resource(ttl="2h")
def configure_db():
    """
    Configure connection to the SQLite database.
    This database simulates the management system for Classic Models Inc.,
    storing data about products, customers, orders, payments, and employees.
    """
    creator = lambda: sqlite3.connect(f"file:{dbfilepath}?mode=ro", uri=True)
    return SQLDatabase(create_engine("sqlite:///", creator=creator))

# Configure SQLite database connection
db = configure_db()

# Define the toolkit for SQL database interaction
toolkit = SQLDatabaseToolkit(db=db, llm=llm)

# Create the SQL agent to handle queries
agent = create_sql_agent(
    llm=llm,
    toolkit=toolkit,
    verbose=True,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION
)

# Initialize or clear chat message history
if "messages" not in st.session_state or st.sidebar.button("Clear message history"):
    st.session_state["messages"] = [{"role": "assistant", "content": "Welcome to Classic Models Inc. database assistant! How can I help you manage your business today?"}]

# Display existing chat messages
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# User input for new queries
user_query = st.chat_input(placeholder="Ask anything related to Classic Models Inc. database")

if user_query:
    st.session_state.messages.append({"role": "user", "content": user_query})
    st.chat_message("user").write(user_query)

    # Use Streamlit callback handler for displaying response
    with st.chat_message("assistant"):
        streamlit_callback = StreamlitCallbackHandler(st.container())
        response = agent.run(user_query, callbacks=[streamlit_callback])
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.write(response)
