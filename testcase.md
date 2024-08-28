

## TEST_CASES.md

### Test Case 1: Retrieve details of all the customers in the United States who have made payments between April 1st, 2003 and March 31st, 2004.

**Description:**

This test case verifies that the system correctly retrieves details of all customers from the United States who have made payments within the specified date range.

**Input:**

- **Country**: USA
- **Date Range**: April 1st, 2003 to March 31st, 2004

**Expected Output:**

A list of tuples containing customer details. Each tuple should include:
- `customerName`
- `contactLastName`
- `contactFirstName`
- `phone`
- `addressLine1`
- `addressLine2`
- `city`
- `state`
- `postalCode`
- `country`
- `creditLimit`

**Example Output:**

```plaintext
[('Daedalus, Inc.', 'Smith', 'John', '1-206-555-9482', '4755 21st Ave. E.', None, 'Seattle', 'Washington', '98112', 'USA', 118),
 ('Dragon Souvenirs, Inc.', 'Natividad', 'Elizabeth', '1-212-555-4718', '251 B King Ave', None, 'New York', 'New York', '10024', 'USA', 137)]
```

### Test Case 2: Determine the total number of units sold for each product.

**Description:**

This test case verifies that the system accurately calculates the total number of units sold for each product.

**Input:**

No specific input is required as the calculation is based on the existing data in the `OrderDetails` table.

**Expected Output:**

A list of dictionaries, each containing:
- `productCode`
- `total_units_sold`

**Example Output:**

```plaintext
[
    {'productCode': 'S18_1099', 'total_units_sold': 246},
    {'productCode': 'S18_2248', 'total_units_sold': 265},
    {'productCode': 'S18_1342', 'total_units_sold': 184},
    {'productCode': 'S18_4409', 'total_units_sold': 213},
    {'productCode': 'S18_2795', 'total_units_sold': 179},
    {'productCode': 'S18_1123', 'total_units_sold': 199},
    {'productCode': 'S18_1380', 'total_units_sold': 243},
    {'productCode': 'S18_1662', 'total_units_sold': 280},
    {'productCode': 'S18_4522', 'total_units_sold': 227},
    {'productCode': 'S18_2949', 'total_units_sold': 259}
]
```

### Test Case 3: Compute the quartile and percentile for each payment made by a customer.

**Description:**

This test case checks that the system computes the correct quartile and percentile rank for each payment made by a customer.

**Input:**

No specific input is required as the calculation is based on the existing data in the `Payments` table.

**Expected Output:**

A list of dictionaries, each containing:
- `checkNumber`
- `paymentDate`
- `amount`
- `customerNumber`
- `quartile`
- `percentRank`

**Example Output:**

```plaintext
[
    {'checkNumber': None, 'paymentDate': '2003-01-16', 'amount': 6500.00, 'customerNumber': 103, 'quartile': 1, 'percentRank': 1},
    {'checkNumber': None, 'paymentDate': '2003-02-16', 'amount': 5000.00, 'customerNumber': 103, 'quartile': 1, 'percentRank': 2},
    {'checkNumber': None, 'paymentDate': '2003-03-16', 'amount': 5000.00, 'customerNumber': 103, 'quartile': 1, 'percentRank': 3},
    {'checkNumber': None, 'paymentDate': '2003-04-16', 'amount': 8500.00, 'customerNumber': 103, 'quartile': 2, 'percentRank': 4},
    {'checkNumber': None, 'paymentDate': '2003-05-16', 'amount': 9500.00, 'customerNumber': 103, 'quartile': 2, 'percentRank': 5},
    {'checkNumber': None, 'paymentDate': '2003-06-16', 'amount': 10000.00, 'customerNumber': 103, 'quartile': 3, 'percentRank': 6},
    {'checkNumber': None, 'paymentDate': '2003-07-16', 'amount': 11000.00, 'customerNumber': 103, 'quartile': 3, 'percentRank': 7},
    {'checkNumber': None, 'paymentDate': '2003-08-16', 'amount': 12000.00, 'customerNumber': 103, 'quartile': 3, 'percentRank': 8},
    {'checkNumber': None, 'paymentDate': '2003-09-16', 'amount': 13000.00, 'customerNumber': 103, 'quartile': 4, 'percentRank': 9},
    {'checkNumber': None, 'paymentDate': '2003-10-16', 'amount': 14000.00, 'customerNumber': 103, 'quartile': 4, 'percentRank': 10}
]
```

### Test Case 4: List order of each customer sorted by order amount (highest to lowest) and display the difference in amount between each order and the next highest order by the same customer.

**Description:**

This test case checks that the system lists all orders made by each customer, sorted by order amount in descending order. Additionally, it verifies that the system correctly calculates the difference in amount between each order and the next highest order by the same customer.

**Input:**

No specific input is required as the calculation is based on the existing data in the `Orders` and `OrderDetails` tables.

**Expected Output:**

A list of dictionaries, each containing:
- `customerNumber`
- `orderNumber`
- `amount`
- `difference_to_next`

**Example Output:**

```plaintext
[
    {'customerNumber': 103, 'orderNumber': 10101, 'amount': 15000.00, 'difference_to_next': 5000.00},
    {'customerNumber': 103, 'orderNumber': 10102, 'amount': 10000.00, 'difference_to_next': 2000.00},
    {'customerNumber': 103, 'orderNumber': 10103, 'amount': 8000.00, 'difference_to_next': 0.00}
]
```
