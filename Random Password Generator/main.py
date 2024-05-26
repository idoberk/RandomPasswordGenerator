import random
from data import data_list


print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_list = []


for char in range(0, nr_letters + 1):
    password_list.append(random.choice(data_list[0]))

for char in range(0, nr_symbols + 1):
    password_list.append(random.choice(data_list[1]))

for char in range(0, nr_numbers + 1):
    password_list.append(random.choice(data_list[2]))

for _ in password_list:
    random.shuffle(password_list)

password = "".join(password_list)

print(f"Here is your password: {password}")

