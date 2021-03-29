# John Rick Santillan     #1910045
class FoodItem:

    def __init__(self,name='None',fats=0.0,carbs=0.0,proteins=0.0):
        self.name = name
        self.fats = fats
        self.carbs = carbs
        self.proteins = proteins

    def get_calories(self, num_servings):
        # Calorie formula
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings;
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

servings = float(input())
food1.print_info()
