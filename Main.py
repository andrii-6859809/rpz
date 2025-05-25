class Order:
    def __init__(self, quantity, item_price):
        self._quantity = quantity # приватне поле (індикація)
        self._item_price = item_price # ...
        self._base_price = self._calculate_base_price() # Підйом поля

    def _calculate_base_price(self): # Підйом методу
        return self._quantity * self._item_price

    def calculate_total_price(self, discount_rate=None):
        if discount_rate is not None:
            return self._apply_discount(discount_rate) # Спуск методу
        return self._base_price

    def _apply_discount(self, discount_rate): # Спуск методу
        return self._base_price * discount_rate

    def get_quantity(self):
        return self._quantity # Доступ до приватного поля через метод

    def get_item_price(self):
        return self._item_price # Доступ до приватного поля через метод

class OrderFormatter:
    @staticmethod
    def format_details(order):
        return f"Кількість: {order.get_quantity()}, Ціна за одиницю: {order.get_item_price()}"

def print_order_summary(order, apply_discount_rate=None):
    formatted_details = OrderFormatter.format_details(order)
    total = order.calculate_total_price(apply_discount_rate)
    print(f"Деталі замовлення: {formatted_details}")
    print(f"Загальна вартість: {total}")

# Приклад використання
order1 = Order(5, 10.0)
print_order_summary(order1, None)

order2 = Order(120, 5.0)
print_order_summary(order2, 0.85)