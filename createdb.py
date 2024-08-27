import requests

# URL of the SQL file
url = "https://raw.githubusercontent.com/harsha547/ClassicModels-Database-Queries/master/database.sql"

# Download the file content
response = requests.get(url)
sql_file_content = response.text

# Print the first few lines of the file to verify
print(sql_file_content)  # Print first 1000 characters to verify content

import sqlite3
import re
import requests

# Function to extract relevant SQL commands
def extract_inserts(sql_content, table_name):
    """
    Extracts INSERT statements for a specific table from the SQL content.
    """
    pattern = rf"INSERT INTO `{table_name}` \(.*?\);"
    matches = re.findall(pattern, sql_content, re.DOTALL)
    return matches

# Connect to SQLite database (ensure this matches your database setup)
conn = sqlite3.connect('ClassicModels.db')
cursor = conn.cursor()

# Extract the 'INSERT INTO Customers' commands
customer_inserts = extract_inserts(sql_file_content, "customers")

# Modify SQL for SQLite Compatibility and Execute Commands
for insert_command in customer_inserts:
    # Modify SQL syntax for SQLite if necessary
    insert_command_sqlite = insert_command.replace('`', '')  # Remove backticks for SQLite

    # Execute the insert command
    cursor.execute(insert_command_sqlite)

# Commit changes and close the connection
conn.commit()
conn.close()

print("Customers added to the database successfully.")


import sqlite3

import requests
from langchain_community.utilities.sql_database import SQLDatabase
from sqlalchemy import create_engine
from sqlalchemy.pool import StaticPool


def get_engine_for_db():
    """Pull sql file, populate in-memory database, and create engine."""
    url = "https://raw.githubusercontent.com/harsha547/ClassicModels-Database-Queries/master/database.sql"
    response = requests.get(url)
    sql_script = response.text

    connection = sqlite3.connect(":memory:", check_same_thread=False)
    connection.executescript(sql_script)
    return create_engine(
        "sqlite://",
        creator=lambda: connection,
        poolclass=StaticPool,
        connect_args={"check_same_thread": False},
    )


engine = get_engine_fordb()

db = SQLDatabase(engine)