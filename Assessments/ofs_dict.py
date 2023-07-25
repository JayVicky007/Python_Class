class Order():
    def __init__(self, order_id: str, items: list, status: str) -> str:
        self.order_id = order_id
        self.items = items
        self.status = status

class OrderFulfillmentSystem():
    def __init__(self):
        self.order = {}

    