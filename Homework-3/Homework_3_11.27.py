#John Rick Santillan        #1910045

p_dict = {}
sort_list = []

def sort_key():
    s_key = sorted(p_dict.keys())
    return s_key

while(True):
    print('MENU')
    print('a - Add player')
    print('d - Remove player')
    print('u - Update player rating')
    print('r - Output players above a rating')
    print('o - Output roster')
    print('q - Quit\n')
    print(input("Choose an option: "))
