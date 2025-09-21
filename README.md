# ToDoApp (Backend)

A backend API for a ToDo application built with **FastAPI**, **SQLAlchemy**, and **JWT authentication**.  
Supports user accounts, role-based access control (admin), CRUD operations for todos, and includes Alembic migrations and pytest testing.

---

## Features

- **Authentication**
  - JWT-based login and access control
  - Password hashing with bcrypt
- **User Operations**
  - View profile
  - Update password and phone number
- **Todos**
  - Create, read, update, delete todos
  - Filter todos by owner
- **Admin Operations**
  - View all todos
  - Delete any user’s todo
- **Database**
  - SQLAlchemy ORM with Alembic migrations
- **Testing**
  - Unit tests using `pytest`

---

## Tech Stack

- **Framework:** FastAPI  
- **Database:** PostgreSQL / SQLite  
- **ORM:** SQLAlchemy  
- **Authentication:** JWT (PyJWT / jose)  
- **Password Hashing:** Passlib (bcrypt)  
- **Migrations:** Alembic  
- **Testing:** pytest  

---