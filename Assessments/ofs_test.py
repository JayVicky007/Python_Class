class Order:
    def __init__(self, order_id, items, status):
        self.order_id = order_id
        self.items = items
        self.status = status

class OrderFulfillmentSystem:
    def __init__(self):
        self.orders = []

    def place_order(self, items):
        order_id = str(len(self.orders) + 1)
        order = Order(order_id, items, "pending")
        self.orders.append(order)
        return order_id

    def process_order(self, order_id):
        order = self.find_order(order_id)
        if order:
            order.status = "processing"

    def ship_order(self, order_id):
        order = self.find_order(order_id)
        if order:
            order.status = "shipped"

    def find_order(self, order_id):
        for order in self.orders:
            if order.order_id == order_id:
                return order
        return None

ofs = OrderFulfillmentSystem()

order_id = ofs.place_order(["item1", "item2"])
print("Order ID:", order_id)

ofs.process_order(order_id)
order_status = ofs.find_order(order_id).status
print("Order status after processing:", order_status)

ofs.ship_order(order_id)
order_status = ofs.find_order(order_id).status
print("Order status after shipping:", order_status)










'''
Problem: Order Fulfillment System:
You are tasked with implementing an order fulfillment system for an e-commerce company. The system should 
allow users to place orders, process them, and track their status.

Requirements:
Implement a class called "Order" with the following
attributes:
order_id (string): unique identifier for each order
items (list): a list of items included in the order
status (string): current status of the order (e.g.,
"pending", "processing", "shipped", "delivered")

Implement a class called "OrderFulfillmentSystem"
with the following methods:
place_order(items: List[str]) > str: Creates a new
order with the provided items and returns the order
ID.
process_order(order_id: str) -> None: Updates the
status of the order with the given order ID to
"processing".
ship_order(order_id: str) > None: Updates the
status of the order with the given order ID to
"shipped".
'''

