# Django REST Project Setup

This guide explains how to set up and run the Django REST project after cloning it.

---

## 1️⃣ Clone the repository

```bash
git clone https://github.com/Feras-Alaqad/training-tasks.git
```

---

## 2️⃣ Navigate to the project folder

```bash
cd training-tasks/<folder name that you want test>
```
example : cd training-tasks/week1
       or cd training-tasks/week2
---

## 3️⃣ Create a virtual environment

```bash
python -m venv venv
```

---

## 4️⃣ Activate the virtual environment

* **Windows:**

```bash
venv\Scripts\activate
```

* **Mac/Linux:**

```bash
source venv/bin/activate
```

> After activation, your terminal should show `(venv)` at the beginning.

---

## 5️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## 7️⃣ Start the development server

```bash
python manage.py runserver
```

The server will be available at:

```
http://127.0.0.1:8000/
```

---

## 8️⃣ Access the endpoints

* `/` → Home page (JSON: "Hello, World!" + personalized name)
* `/<name>/` → Home page with dynamic name in JSON

## 9️⃣ Notes

* Always activate the virtual environment before running the server.
* Any new packages should be added to `requirements.txt` using:
