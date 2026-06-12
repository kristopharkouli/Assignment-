products = {
    "Laptop": 15,
    "Mouse": 8,
    "Keyboard": 5,
    "Monitor": 12,
    "USB Drive": 3
}

print("Products with stock less than 10:\n")

for name, stock in products.items():
    if stock < 10:
        print(f"{name}: {stock}")
