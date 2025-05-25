class Order:
    def __init__(self, quantity, item_price):
        self.quantity = quantity
        self.item_price = item_price

    def calculate_total_price(self, has_discount):
        base_price = self.quantity * self.item_price
        if has_discount:
            if self.quantity > 100:
                return base_price * 0.85
            else:
                return base_price * 0.9
        else:
            return base_price

    def get_item_details(self):
        return f"Кількість: {self.quantity}, Ціна за одиницю: {self.item_price}"

def print_order_summary(order, apply_discount):
    details = order.get_item_details()
    total = order.calculate_total_price(apply_discount)
    print(f"Деталі замовлення: {details}")
    print(f"Загальна вартість: {total}")

# --- Приклад використання
order1 = Order(5, 10.0)
print_order_summary(order1, False)

order2 = Order(120, 5.0)
print_order_summary(order2, True)
