# 📝 Blog API

Live Demo: [https://blog-api-7byp.onrender.com](https://blog-api-7byp.onrender.com)

---

## 📌 Project Overview

This is a **Django REST Framework-based Blog API** that allows users to register, log in, create blog posts, view posts, and manage their own posts. Authentication is handled using **JWT tokens**, and posts are paginated for better performance.

There are two main apps in the project:
- `post`: Handles all blog-related operations like creating, viewing, updating, and deleting posts.
- `author`: Handles user registration, login, and logout functionality.

---

## 🔗 API Endpoint Descriptions

### 🔹 Post Endpoints

- `GET  http://127.0.0.1:8000/post/`  
  ➤ Returns a list of all blog posts (paginated).  
  ➤ Authenticated users can also create new posts using this endpoint (via POST method).

- `GET http://127.0.0.1:8000/post/id `  
  ➤ Returns the details of a specific post by its ID.  
  ➤ The post's owner can update or delete their own post using PUT or DELETE methods.

### 🔹 User Authentication Endpoints

- `POST http://127.0.0.1:8000/user/register/`  
  ➤ Allows a new user to register with username, email, and password.

- `POST http://127.0.0.1:8000/user/login/`  
  ➤ Authenticates the user and returns JWT access and refresh tokens.

- `POST http://127.0.0.1:8000/user/logout/`  
  ➤ Logs out the currently authenticated user (JWT blacklisting or session clearing depending on setup).

---

## 🛠 Project Setup Instructions

1. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   
2. **  Install PostgreSQL Adapter for Django **:
    ```bash
   pip install psycopg2-binary
