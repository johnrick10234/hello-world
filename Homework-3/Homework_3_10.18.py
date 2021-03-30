#John Rick Santillan    #1910045

class ItemToPurchase:
    def __init__(self,item_name='none',item_price=0,item_quantity=0,item_description='none'):
        self.item_name= item_name
        self.item_price=item_price
        self.item_quantity=item_quantity
        self.item_description=item_description

    def print_item_cost(self):
        print(self.item_name, self.item_quantity, "@", "$" + str(self.item_price).split('.')[0], '=','$' + str(self.item_price * self.item_quantity).split('.')[0])
    def pritn_item_description(self):
        print(self.item_name+': '+self.item_description)