#John Rick Santillan    #1910045

class ItemToPurchase:
    def __init__(self,item_name='none',item_price=0,item_quantity=0,item_description='none'):
        self.item_name= item_name
        self.item_price=item_price
        self.item_quantity=item_quantity
        self.item_description=item_description

    def print_item_cost(self):
        print(self.item_name, self.item_quantity, "@", "$" + str(self.item_price).split('.')[0], '=','$' + str(self.item_price * self.item_quantity).split('.')[0])
    def print_item_description(self):
        print(self.item_name+': '+self.item_description)
class ShoppingCart:
    def __init__(self,customer_name='none',current_date='January 1,2016'):
        self.customer_name=customer_name
        self.current_date=current_date
        self.cart_item=[]
    def add_item(self,ItemToPurchase):
        self.cart_item.append(ItemToPurchase)
    def remove_item(self,item_name):
        tremove = False
        for i in self.cart_item:
            if i.item_name == item_name:
                self.cart_item.remove(i)
                tremove = True
                break
        if not tremove:
            print("Item not found in cart. Nothing removed")
        # if item_name not in self.cart_item:
        #     print("Item not found in cart. Nothing removed")
        # else:
        #     self.cart_item.remove(item_name)
    def modify_item(self,ItemToPurchase):
        m_item = False
        for i in self.cart_item:
            if i.item_name == ItemToPurchase.item_name:
                m_item = True
                if ItemToPurchase.item_price != 0:
                    i.item_price = ItemToPurchase.item_price
                if ItemToPurchase.item_description != 'none':
                    i.item_description = ItemToPurchase.item_description
                if ItemToPurchase.item_quantity !=0:
                    i.item_quantity = ItemToPurchase.item_quantity
                break

        if not m_item:
            print("Item not found in cart. Nothing removed.")
    def get_num_item_in_cart(self):
        num_item=0
        for i in self.cart_item:
            num_item+= i.item_quantity
        return num_item
    def get_cost_of_cart(self):
        cost_cart = 0
        cost=0
        for i in self.cart_item:
            cost = (i.item_quantity * i.item_price)
            cost_cart += cost
        return cost_cart
    def print_total(self):
        total_cost = self.get_cost_of_cart()
        if(total_cost==0):
            print("SHOPPING CART IS EMPTY")
        else:
            print("OUTPUT SHIPPING CART")
            print(self.customer_name+"'s","Shopping Cart -",self.current_date)
            print('Number of Items:',self.get_num_item_in_cart())
            print()
            for i in self.cart_item:
                i.print_item_cost()
            print()
            print('Total:','$'+str(total_cost))
    def print_descriptions(self):
        if len(self.cart_item)==0:
            print('SHOPPING CART IS EMPTY')
        else:
            print(self.customer_name+"'s","Shopping Cart -",self.current_date)
            print()
            print("Item Descriptions")
            for i in self.cart_item:
                i.print_item_description()

def print_menu(nc):
    new_cart=nc
    key = ''
    while (key != 'q'):
        print('MENU')
        print('a - Add item to cart')
        print('r - Remove item from cart')
        print('c - Change item quantity')
        print("i - Output item's description")
        print('o - Output shopping cart')
        print('q - Quit')
        print()
        key = input('Choose an option:')
        if (key == "a"):
            print('ADD ITEM TO CART')
            item_name = input('Enter the item name:')
            item_description = input('Enter the item description:')
            item_price = int(input('Enter the item price:'))
            item_quantity = int(input('Enter the item quantity:'))
            itemToPurchase = ItemToPurchase(item_name,item_price,item_quantity,item_description)
            new_cart.add_item(itemToPurchase)
        elif(key=='r'):
            print('REMOVE ITEM FROM CART')
            item_name = input('Enter name of item to remove:\n')
            new_cart.remove_item(item_name)
        elif(key=='c'):
            print('CHANGE ITEM QUANTITY:\n')
            item_name = input('Enter the item name:\n')
            tem_quantity = int(input('Enter the new quantity:\n'))
            itemToPurchase = ItemToPurchase(item_name,0,tem_quantity)
            new_cart.modify_item(itemToPurchase)
        elif(key=='i'):
            print("OUTPUT ITEMS' DESCRIPTIONS")
            new_cart.print_descriptions()
        elif(key=='o'):
            print('OUTPUT SHOPPING CART\n')
            new_cart.print_total()




if __name__ == "__main__":
    customer_name = input("Enter customer's name: \n")
    current_date = input("Enter today's date: \n")
    print()
    print("Customer name:",customer_name)
    print("Today's date:",current_date)
    nc = ShoppingCart(customer_name,current_date)
    print_menu(nc)







