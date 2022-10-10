import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
no_lett= int(input("How many letters would you like in your password?\n")) 
no_sym = int(input(f"How many symbols would you like?\n"))
no_no = int(input(f"How many numbers would you like?\n"))

password_list = []

for char in range(1, no_lett + 1):
  password_list.append(random.choice(letters))

for char in range(1, no_sym + 1):
  password_list += random.choice(symbols)

for char in range(1, no_no + 1):
  password_list += random.choice(numbers)


random.shuffle(password_list)


password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")

print('the end of program')
