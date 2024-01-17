products = []

# Function to add a new product to the database
def add_product(name, price):
  products.append({
    "name": name,
    "price": price
  })

# Function to edit an existing product in the database
def edit_product(index, name, price):
  products[index]["name"] = name
  products[index]["price"] = price

# Function to delete a product from the database
def delete_product(index):
  del products[index]

# Initialize the customer database
customers = []

# Function to register a new customer
def register_customer(name, email):
  customers.append({
    "name": name,
    "email": email
  })

# Function to place an order
def place_order(customer_index, product_index):
  customer = customers[customer_index]
  product = products[product_index]
  print(f"{customer['name']} has placed an order for {product['name']} at a price of {product['price']}.")

# Example usage
add_product("Laptop", 1000)
add_product("Keyboard", 50)
register_customer("John Smith", "john@example.com")
place_order(0, 0)
