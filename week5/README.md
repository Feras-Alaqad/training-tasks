# 1️⃣ Navigate to the project folder
```bash
cd week4/Category
```
# 2️⃣ create and Activate the virtual environment

## create virtual environment
```bash
python -m venv venv
```
## Activate virtual environment
# Windows
```bash
venv\Scripts\activate
```
# Linux/Mac
```bash
source venv/bin/activate
```
# 3️⃣ Install dependencies (if requirements.txt exists)
```bash
pip install -r requirements.txt
```
# 4️⃣ Create migration files for the new models
```bash
python manage.py makemigrations
```
# 5️⃣ Apply migrations to create database tables
```bash
python manage.py migrate
```

This section explains how to perform **Create, Read, Update, and Delete (CRUD)** operations on the Product model using Django REST Framework (DRF) with ViewSets.

---

0️⃣ Run the Development Server

Before testing the CRUD operations, you need to start the Django development server:
```bash
python manage.py runserver
```

## Base URL products
 
```
/api/products/
```

---

## 1️⃣ Create Product (POST)

### Endpoint

```
POST /api/products/
```

### Request Body (Valid)

```json
{
  "name": "Laptop",
  "price": 1200.00
}
```

### Success Response (201 Created)

```json
{
  "id": 1,
  "name": "Laptop",
  "price": "1200.00"
}
```
## 2️⃣ Base URL categories

```
/api/categories/
```
### Success Response

```json
  {
        "id": 1,
        "name": "Electronics"
    },
    {
        "id": 2,
        "name": "Fashion"
    },
    {
        "id": 3,
        "name": "Home"
    },
    {
        "id": 4,
        "name": "Sports"
    },
    {
        "id": 5,
        "name": "Books"
    }
```
---

## 4️3️⃣ Notes

* Database integrity is enforced using:

  * `unique=True` for name
  * `DecimalField` for price
* Same serializer is used for **Create** and **Update**
* Error responses follow Django REST Framework standard format

---

## ✅ Result

* One-to-Many relationship implemented

* Strong validation rules

* Optimized database queries

* Clean and maintainable code

* Ready for production use

