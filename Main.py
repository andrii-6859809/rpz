class Order:
    def __init__(self, quantity, item_price):
        self.quantity = quantity
        self.item_price = item_price

    def _calculate_discounted_price(self, base_price): # Виділення методу
        if self.quantity > 100:
            return base_price * 0.85
        return base_price * 0.9

    def calculate_total_price(self, discount_rate=None): # Заміна параметра
        base_price = self.quantity * self.item_price
        if discount_rate is not None:
            return base_price * discount_rate
        return base_price # Вбудовування умовного оператора для випадку відсутнос…

    def get_quantity(self): # Додавання методу
        return self.quantity

class OrderFormatter: # Переміщення методу в новий клас
    @staticmethod
    def format_details(order): # Вбудовування тимчасової змінної 'details'
        quantity = order.get_quantity() # Вбудовування методу
        item_price = order.item_price # Вбудовування поля
        return f"Кількість: {quantity}, Ціна за одиницю: {item_price}"

def print_order_summary(order, apply_discount_rate=None): # Заміна параметра
    formatted_details = OrderFormatter.format_details(order)
    total = order.calculate_total_price(apply_discount_rate)
    print(f"Деталі замовлення: {formatted_details}")
    print(f"Загальна вартість: {total}")

# --- Приклад використання
order1 = Order(5, 10.0)
print_order_summary(order1, None) # Використання нової логіки знижок

order2 = Order(120, 5.0)
print_order_summary(order2, 0.85)