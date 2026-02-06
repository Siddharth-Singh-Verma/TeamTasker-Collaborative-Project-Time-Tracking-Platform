# **TeamTasker — Collaborative Project & Time Tracking Platform**

## 🚀 Overview

**TeamTasker** is a Django-based collaborative project management and time-tracking platform designed for teams that need clear ownership, accountability, and visibility of work. It provides role-based access, structured task allocation, real-time activity tracking, and a checklist-driven workflow to ensure efficient execution.

This is not a simple to-do app — it is built for real teams working on real projects with multiple users, multiple roles, and multiple parallel tasks.

---

## 🎯 Key Features

### 🔐 Authentication & Authorization

* Secure user authentication using Django’s built-in auth system
* Role-based access control with different permission levels:

  * **Admin / Project Owner (High-level user)**
  * **Manager**
  * **Team Member**

### 📁 Project Management

* Users can own **multiple projects**
* Each project can have **multiple collaborators**
* Clear separation of data based on user roles
* Project-wise activity tracking

### ✅ Task Allocation System

* High-level users can:

  * Create tasks
  * Assign tasks to specific members
  * Set priorities and deadlines
* Members can:

  * View assigned tasks
  * Update progress
  * Mark tasks as completed

### 📋 Checklist System

* Every task can have:

  * Sub-tasks / checklist items
  * Step-by-step completion tracking
  * Visual progress indicators

### ⏱️ Activity Tracking

* Logs of:

  * Last activities performed in a project
  * Task updates
  * User contributions
* Helps maintain transparency and accountability

### 🎨 Frontend

* Built using:

  * Django Templates
  * Tailwind CSS for modern UI
* Clean, minimal, and responsive design

### 🛠 Backend

* Django-based architecture
* Models designed for:

  * Projects
  * Users
  * Tasks
  * Checklists
  * Activity Logs

---

## 🏗 Tech Stack

| Layer          | Technology                                            |
| -------------- | ----------------------------------------------------- |
| Backend        | Django                                                |
| Frontend       | Django Templates + Tailwind CSS                       |
| Database       | SQLite (default, can be switched to PostgreSQL/MySQL) |
| Authentication | Django Auth System                                    |

---

## 📂 Project Structure (High-Level)

```
TeamTasker/
│── manage.py
│── db.sqlite3
│── requirements.txt
│
├── core/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   └── static/
│
├── users/
│   ├── models.py
│   ├── views.py
│   └── auth.py
│
├── projects/
│   ├── models.py
│   ├── views.py
│   └── templates/
│
└── tasks/
    ├── models.py
    ├── views.py
    └── templates/
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/TeamTasker.git
cd TeamTasker
```

### 2️⃣ Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run migrations

```bash
python manage.py migrate
```

### 5️⃣ Create superuser

```bash
python manage.py createsuperuser
```

### 6️⃣ Run server

```bash
python manage.py runserver
```

Open: `http://127.0.0.1:8000/`

---

## 🎯 Use Cases

TeamTasker is ideal for:

* College project teams
* Startups
* Remote teams
* Freelancers managing multiple clients
* Hackathon teams
* Software development groups

---

## 🚧 Future Enhancements (Planned)

* Real-time notifications using WebSockets
* Time tracking per task
* Kanban board view
* File attachments per task
* Email notifications
* Analytics dashboard

---

## 🤝 Contributing

Pull requests are welcome. For major changes, open an issue first to discuss what you want to improve.

---

## 📜 License

MIT License

---

## 👨‍💻 Author

Siddharth

---

If you want, I can tailor this README for **GitHub (more professional), Resume, or Portfolio website**.
