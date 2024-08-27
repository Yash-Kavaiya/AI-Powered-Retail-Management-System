
# Classic Models Inc. Retail Management System

This project is a SQL-based application designed to manage the business operations of Classic Models Inc., a manufacturer of small-scale models of cars, motorcycles, planes, ships, and trains. The application uses a SQLite database to store information about customers, orders, payments, employees, offices, products, and product lines.

## Project Overview

Classic Models Inc. has a global presence with multiple offices, employees, and customers. This project aims to streamline the company's operations by providing a robust SQL database and a user-friendly Streamlit interface for querying and managing data. The system can handle various tasks such as adding customers, placing orders, recording payments, and managing employees.

## Database Schema

The database schema for Classic Models Inc. includes the following tables:

- **Payments**: Records payments made by customers, including check numbers, payment dates, amounts, and associated customer numbers.

- **Offices**: Stores information about the company's offices, including office codes, cities, phone numbers, addresses, and regions.

- **Customers**: Contains customer information such as customer numbers, names, contact details, addresses, sales representative numbers, credit limits, and locations.

- **Employees**: Maintains employee records, including employee numbers, names, contact details, job titles, and the office they are associated with.

- **Orders**: Tracks customer orders with details like order numbers, dates, shipping statuses, and associated customer numbers.

- **OrderDetails**: Provides details of each order, including order numbers, product codes, quantities ordered, prices, and line numbers.

- **Products**: Stores information about products, including product codes, names, scales, vendors, descriptions, quantities in stock, buy prices, and MSRP.

- **ProductLines**: Contains product line information such as product line identifiers and descriptions.

## ERD Diagram

The Entity-Relationship Diagram (ERD) shows the relationships between the tables in the database:

![ERD Diagram](ERD_Diagram.png)

## Setup and Installation

To run this project locally, follow these steps:

1. **Clone the Repository**: Clone the repository to your local machine using `git clone` or download the ZIP file.

2. **Install Required Libraries**: Install the necessary Python libraries using pip:
    ```bash
    pip install streamlit sqlalchemy langchain_community sqlite3
    ```

3. **Database Setup**: Ensure the `ClassicModels.db` SQLite database file is in the root directory of the project.

4. **Run the Application**: Start the Streamlit application by running:
    ```bash
    streamlit run app.py
    ```

## Usage

- **API Key**: You will need to enter your Groq API key in the sidebar to interact with the language model.

- **Query the Database**: Use the chat interface to interact with the database. You can ask questions or execute commands related to the data stored in the database, such as fetching customer details, placing new orders, or managing employee records.

- **Clear History**: Use the 'Clear message history' button to reset the conversation.

## Contributing

If you want to contribute to this project, please fork the repository and submit a pull request with your changes. Ensure that your code follows the project's coding standards and includes tests for new functionality.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

