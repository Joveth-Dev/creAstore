# CREÁSTORE

A Simple API that allows user to create and manage their own stores.

## Features

- User registration, authorization, and store management APIs
- **API Documentation** accessible at `localhost/doc/` and `localhost/redoc/` (make sure system is running).
- **Automated Tests**  for models, authentication, authorization, and endpoints.

## Requirements
- Python 3.12.x
- Django 5.0

## Tech Stack Used
- Programming Language and Framework: **Python** with **Django**
- Database: **SQLite**
- API Toolkit: **Django REST Framework**

## Installation

**The project is Dockerized.** To get up and running quickly, run it using Docker, make sure you have Docker installed first and then run:

    docker compose up --build


**Installation for Development**
- Before you begin, make sure you have **Python** and **pip** installed on your system. This project also uses **pipenv** for virtual environment management.


**Install using `pip`**

    pip install pipenv


**Clone the repository with**

    git clone https://github.com/Joveth-Dev/creAstore.git


**Set up Virtual Environment and Install Dependencies**

    pipenv install


**Activate Virtual Environment**

    pipenv shell


**Apply Migrations**

    python manage.py migrate


**Create Admin Superuser (optional)**

    python manage.py createsuperuser
    
  - Follow the prompts to create a superuser account, which will be used to access the Django admin interface.
  

**Run the Development Server**

    python manage.py runserver

  - Visit `http://localhost:8000/auth/users/`. Start creating a user and explore!

