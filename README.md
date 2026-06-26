# TASKRANT 🎯
> Tactical Task Management — Valorant-themed Django Todo App

![alt text](<Screenshot 2026-06-25 182937.png>)
![alt text](<Screenshot 2026-06-25 182918.png>)
![alt text](<Screenshot 2026-06-25 182852.png>)


---

## What is TaskRant?

TaskRant is a full-stack todo web app built with Django, styled with a Valorant-inspired tactical UI. Create an account, deploy missions (tasks), track your completion rate, and climb the rank ladder from Iron Cadet to Radiant Operator.

---

## Features

- 🔐 User authentication — register, login, logout
- ✅ Create, complete, and delete tasks
- 📊 Live stats — total, active, completed, completion rate
- 🏆 Rank system based on completion percentage
- 💬 Random motivational quotes
- ⚡ Animated UI — glitch effect, scan line, particle canvas
- 📱 Responsive design

---

## Screenshots

> Add screenshots of your login, signup, and todo pages here.

---

## Tech Stack

| Layer     | Technology        |
|-----------|-------------------|
| Backend   | Django 6.0        |
| Database  | SQLite (default)  |
| Frontend  | HTML, CSS, JS     |
| Auth      | Django built-in   |
| Fonts     | Google Fonts (Rajdhani, Inter) |

---

## Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/YOUR_USERNAME/taskrant.git
cd taskrant
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate       # Mac/Linux
venv\Scripts\activate          # Windows
```

### 3. Install dependencies

```bash
pip install django
```

### 4. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Start the server

```bash
python manage.py runserver
```

Then open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

---

## Project Structure

```
taskrant/
├── todo/
│   ├── templates/
│   │   ├── login.html
│   │   ├── sign.html
│   │   └── todo.html
│   ├── models.py       # TODO model
│   ├── views.py        # Login, signup, todo, toggle, delete, logout
│   ├── urls.py         # URL routing
│   ├── admin.py
│   └── settings.py
├── db.sqlite3
└── manage.py
```

---

## URL Routes

| URL | View | Description |
|-----|------|-------------|
| `/` | `login_page` | Login page |
| `/signup/` | `signup_page` | Register new user |
| `/todo/` | `todo_page` | Main task dashboard |
| `/toggle/<id>/` | `toggle_todo` | Mark task complete/active |
| `/delete/<id>/` | `delete_todo` | Delete a task |
| `/logout/` | `logout_page` | Logout |

---

## Rank System

Your rank is based on task completion rate:

| Completion | Rank |
|------------|------|
| 80%+ | ⚡ Radiant Operator |
| 60%+ | 💎 Diamond Agent |
| 40%+ | 🔷 Platinum Recruit |
| 20%+ | 🥈 Silver Trainee |
| 0%+  | 🛡 Iron Cadet |

---

## Notes

- This project uses Django's built-in SQLite — no extra database setup needed
- `SECRET_KEY` in `settings.py` should be changed before deploying to production
- `DEBUG = True` should be set to `False` in production

---

## Author

Built by **Mahesh Shinde** — inspired by Valorant's tactical aesthetic.

---

## License

MIT License — free to use and modify.
