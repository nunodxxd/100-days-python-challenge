#list comprehension numbers
""" numbers = [1, 2, 3]
new_list = [n * 2 for n in numbers]
print(new_list)
 """

#list comprehension string
""" name = "Angela"
letters = [letter for letter in name]
print(letters) """

#create a list with list comprehension
""" list_numbers = [num * 2 for num in range(1,5)]
print(list_numbers) """

#Create a list comprehension with a condicional
""" names = ["Alex","Beth","Caroline","Dave","Eleanor","Freddie"]

short_names = [name for name in names if len(name) < 5]
print(short_names)
long_names = [name.upper() for name in names if len(name) > 5]
print(long_names)
 """