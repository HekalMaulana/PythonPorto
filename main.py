#Write your code below this row 👇
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
my_password = ""

# get random letter
for letter in range(0, nr_letters):
    my_password += random.choice(letters)

# get random symbos
for symbol in range(0, nr_symbols):
    my_password += random.choice(symbols)

# get random number
for number in range(0, nr_numbers):
    my_password += random.choice(numbers)

# Print random password without random list
print(f"Not random password = {my_password}")


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# Memasukan random password ke dalam list
my_password_list = []
for n in range(0, len(my_password)):
    my_password_list += my_password[n]

# Mengacak urutan sebuah list
random.shuffle(my_password_list)

# Memasukan tiap list ke dalam sebuah string
my_random_password = ""
for random_pasword in my_password_list:
    my_random_password += random_pasword

print(f"\nRandom password = {my_random_password}")
