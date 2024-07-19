# Blog Platform

## Overview

The Blog Platform is a web application that allows users to create, read, update, and delete blog posts. Users can also comment on posts, and an administrator can manage users and view user data. The application is built using HTML, CSS, Bootstrap, Python, Flask, and MySQL.

## Features

- **User Management:**
  - Registration and login
  - User profile management
  - Password hashing and authentication

- **Blog Posts:**
  - Create, edit, and delete posts
  - View posts with comments

- **Comments:**
  - Add and view comments on posts

- **Admin Dashboard:**
  - Manage users
  - View user data

## Technology Stack

- **Frontend:**
  - HTML
  - CSS
  - Bootstrap

- **Backend:**
  - Python
  - Flask
  - MySQL

## Installation and Setup

### Prerequisites

- Python 3.x
- MySQL Server
- pip (Python package installer)


### Create and Activate a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Database

1. **Edit the Database Configuration:**
   Open `config.py` and configure the database URI:

   ```python
   SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://username:password@localhost/blog_db'
   SQLALCHEMY_TRACK_MODIFICATIONS = False
   ```

2. **Create the Database:**

   ```bash
   mysql -u username -p
   CREATE DATABASE blog_db;
   ```

### Initialize the Database

Run the following commands to set up the database:

```bash
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
```

### Run the Application

```bash
python run.py
```

Open a web browser and go to `http://localhost:5000` to access the application.

## Usage

- **Homepage:** View a list of all blog posts.
- **Login/Logout:** Access protected areas and manage your session.
- **Register:** Create a new user account.
- **Create Post:** Add new blog posts.
- **View Post:** Read individual blog posts and comments.
- **Edit Post:** Modify existing posts.
- **Admin Dashboard:** View and manage user accounts.

## Project Structure

- **`app/`**: Contains the application code.
  - **`__init__.py`**: Initializes the Flask app and sets up the database.
  - **`routes.py`**: Defines routes and request handling.
  - **`models.py`**: Defines the database models.
  - **`forms.py`**: Contains form definitions.
  - **`static/`**: Static files (CSS, JavaScript).
  - **`templates/`**: HTML templates.
- **`migrations/`**: Database migrations.
- **`venv/`**: Virtual environment.
- **`config.py`**: Configuration settings.
- **`run.py`**: Entry point to run the application.
- **`requirements.txt`**: Project dependencies.

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Create a new Pull Request

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Flask and SQLAlchemy for providing the backend framework and ORM.
- Bootstrap for the responsive design.
- MySQL for the database management system.

---

For more information, please refer to the documentation or contact the project maintainer.
```
