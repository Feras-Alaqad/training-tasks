# 1️⃣ Navigate to the project folder
```bash
cd week6/
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

This section explains how to **create** Category, Supplier, Product, and Product–Supplier relationships using Django REST Framework (DRF) with ViewSets.

---

0️⃣ Run the Development Server

Before testing the CRUD operations, you need to start the Django development server:
```bash
python manage.py runserver
```

## Base URL Category
 
```
/api/categories/
```

---

## 1️⃣ Create Category (POST)

### Endpoint

```
POST /api/categories/

```

### Request Body (Valid)

```json
{
  "name": "Electronics"
}

```

### Success Response (201 Created)

```json
{
  "id": 1,
  "name": "Electronics"
}

```
## 2️⃣ Create Supplier (POST)

```
POST /api/suppliers/

```
### Request Body (Valid)

```json
{
  "name": "Tech Supplier",
  "email": "tech@supplier.com"
}

```

### Success Response (201 Created)

```json
{
  "id": 1,
  "name": "Tech Supplier",
  "email": "tech@supplier.com"
}
```
## 3️⃣ Create Product (POST)

```
POST /api/products/
```

### Request Body (Valid)

```json
{
  "name": "Laptop",
  "price": 1200.00,
  "category_id": 1
}

```

### Success Response (201 Created)

```json
{
  "id": 1,
  "name": "Laptop",
  "price": "1200.00",
  "category_id": 1
}
```

## 4️⃣ Create Product–Supplier Relationship (POST)

```
POST /api/product-suppliers/
```

### Request Body (Valid)

```json
{
  "product_id": 1,
  "supplier_id": 1,
  "cost_price": "950.00",
  "lead_time_days": 5
}

```

### Success Response (201 Created)

```json
{
  "id": 1,
  "product_id": 1,
  "supplier_id": 1,
  "cost_price": "950.00",
  "lead_time_days": 5
}

```
---

## 5️⃣ Notes

* Database integrity is enforced using:

  * `unique=True` for category and supplier names
  * `unique_together` for Product–Supplier relationships
* ViewSets with Routers are used for cleaner routing
* Validation prevents duplicate Product–Supplier relationships
* Standard DRF error response format is applied

---

## ✅ Result

* Correct creation order enforced (Category → Supplier → Product → Product–Supplier)

* One-to-Many relationship (Category → Products)

* Many-to-Many relationship with extra fields (Product ↔ Supplier)

* Scalable and maintainable API design


