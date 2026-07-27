# Application Security - Day 2 Assignment

## SQL Injection and Input Validation (Python/Django)

### Project Overview

This project demonstrates how SQL Injection vulnerabilities occur in a Django application and how they can be prevented using secure coding practices.

The application manages a simple vehicle parts inventory and includes both an intentionally vulnerable search implementation and a secure implementation using the Django ORM.

---

## Features

- Vehicle Parts Inventory
- Search for vehicle parts
- Demonstration of a vulnerable SQL query
- SQL Injection attack demonstration
- Secure search using the Django ORM
- Frontend input validation
- Backend validation using Django Forms

---

## Technologies Used

- Python 3
- Django 6
- SQLite3
- HTML

---

## Demonstration

### Vulnerable Search

The application initially used a raw SQL query that directly concatenated user input into the SQL statement.

Example payload:

```text
' OR 1=1 --
```

The payload successfully bypassed the intended search condition and returned every record in the database, demonstrating a SQL Injection vulnerability.

---

### Secure Search

The vulnerable query was replaced with the Django ORM:

```python
Part.objects.filter(name__icontains=query)
```

The Django ORM safely handles user input by parameterizing database queries, preventing SQL Injection attacks.

---

## Input Validation

### Frontend Validation

The search form implements client-side validation using:

- `required`
- `maxlength`
- `pattern`

This improves the user experience by preventing invalid input before the form is submitted.

### Backend Validation

Server-side validation is implemented using Django Forms.

The application validates that:

- the search field is not empty;
- the input does not exceed 50 characters; and
- only letters, numbers, and spaces are accepted.

Invalid input is rejected before any database query is executed.

---

## Explanation

The original search functionality was vulnerable because it directly inserted user input into an SQL query, allowing SQL Injection attacks. By entering a payload such as `' OR 1=1 --`, an attacker could manipulate the SQL statement and retrieve all records from the database. The vulnerability was resolved by replacing the raw SQL query with the Django ORM, which safely parameterizes user input and prevents it from being interpreted as executable SQL. Frontend validation improves usability by preventing common input mistakes, but it can be bypassed, making backend validation essential for protecting the application.

---

## Author

Mercy Pimer
Refactory Academy – Application Security
