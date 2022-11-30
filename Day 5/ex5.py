# Go to: https://replit.com/@appbrewery/password-generator-start?v=1
import random 
import string
alphabet = list(string.ascii_lowercase)
symbols_list = list(string.punctuation)
numbers_list = [i for i in range(10)]

letters = int(input("How many letters would you like in your password? "))
symbols = int(input("How many symbols would you like? "))
numbers = int(input("How many numbers would you like? "))

password = ""
for x in range(letters):
    value = random.randint(0,len(alphabet)-1)
    password += str(alphabet[value])
for x in range(symbols):
    value = random.randint(0,len(symbols_list)-1)
    password += str(symbols_list[value])
for x in range(numbers):
    value = random.randint(0,len(numbers_list)-1)
    password += str(numbers_list[value])

password_list = list(password)
random.shuffle(password_list)
password_shuffle = ''.join(password_list)

print(password_shuffle)