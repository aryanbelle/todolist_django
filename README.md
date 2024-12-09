# Todo Application

A simple todo list application built using Django. This app allows users to add, view, and manage tasks efficiently.

## Features

- Add new tasks with a title and description.
- View all tasks in a list format.
- Edit and delete tasks.
- User-friendly UI for easy task management.

---

## Prerequisites

Before you can set up and run this project, ensure you have the following installed on your system:

- Python 3.8 or later
- pip (Python package manager)
- SQLite (or any other database supported by Django)

---

## Setup and Installation

Follow these steps to set up the project:

### 1. Clone the Repository

```bash
git clone https://github.com/aryanbelle/todolist_django
cd todolist_django
```

### 2. Create and Activate a Virtual Environment

#### On Linux/Mac:
```bash
python3 -m venv env
source env/bin/activate
```

#### On Windows:
```bash
python -m venv env
env\Scripts\activate
```

### 3. Install Dependencies

Install the required Python packages listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

Run the following commands to create the database tables:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Run the Development Server

Start the server with:

```bash
python manage.py runserver
```

The application will be accessible at:  
[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## Usage

1. Open the application in your web browser.
2. Use the "Add Task" button to create new tasks.
3. View and manage your tasks in the task list.
4. Edit or delete tasks as needed.

---

## Deployment

To deploy the app to a live server, follow the steps outlined [here](https://docs.djangoproject.com/en/stable/howto/deployment/).

---

## Author

**Aryan Belle**  
GitHub: [aryanbelle](https://github.com/aryanbelle)

---
