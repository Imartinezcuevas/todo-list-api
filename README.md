# To-Do List API

This project implements a RESTful API for managing a to-do list, focusing on user authentication, robust error handling, and secure data management. This project is inspired by the To-Do List API project on Roadmap.sh (https://roadmap.sh/projects/todo-list-api).

<img src="images/todo-list-api-bsrdd.png" alt="Todo list API" width="900" height="400">

## Project Goals

This project provides hands-on experience with:

* **User Authentication:** Implementing secure user registration and login using JWT (or a similar token-based approach).
* **Schema Design & Databases:** Designing an efficient database schema for users and to-do items, and interacting with the database (e.g., PostgreSQL, MySQL, MongoDB).
* **RESTful API Design:** Building a clean and well-structured RESTful API following best practices.
* **CRUD Operations:** Implementing Create, Read, Update, and Delete operations for to-do items.
* **Error Handling:** Implementing comprehensive error handling to provide informative responses to clients.
* **Security:** Implementing security measures to protect against common web vulnerabilities.
* **Data Validation:**  Validating user input to ensure data integrity.
* **Pagination and Filtering:** Implementing pagination and filtering for efficient retrieval of to-do items.

## Technologies Used
    * FastAPI to build fast, efficient and secure APIs.
    * PostgreSQL
    * JWT (JSON Web Tokens) for authentication
    * bcrypt for password hashing

## API Endpoints

### User Authentication

*  **Register a new user.**
    ```json
    POST /register
    {
      "name": "John Doe",
      "email": "john@doe.com",
      "password": "password"
    }
    ```
    Validate the given details, make sure the email is unique and store the user details in the database. Response with a token that can be used for authentication if the registration is successful.:
    ```json
    {
      "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9" // JWT token
    }
    ```
* **Authenticate a user.**
    ```json
    POST /login
    {
      "email": "john@doe.com",
      "password": "password"
    }
    ```
    Response:
    ```json
    {
      "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9" // JWT token
    }
    ```

### To-Do Items

* **Create a new to-do item**  (requires authentication via `Authorization` header with the token).
    ```json
    POST /todos
    {
      "title": "Buy groceries",
      "description": "Buy milk, eggs, and bread"
    }
    ```
    Response:
    ```json
    {
      "id": 1,
      "title": "Buy groceries",
      "description": "Buy milk, eggs, and bread"
    }
    ```
* **Get a list of to-do items** (requires authentication). Supports pagination.
    ```json
    GET /todos?page=1&limit=10
    {
      "data": [
        // ... to-do items
      ],
      "page": 1,
      "limit": 10,
      "total": 2
    }
    ```
* **Update a to-do item** (requires authentication and authorization - user must own the item).
    ```json
    PUT /todos/1
    {
      "title": "Buy groceries",
      "description": "Buy milk, eggs, bread, and cheese"
    }
    ```
    Response:
    ```json
    {
      "id": 1,
      "title": "Buy groceries",
      "description": "Buy milk, eggs, bread, and cheese"
    }
    ```
* **Delete a to-do item** (requires authentication and authorization).  Response: 204 No Content.
    ```json
    DELETE /todos/1
    ```
    Response:
    ```json`
    Status code 204
    ```

## Error Handling

The API implements robust error handling and returns appropriate HTTP status codes and error messages for various scenarios, including:

* **400 Bad Request:** Invalid input data.
* **401 Unauthorized:** Missing or invalid authentication token.
* **403 Forbidden:** User does not have permission to access the resource.
* **404 Not Found:** Resource not found.
* **500 Internal Server Error:** Server error.

## Bonus Features (If implemented)

* **Filtering and Sorting:**  Implement filtering and sorting options for to-do items.
* **Unit Tests:**  Include unit tests for API endpoints.
* **Rate Limiting/Throttling:**  Implement rate limiting to prevent abuse.
* **Refresh Token Mechanism:** Implement a refresh token mechanism for improved security.

## Setup and Installation

[instructions on how to set up and run the project locally.  Include steps for installing dependencies, configuring the database, and running the server.]

## How to Run

[instructions on how to run the API.]

## Testing

[how to run the unit tests.]

## Future Improvements

[potential future improvements for the project.]