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
>>> from api.models import Product
>>> Product.objects.all()
