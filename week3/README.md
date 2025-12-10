# 1️⃣ Navigate to the project folder
cd week3/product

# 2️⃣ create and Activate the virtual environment

## create virtual environment
python -m venv venv

## Activate virtual environment
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

# 3️⃣ Install dependencies (if requirements.txt exists)
pip install -r requirements.txt

# 4️⃣ Create migration files for the new models
python manage.py makemigrations

# 5️⃣ Apply migrations to create database tables
python manage.py migrate

# 6️⃣ Run the seeder to add dummy products
python manage.py seed_products

# 7️⃣ Verify the data (optional)
python manage.py shell
# Import the Product model and view all products
>>> from api.models import Product
>>> Product.objects.all()

# If you want to see only the name and price, you can loop through the results

>>> for product in Product.objects.all():
    print(f"Name: {product.name}, Price: {product.price}")

press ENTER

# Exit the shell:

>>> exit()

## ✅ CRUD Operations for Products

This section explains how to perform **Create, Read, Update, and Delete (CRUD)** operations on the Product model using Django REST Framework (DRF) with ViewSets.

---

### 1️⃣ Create a Product

**Endpoint:** `POST /api/products/`

**Example using curl:**

```bash
curl -X POST http://127.0.0.1:8000/api/products/ \
-H "Content-Type: application/json" \
-d '{"name": "Mouse", "price": 25.50}'

Response:

{
    "id": 6,
    "name": "Mouse",
    "price": "25.50",
    "created_at": "2025-12-10T12:00:00Z",
    "updated_at": "2025-12-10T12:00:00Z"
}

2️⃣ Read Products
List all products

Endpoint: GET /api/products/

curl -X GET http://127.0.0.1:8000/api/products/


Response:

[
    {"id": 1, "name": "Laptop", "price": "1500.00", ...},
    {"id": 2, "name": "Smartphone", "price": "800.00", ...},
    ...
]

Retrieve a single product

Endpoint: GET /api/products/<id>/

curl -X GET http://127.0.0.1:8000/api/products/1/


Response:

{"id": 1, "name": "Laptop", "price": "1500.00", ...}

3️⃣ Update a Product

Endpoint: PUT /api/products/<id>/ or PATCH /api/products/<id>/

Example (full update):

curl -X PUT http://127.0.0.1:8000/api/products/1/ \
-H "Content-Type: application/json" \
-d '{"name": "Laptop Pro", "price": 1800.00}'


Example (partial update):

curl -X PATCH http://127.0.0.1:8000/api/products/1/ \
-H "Content-Type: application/json" \
-d '{"price": 1750.00}'

4️⃣ Delete a Product

Endpoint: DELETE /api/products/<id>/

curl -X DELETE http://127.0.0.1:8000/api/products/6/


The product will be removed from the database.

5️⃣ Verify CRUD in Django Shell (Optional)
python manage.py shell

from api.models import Product

# List all products with name and price
for product in Product.objects.all():
    print(f"Name: {product.name}, Price: {product.price}")


Exit shell:

exit()


or

quit()


or press Ctrl + D


---

💡 **Notes:**

- All CRUD endpoints are automatically provided by **DRF ViewSet + Router**.  
- Seeder ensures 5 dummy products exist in the database before testing CRUD.  
- You can test these APIs with **Postman, curl, or any frontend**.

---
