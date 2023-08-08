import mysql.connector as sql
from mysql.connector import Error
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

user = os.environ.get('user')
password = os.environ.get('password')
host = os.environ.get('host')
database = os.environ.get('database')

class Product:
    def __init__(self, product_id, name, category, price, stock_quantity):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.stock_quantity = stock_quantity

class Customer:
    def __init__(self, customer_id, name, email, shipping_address):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.shipping_address = shipping_address

class Order:
    def __init__(self, order_id, order_date, customer_id, total_amount, items):
        self.order_id = order_id
        self.order_date = order_date
        self.customer_id = customer_id
        self.total_amount = total_amount
        self.items = items

class OrderItem:
    def __init__(self, product_id, quantity, sub_total):
        self.product_id = product_id
        self.quantity = quantity
        self.sub_total = sub_total

class OrderHistory:
    def __init__(self, order_id, order_date, total_amount, product_name, quantity, sub_total):
        self.order_id = order_id
        self.order_date = order_date
        self.total_amount = total_amount
        self.product_name = product_name
        self.quantity = quantity
        self.sub_total = sub_total


class DB:
    def __init__(self):
        self.__db = sql.connect(
            host=host,
            password=password,
            user=user,
            database=database
        )
        self.productT = 'products'
        self.customerT = 'customers'
        self.orderT = 'orders'
        self.orderItem = 'order_items'
        self.__cursor = self.__db.cursor()


    def add_product(self, product: Product):
        self.__cursor.execute(f'INSERT INTO {self.productT} (name, category, price, stock_quantity) VALUES (%s, %s,%s,%s)', 
    (product.name, product.category, product.price, product.stock_quantity))
        self.__db.commit()    

    def remove_product(self, id):
        self.__cursor.execute(
            f'DELETE FROM {self.productT} WHERE product_id = {id}')
        self.__db.commit()

    def update_product(self, product: Product):
        self.__cursor.execute(
            f'UPDATE {self.productT} SET name = %s, category = %s, price = %s, stock_quantity = %s WHERE product_id = %s',
            (product.name, product.category, product.price, product.stock_quantity, product.product_id))
        self.__db.commit()
    
    def add_customer(self, customer: Customer):
        self.__cursor.execute(
            f'INSERT INTO {self.customerT} (name, email, shipping_address) VALUES (%s,%s,%s)',
            (customer.name, customer.email, customer.shipping_address))
        self.__db.commit()

    def update_customer(self, customer: Customer):
        self.__cursor.execute(
            f'UPDATE {self.customerT} SET name = %s, email = %s, shipping_address = %s WHERE customer_id = %s',
            (customer.name, customer.email, customer.shipping_address, customer.customer_id))
        self.__db.commit()

    def place_order(self, customer_id, total_amount):
        order_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.__cursor.execute(
            f'INSERT INTO {self.orderT} (order_date, customer_id, total_amount) VALUES (%s, %s, %s)',
            (order_date, customer_id, total_amount))
        self.__db.commit()

    def get_order(self, table_name, customer_id):
        self.__cursor.execute(
            f'SELECT * FROM {table_name} WHERE customer_id = %s',
            (customer_id,))
        return self.__cursor.fetchall()
        
    def view_order_history(self, customer_id):
        self.__cursor.execute(
            f'SELECT order_id, order_date, total_amount FROM {self.orderT} WHERE customer_id = %s', (customer_id,))
        
        order_history = []
        for row in self.__cursor.fetchall():
            order_id, order_date, total_amount = row
            order_history.append(Order(order_id, order_date, customer_id, total_amount, []))  # Assuming your Order class constructor requires an items argument.
        
        return order_history 
    
    def get_all_products(self):
        self.__cursor.execute(f'SELECT * FROM {self.productT}')
        rows = self.__cursor.fetchall()
        products = []
        for row in rows:
            product_id, name, category, price, stock_quantity = row
            product = Product(product_id, name, category, price, stock_quantity)
            products.append(product)
        return products    
    

    def close(self):
        self.__db.close()


def main():
    db = DB()
    
    print("Welcome to SuperMart - Your Online Shopping Destination!")
    
    while True:
        print("1. Browse products")
        print("2. Add a product to cart")
        print("3. View cart")
        print("4. Place an order")
        print("5. View order history")
        print("6. Register as a new customer")
        print("7. Update customer information")
        print("8. Exit")
        
        choice = input("Please select an option: ")
        
        if choice == '1':
            print("\n--Available Products--")
            products = db.get_all_products()
            for product in products:
                print(f"Product ID: {product.product_id} | Name: {product.name} | Category: {product.category} | Price: ${product.price:.2f} | Stock Quantity: {product.stock_quantity}")   
        
        elif choice == '2':
            pass
        
        elif choice == '3':
            pass
        
        elif choice == '4':
            pass
        
        elif choice == '5':
            pass
        
        elif choice == '6':
            pass
        
        elif choice == '7':
            pass
        
        elif choice == '8':
            print("Thank you for using SuperMart. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please select a valid option.")

    db.close()

if __name__ == "__main__":
    main()