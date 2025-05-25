class Order:
    def __init__(self, quantity, item_price):
        self.quantity = quantity
        self.item_price = item_price

    def _get_base_price(self):
        return self.quantity * self.item_price

    def _calculate_quantity_discount(self, base_price): # Декомпозиція умов. оп.
        if self.quantity > 100:
            return base_price * 0.85
        return base_price

    def calculate_total_price(self, discount_rate=None):
        base_price = self._get_base_price()
        if discount_rate is not None:
            return base_price * discount_rate
        return base_price

    def get_quantity(self):
        return self.quantity

class OrderFormatter:
    @staticmethod
    def format_details(order):
        return f"Кількість: {order.get_quantity()}, Ціна за одиницю: {order.item_price}"

def print_order_summary(order, apply_discount_rate=None):
    formatted_details = OrderFormatter.format_details(order)
    total = order.calculate_total_price(apply_discount_rate)
    print(f"Деталі замовлення: {formatted_details}")
    print(f"Загальна вартість: {total}")

# --- Приклад використання
order1 = Order(5, 10.0)
print_order_summary(order1, None)

order2 = Order(120, 5.0)
print_order_summary(order2, 0.85)
