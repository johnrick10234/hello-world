class ItemToPurchase:
    def __init__(self):
        self.item_name = "none"
        self.item_price=0
        self.item_quantity=0
    def item_cost(self):
        print(self.item_name,self.item_quantity,"@","$"+str(self.item_price),'=','$'+str(self.item_price * self.item_quantity))

if __name__ == "__main__":
    Item=ItemToPurchase()
    item_name=input()
    item_price=float(input())
    item_quantity=int(input())


    Item.item_name = item_name
    Item.item_price = item_price
    Item.item_quantity = item_quantity
Item.item_cost()
print(Item.item_cost)


