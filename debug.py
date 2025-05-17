from customer import Customer
from coffee import Coffee
from order import Order


c1 = Customer("Alice")
c2 = Customer("Bob")
latte = Coffee("Latte")
mocha = Coffee("Mocha")


c1.create_order(latte, 3.5)
c1.create_order(mocha, 4.0)
c2.create_order(latte, 4.5)


print(c1.orders())
print(c1.coffees())
print(latte.orders())
print(latte.customers())
print(latte.num_orders())
print(latte.average_price())
print(Customer.most_aficionado(latte)) 
