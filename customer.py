from order import Order

class Customer:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value
        else:
            raise ValueError("Customer name must be a string between 1 and 15 characters.")
        
    def orders(self):
        return [order for order in Order.all_orders if order.customer == self]

    def coffees(self):
        return list(set(order.coffee for order in self.orders()))
    
    def create_order(self, coffee, price):
        return Order(self, coffee, price)
    
    @classmethod
    def most_aficionado(cls, coffee):
        customer_spending = {}
        for order in Order.all_orders:
            if order.coffee == coffee:
                customer_spending[order.customer] = customer_spending.get(order.customer, 0) + order.price
        if not customer_spending:
            return None
        return max(customer_spending, key=customer_spending.get)
    
    def __repr__(self):
       return f"Customer('{self.name}')"


        
    