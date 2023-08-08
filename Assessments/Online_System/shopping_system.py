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

class OrderItem:
    def __init__(self, product_id, quantity, sub_total):
        self.product_id = product_id
        self.quantity = quantity
        self.sub_total = sub_total

class Order:
    def __init__(self, order_id, order_date, customer_id, total_amount, items):
        self.order_id = order_id
        self.order_date = order_date
        self.customer_id = customer_id
        self.total_amount = total_amount
        self.items = items

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

    def get_all_data(self, tableName):
        self.__cursor.execute(f'SELECT * FROM {tableName}')
        return self.__cursor.fetchall()
    
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
    
    def close(self):
        self.__db.close()


if __name__ == "__main__":
    db = DB()

    # product = Product(1, 'Fan', 'Electronics', 500.0, 10)
    # customer = Customer(1, 'John Dew', 'john@gmail.com', '123 Main St, City')
    # order_item = OrderItem(1, 2, 1000)

    # db.add_product(product)
    # db.add_customer(customer)
    # db.update_product(Product(1, 'Fridge', 'Electronics', 600.0, 5))

    products = db.get_all_data('products')
    for product in products:
        print(product[1])  # Index 1 corresponds to the name column

    # items = [order_item]
    # db.place_order(1, sum(item.sub_total for item in items))

    # retrieved_product = db.get_product_by_id(1)
    # print(retrieved_product.name)

    # retrieved_customer = db.get_customer_by_id(1)
    # print(retrieved_customer.name)

    # orders = db.get_order('orders', 1)
    # for order in orders:
    #     print(f"Order ID: {order.order_id}, Total Amount: {order.total_amount}")

    db.close()