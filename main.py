import Customer
import Inventory
import Product


customer = Customer.Customer('fatih', 'fatihcil.2001@gmail.com')
#print(customer.name)
#print(customer.email)

apple_watch = Product.Product('Phone', 999)
#print(apple_watch.name)
#print(apple_watch.price)

mac = Product.Product('Laptop', 1999)
#print(mac.name)
#print(mac.price)

inventory = Inventory.Inventory()
inventory.add_product(apple_watch, 100)
inventory.add_product(mac, 498)

inventory.print_inventory()
customer.purchase(inventory, apple_watch)
customer.purchase(inventory, mac)
inventory.print_inventory()
customer.print_purchases()