# 📦 Inventory Management API

A Django REST Framework API for managing Products, Categories, Suppliers, and Product-Supplier relationships with authentication and soft delete system.

---

# 🚀 Base URL
[text](http://127.0.0.1:8000/api/)


---

# 🔐 Authentication

## 1. Signup
POST api/signup/


### Request
```json
{
  "username": "john",
  "email": "john@mail.com",
  "password": "123456",
  "password2": "123456"
}
```
### Response
```json
{
  "message": "User created successfully"
}
```
## 2. Login (JWT Token)
POST api/token/

### Request
```json
{
  "username": "john",
  "password": "123456"
}
```
### Response
```json
{
  "refresh": "token_here",
  "access": "token_here"
}
```

## 3. Refresh Token
POST api/token/refresh/

### Request
```json
{
  "refresh": "token_here"
}
```
### Response
```json
{
  "access": "token_here"
}
```
## Suppliers API
# Create Supplier
POST api/suppliers/

### Request
```json
{
  "name": "Supplier A",
  "email": "supplier@mail.com"
}
```

# List Suppliers
GET api/suppliers/

# Update Supplier 
PUT api/suppliers/{id}/
### Request
```json
{
  "name": "Tech Supplier",
  "email": "supplier@mail.com"
}
```
# Delete Supplier
DELETE api/suppliers/{id}/

## Categories API
# Create Category
POST api/categories/
```json
{
  "name": "Electronics"
}
```
# List Categories
GET api/categories/

# Update Category
PUT api/categories/{id}/
```json
{
  "name": "Elect"
}
```
# Delete Category
DELETE api/categories/{id}/

## Products API
POST api/products/
```json
{
  "name": "lap",
  "price": "5760.00",
  "category_id": 1
}
```

# List Products
GET api/products/

# Delete Product (Soft Delete)
DELETE api/products/{id}/

# Trash (Soft Deleted Products)
GET api/products/trash/

# Restore Product
POST api/products/{id}/restore/

# Force Delete Product
DELETE api/products/{id}/force_delete/

# Update Product Image
PATCH api/products/{id}/update-image/

# Search / Filter / Order Product
GET api/products/?search=lap
GET api/products/?category_id=1
GET api/products/?supplier_id=2
GET api/products/?price=100
GET api/products/?price__gte=100&price__lte=500
GET api/products/?ordering=price
GET api/products/?ordering=-created_at

### Product Suppliers API
POST api/product-suppliers/
```json
{
  "product_id": 1,
  "supplier_id": 2,
  "cost_price": 50,
  "lead_time_days": 5
}
```

# Dashboard
GET api/dashboard/
```json
{
    "success": true,
    "data": {
        "total_products": 4,
        "total_categories": 1,
        "total_suppliers": 1,
        "latest_products": [
            {
                "id": 14,
                "name": "taps",
                "price": "5760.00",
                "category_id": 1,
                "image": "/media/products/IMG_20260306_175050_AgmAao6.png",
                "image_url": "/media/products/IMG_20260306_175050_AgmAao6.png",
                "deleted_at": "2026-04-10T13:00:22.891839Z",
                "created_at": "2026-04-10T12:25:53.837691Z"
            },
            {
                "id": 13,
                "name": "tap",
                "price": "560.00",
                "category_id": 1,
                "image": "/media/products/download.png",
                "image_url": "/media/products/download.png",
                "deleted_at": null,
                "created_at": "2026-04-10T11:52:35.822415Z"
            },
            {
                "id": 11,
                "name": "tap",
                "price": "560.00",
                "category_id": 1,
                "image": null,
                "image_url": null,
                "deleted_at": null,
                "created_at": "2026-04-10T11:41:37.790950Z"
            },
            {
                "id": 10,
                "name": "jawal",
                "price": "2200.00",
                "category_id": 1,
                "image": "/media/products/image-20220601-202452.png",
                "image_url": "/media/products/image-20220601-202452.png",
                "deleted_at": null,
                "created_at": "2026-04-10T08:43:02.239404Z"
            }
        ]
    }
}
```
---
 Notes
- All endpoints require authentication (Bearer Token)
- Products use Soft Delete (deleted_at)
- Images must be:
- JPG / PNG / WEBP
- Max size: 2MB
- Use multipart/form-data for image upload

---