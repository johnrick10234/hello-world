#John Rick Santillan #1910045

class ItemToPurchase:
    def __init__(self):
        self.item_name = "none"
        self.item_price=0
        self.item_quantity=0
    def print_item_cost(self):
        print(self.item_name,self.item_quantity,"@","$"+str(self.item_price).split('.')[0],'=','$'+str(self.item_price * self.item_quantity).split('.')[0])

if __name__ == "__main__":
    print("Item 1")
    Item1=ItemToPurchase()
    item_name=input("Enter the item name:\n")
    item_price=float(input("Enter the item price:\n"))
    item_quantity=int(input("Enter the item quantity:\n"))
    Item1.item_name = item_name
    Item1.item_price = item_price
    Item1.item_quantity = item_quantity
    print()
    print("Item 2")
    Item2=ItemToPurchase()
    item_name=input("Enter the item name:\n")
    item_price=float(input("Enter the item price:\n"))
    item_quantity=int(input("Enter the item quantity:\n"))
    Item2.item_name = item_name
    Item2.item_price = item_price
    Item2.item_quantity = item_quantity


    print()
    total = (Item1.item_price * Item1.item_quantity) + (Item2.item_price * Item2.item_quantity)
    print('TOTAL COST')
    Item1.print_item_cost()
    Item2.print_item_cost()
    print()
    print('Total:','$'+str(total).split('.')[0])




