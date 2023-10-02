# Python_machine_test_API
This API project is designed to simplify user registration, login, client management, and project assignment processes for your application. It provides a set of endpoints to interact with user accounts, clients, and projects efficiently.

# Key Features
- Ragister and Login a User
- Register a client
- Fetch clients info
- Edit/Delete client info
- Add new projects for a client and assign users to those projects
- Retrieve assigned projects to logged-in users

## User Registration and Login
- Register a User: Allow new users to create an account by providing their information, including username, email, and password.
- Login: Enable registered users to log in securely using their credentials.

## Client Management
- Register a Client: Allow authorized users to register clients by providing client details like name, contact information, and additional notes.
- Fetch Client Info: Retrieve detailed information about registered clients.
- Edit Client Info: Permit authorized users to update client details, ensuring that client information remains accurate and up-to-date.
- Delete Client: Provide the capability to delete client records when necessary.

## Project Management
- Add New Projects: Allow authorized users to create new projects and associate them with specific clients.
- Assign Users to Projects: Enable the assignment of users to projects, ensuring that project teams are properly configured.
- Retrieve Assigned Projects: Allow logged-in users to view a list of projects they are assigned to, along with project details.

# Technologies Used
Django: A high-level Python web framework that provides robust features for web application development.

Django rest_Framework: A powerful and flexible toolkit for building Web APIs in Django applications.

Database: SQLite.

