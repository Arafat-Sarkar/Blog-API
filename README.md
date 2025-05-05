# 📝 Blog API

Live Demo: [https://blog-api-7byp.onrender.com](https://blog-api-7byp.onrender.com)

---

## 📌 Project Overview

This is a **Django REST Framework-based Blog API** that allows users to register, log in, create blog posts, view posts, and manage their own posts. Authentication is handled using **JWT tokens**, and posts are paginated for better performance.

There are two main apps in the project:
- `post`: Handles all blog-related operations like creating, viewing, updating, and deleting posts.
- `author`: Handles user registration, login, and logout functionality.

---

## 🛠 Project Setup Instructions

1. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
