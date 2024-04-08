# AirBnB Clone - Web Framework

Welcome to the AirBnB clone project! This part focuses on creating a simple web framework using Flask, a lightweight WSGI web application framework in Python. By the end of this project, you'll understand how web frameworks work and how to build dynamic websites that interact with a database.

## Concepts

For a comprehensive understanding, ensure to review the concept page on the [AirBnB clone](https://intranet.hbtn.io/concepts/74).

## Learning Objectives

- Understanding of what a Web Framework is.
- How to build a web framework with Flask.
- Defining routes in Flask and the significance of a route.
- Managing variables in a route.
- Introduction to templates and how to create an HTML response in Flask using templates.
- Dynamically generating templates with loops and conditions.
- Displaying data from a MySQL database in HTML.

## Requirements

### Python Scripts

- Compatible with Ubuntu 20.04 LTS and Python 3.8.5.
- Follows PEP 8 style (version 2.7.*).
- All files must end with a new line.
- The first line of all your files should be exactly `#!/usr/bin/python3`.
- All your files must be executable.
- Your code should use the `pycodestyle`.
- You must use the Flask framework.

### HTML/CSS Files

- Code should be W3C compliant and validate with the W3C-Validator.
- All CSS files should be in the styles folder.
- All images should be in the images folder.
- No use of `!important` or ID selectors in CSS files.

### Installation

Install Flask using pip:

```bash
pip3 install Flask
```

## Tasks

### 0. Hello Flask!

A simple Flask application that responds to the root URL (`/`) with "Hello HBNB!".

### 1. HBNB

Expands the previous application with a new route `/hbnb` that displays "HBNB".

### 2. C is fun!

Introduces variable rules in routes with a route `/c/<text>` that displays "C ", followed by the text passed as a route variable.

### 3. Python is cool!

Similar to task 2 but for Python, and with a default text "is cool".

### 4. Is it a number?

Only displays the route if the variable passed as `n` is an integer: `/number/<n>`.

### 5. Number template

Displays a simple HTML page only if `n` is an integer, using Flask templates.

### 6. Odd or even?

Expands on task 5 by determining if `n` is odd or even and displaying it in the HTML.

### 7. Improve engines

Requires updates to both FileStorage and DBStorage engines to add a `close` method, and to the `State` model to handle a conditional relationship with `City` objects.

### 8. List of states

A route that displays a HTML page listing all states from the database.

### 9. Cities by states

A route that displays a HTML page listing all cities by states from the database.

### 10. States and State

A route that displays a HTML page with a list of all states or the cities of a specific state.

### 11. HBNB filters

A dynamic webpage that displays a list of states, cities, and amenities to filter places in the database.

## Conclusion

This project demonstrates the basic concepts of building a dynamic web application using the Flask framework and integrating with a database using SQLAlchemy ORM. Through building routes, handling database sessions, and rendering templates, you'll gain foundational knowledge in web development with Flask.

For more details, refer to the task files and templates included in the project repository.