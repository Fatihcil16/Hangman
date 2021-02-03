class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.purchases = []

    def purchase(self, inventory, product):
        inventory_dict = inventory.inventory
        if product in inventory_dict:
            if inventory_dict[product] > 0:
                self.purchases.append(product)
                inventory_dict[product] -= 1
            else:
                print('We are out of stock!')
        else:
            print("We don't have that product!")

    def print_purchases(self):
        print("The customer has purchased")
        for item in self.purchases:
            print(item.name)