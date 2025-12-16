# 1️⃣ Navigate to the project folder
```bash
cd week4/validations
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

## Base URL

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

---

### ❌ Validation Cases (Create)

#### 1. Name is empty

**Request**

```json
{
  "name": "",
  "price": 500
}
```

**Response (400 Bad Request)**

```json
{
  "name": ["This field may not be blank."]
}
```

---

#### 2. Duplicate product name

**Request**

```json
{
  "name": "Laptop",
  "price": 800
}
```

**Response (400 Bad Request)**

```json
{
  "name": ["Product name must be unique."]
}
```

---

#### 3. Price is zero or negative

**Request**

```json
{
  "name": "Mouse",
  "price": 0
}
```

**Response (400 Bad Request)**

```json
{
  "price": ["Price must be greater than 0."]
}
```

---

## 2️⃣ Update Product (PUT)

### Endpoint

```
PUT /api/products/{id}/
```

### Request Body (Valid – same name)

```json
{
  "name": "Laptop",
  "price": 1500
}
```

### Success Response (200 OK)

```json
{
  "id": 1,
  "name": "Laptop",
  "price": "1500.00"
}
```

---

### ❌ Validation Cases (Update)

#### 4. Update without changing name (Allowed)

* The name not change
* There is no repeat

✔ **Request passes successfully**

---

#### 5. Update with duplicate name

**Request**

```json
{
  "name": "Phone",
  "price": 1000
}
```

**Response (400 Bad Request)**

```json
{
  "name": ["Product name must be unique."]
}
```

---

#### 6. Update with invalid price

**Request**

```json
{
  "name": "Tablet",
  "price": -50
}
```

**Response (400 Bad Request)**

```json
{
  "price": ["Price must be greater than 0."]
}
```

---

## 3️⃣ Validation Rules Summary

| Field | Rule                   |
| ----- | ---------------------- |
| name  | Required, Unique       |
| price | Required, Decimal, > 0 |

---

## 4️⃣ Notes

* Validation logic is handled inside **Serializer** (Clean Code)
* Database integrity is enforced using:

  * `unique=True` for name
  * `DecimalField` for price
* Same serializer is used for **Create** and **Update**
* Error responses follow Django REST Framework standard format

---

## ✅ Result

* Invalid data is rejected
* Clear validation messages are returned
* API is production-ready and predictable

