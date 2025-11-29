products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Mouse",  "price": 25},
    {"name": "Keyboard", "price": 45}
]

for product in products:   # foreach-style loop
    print(f"Product: {product['name']} - Price: {product['price']} USD")
