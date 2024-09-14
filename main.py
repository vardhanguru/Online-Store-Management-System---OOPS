class Product:
    def __init__(self,product_id, name,price, stock, category, description):
        self.product_id = product_id
        self.name = name
        self.price = price
        self._stock = stock
        self.category = category
        self.description = description


    def get_stock(self):
        return self._stock
    
    def reduce_quantity(self, amount):
        if amount <= self._stock:
            self._stock -= amount
            print("successfully purchased")
        else:
            print("Stock is not available")

    def is_in_stock(self,amount):
        return self._stock >= amount
    
    
class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.order_history = []

    def add_order(self,order):
        self.order_history.append(order)

    def view_order_history(self):
        for order in self.order_history:
            print(order)


class Order:
    def __init__(self, customer):
        self.customer = customer
        self.items = []
        self.discount = 0

    def add_product(self,product,quantity):
        if product.is_in_stock(quantity):
            self.items.append((product, quantity))
        else:
            print(f"Not enough stock for {product.name}. Only {product.get_quantity()} left.")

    def apply_discount(self, discount_percentage):
        self.discount = discount_percentage
        print(f"Discount of {self.discount}% applied.")
    def calculate_total(self):
        total = sum(product.price * quantity for product, quantity in self.items)
        if self.discount > 0:
            total -= total * (self.discount / 100)
        return total

    def process_order(self):
        for product, quantity in self.items:
            product.reduce_quantity(quantity)
        total = self.calculate_total()
        self.customer.add_order(self)
        print(f"Order successful! Total cost after discount: ${total:.2f}")
        return total

    def __str__(self):
        details = [f"{product.name} (x{quantity}): ${product.price * quantity}" for product, quantity in self.items]
        return "\n".join(details)


# Payment class to handle payment methods
class Payment:
    def __init__(self, method):
        self.method = method

    def process_payment(self, total_amount):
        print(f"Processing {self.method} payment for ${total_amount:.2f}.")
        print("Payment successful!")


# --- Simulation of the System ---

# Create some products
laptop = Product(101, "Laptop", 1000, 10, "Electronics", "High-performance laptop")
phone = Product(102, "Smartphone", 500, 20, "Electronics", "Latest model smartphone")

# Create a customer
customer1 = Customer("Alice", "alice@example.com")

# Customer places an order with multiple products
order = Order(customer1)
order.add_product(laptop, 2)  # Alice orders 2 laptops
order.add_product(phone, 3)   # Alice orders 3 phones

# Apply a discount
order.apply_discount(10)  # Apply a 10% discount

# Process the order and calculate total
total = order.process_order()

# Payment processing
payment = Payment("Credit Card")
payment.process_payment(total)

# Customer views order history
customer1.view_order_history()
