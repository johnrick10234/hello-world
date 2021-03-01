# John Rick Santillan   ID# 1910045

user_input=input()
new_input=user_input.replace(' ', '')
rev = new_input[::-1]
if new_input == rev:
    print(user_input +' is a palindrome')
else:
    print(user_input + ' is not a palindrome')
