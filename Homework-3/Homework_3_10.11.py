# John Rick Santillan     #1910045
class FoodItem:

    def __init__(self,name='None',fats=0.0,carbs=0.0,proteins=0.0):
        self.name = name
        self.fats = fats
        self.carbs = carbs
        self.proteins = proteins

    def get_calories(self, servings):
        # Calorie formula
        calories = ((self.fats * 9) + (self.carbs * 4) + (self.proteins * 4)) * servings;
        return calories

    def print_info(self):
        print('Nutritional information per serving of {}:'.format(self.name))
        print('   Fat: {:.2f} g'.format(self.fats))
        print('   Carbohydrates: {:.2f} g'.format(self.carbs))
        print('   Protein: {:.2f} g'.format(self.proteins))

if __name__ == "__main__":
    food1= FoodItem()
    name_item = input()
    number_fats = float(input())
    number_carbs = float(input())
    number_proteins = float(input())

serving = float(input())
food1.print_info()
print("Number of calories for","{:.2f}".format(serving),"serving(s):","{:.2f}".format(food1.get_calories(serving)))
food2 = FoodItem(name_item,number_fats,number_carbs,number_proteins)
print()
food2.print_info()
print("Number of calories for","{:.2f}".format(serving),"serving(s):","{:.2f}".format(food2.get_calories(serving)))