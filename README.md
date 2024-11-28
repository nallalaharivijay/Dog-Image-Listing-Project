Dog Image Listing Project

Overview:
This Django project provides a web application for listing and displaying dog images. The project includes user authentication using JSON Web Tokens (JWT), a RESTful API for interacting with the dog image data, and Role-Based Access Control (RBAC) for managing user permissions.

Features:
User authentication using JSON Web Tokens (JWT)
RESTful API for listing, creating, reading, updating, and deleting dog images
User-friendly web interface for interacting with the dog image data
Role-Based Access Control (RBAC) for managing user permissions

RBAC Roles:
The following RBAC roles are defined in the project:
Admin: Has full access to all features and data in the application.
Moderator: Has access to manage dog images, but cannot access user management features.
User: Has access to view dog images, but cannot manage or upload images.

Requirements:
Python 3.8+,
Django 3.2+,
djangorestframework 3.12+,
djangorestframework-simplejwt 4.6+,

Where files located:
Open My_project > Account (Main APP) > {Models, Views, Forns, URLS.py, admin.py}
Open My_project > My_project > {settings.py, admin urls.py, wagi.py}
Open My_project > Static (For all CSS files)
Open My_project > Template (For all HTML files)
