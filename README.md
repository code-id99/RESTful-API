Flask User API

This is a simple RESTful API built using Flask, a lightweight web framework in Python. 
The API provides two endpoints to interact with user data: one for retrieving user information and another for creating new users.

Features:
GET /get-user/<user_id>: Retrieves user data based on the user_id provided in the URL. Optionally, you can add an extra query parameter to include additional data in the response.
POST /create-user: Allows creating a new user by sending a JSON payload with user details.
Requirements
Python 3.x
Flask: Install Flask using pip
