# Inventory Management System 
def add_product(products, name, price, stock, category):
    if name in products:
        print(f"Error: Product '{name}' already exists.")
        return  

    products[name] = {
        'price': price,
        'stock': stock,
        'category': category
    }
    print(f"Product '{name}' added successfully.")

def update_product(products, name, new_price=None, new_stock=None):
    if name not in products:
        print(f"Error: Product '{name}' does not exist.")
        return  

    if new_price is not None:
        products[name]['price'] = new_price
    if new_stock is not None:
        products[name]['stock'] = new_stock

    print(f"Product '{name}' updated successfully.")

def view_products(products):
    if not products:
        print("No products available.")
        return  

    header = f"{'Name':<15}{'Price':<10}{'Stock':<10}{'Category':<15}"
    lines = [header, "=" * len(header)]
    for name, details in products.items():
        lines.append(f"{name:<15}{details['price']:<10}{details['stock']:<10}{details['category']:<15}")
    
    print("\n".join(lines))

def low_stock_report(products, threshold):
    low_stock_items = [
        f"{name} (Stock: {details['stock']})"
        for name, details in products.items()
        if details['stock'] < threshold
    ]
    
    if not low_stock_items:
        print("No low-stock items found.")
        return  
    
    print("Warning: " + ", ".join(low_stock_items))

# Main Program 
products = {}
while True:
    print("\nInventory Management System")
    print("1. Add Product")
    print("2. Update Product")
    print("3. View Products")
    print("4. Low-Stock Report")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        stock = int(input("Enter product stock: "))
        category = input("Enter product category: ")
        add_product(products, name, price, stock, category)  

    elif choice == "2":
        name = input("Enter product name to update: ")
        update_choice = input("Update (1) Price or (2) Stock? ")
        if update_choice == "1":
            new_price = float(input("Enter new price: "))
            update_product(products, name, new_price=new_price)  
        elif update_choice == "2":
            new_stock = int(input("Enter new stock: "))
            update_product(products, name, new_stock=new_stock)  
        else:
            print("Invalid choice.")

    elif choice == "3":
        view_products(products)  

    elif choice == "4":
        threshold = int(input("Enter low-stock threshold: "))
        low_stock_report(products, threshold)  

    elif choice == "5":
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")

