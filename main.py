# price = 10
# price = 20.53
# is_accepted = False
# name = 'Sia'
#
# print("(o-o)\n" * 5)
# print(type(price))
# print(type(is_accepted))
# print(type(name))
#
# name = input('What is your name? ')
# color = input('What is your favourite color? ')
# print('"' + name + ' likes ' + color + ' color.'+'"')

# birth_year = input('Input your birth year. ')
# current_year = input('Input the current year. ')
# age = int(current_year) - int(birth_year)
# print('Your age is, ' + str(age))

# weightInPound = input('Input your weight in pound: ')
# weightInKilo = int(weightInPound) / 2.205
# # precision point in python
# print('%.2f' % weightInKilo)
# print("{0:.2f}".format(weightInKilo))
# print(round(weightInKilo, 2))

# print(
#     '''
#     Nice to meet you.
#     '''
# )

# course = 'Python for beginners.'
# print(course[-3])
# name = 'Pollab'
# print(name[1:-1])

# first_name = 'Pollab'
# last_name = 'Ahmed'
# strong = f'{first_name} {last_name} is my name.'
#
# print(len(first_name))
#
# print(first_name.replace('P', 'M'));
# print(first_name)
#
# print('Pol' in first_name)

# is_hot = False
# is_cold = False
#
# if is_hot:
#     print("It is a hot day.")
#     print('Drink more water.\n')
# elif is_cold:
#     print('It is a cold day.')
#     print('Wear warm cloths.\n')
# else :
#     print('It is a lovely day.\n')
# print('Be safe')

# house_price = 1000000
# has_good_credit = False
#
# if has_good_credit:
#     down_payment = 0.01 * house_price
# else:
#     down_payment = 0.02 * house_price
# print(f"Down payment is ${down_payment}")

# has_umbrella = True
# is_raining = True
# is_hot = True
#
# if is_raining and has_umbrella:
#     print('You have advantage.')

# temperature = input("Input today's temperature: ")
#
# if int(temperature) >= 30:
#     print('It is a hot day')
# elif int(temperature) <= 10:
#     print('It is a cold day')
# else:
#     print('It is neither hot or cold')
# name = input("Enter a name: ")
#
# if len(name) <= 3:
#     print("Name must be 3 character long.")
# elif len(name) > 50:
#     print("Name can be a maximum of 50 characters.")
# else:
#     print("Name looks fine.")

# weight = int(input("Input your weight: "))
# typo = input("(L)bs or K(g): ")
# if typo.upper() == "L":
#     convert = weight * 2.205
#     # print("Your weight in (L)bs is " + str(convert))
#     print(f"Your are {convert} pounds.")
# elif typo.upper() == "K":
#     convert = weight / 2.205
#     # print("Your weight in (K)g is " + str(convert))
#     print(f"Your are {convert} kilos.")
# else:
#     print("Wrong input.")

# i = 1
# while i <= 5:
#     print("(0-0)" * i)
#     i = i + 1
# print("Done")

# import random
#
# secret = random.randint(1, 10)
# guess_limit = 1
# guess_count = 0
# # print(secret)
# print("Guess The Secret Number Game!")
# print("  You have three chances!")
# while guess_limit <= 3:
#     guess = int(input("Guess: "))
#     guess_limit = guess_limit + 1
#     if guess != secret:
#         guess_count = guess_count + 1
#         continue
#     elif guess == secret:
#         print("You win!")
#         break
# else:
#     print("You lose!")

# print("If you don't know any command, type 'help' and press 'ENTER'.")
# get = input()
#
# while True:
#     if get.lower() == "help":
#         print("You can insert the following commands,"
#               "\n start - start the car "
#               "\n stop - stop the car "
#               "\n quit the program")
#     elif get.lower() == "start":
#         print("The car started....Ready to go!")
#     elif get.lower() == "stop":
#         print("The car stopped!")
#     elif get.lower() != "quit":
#         exit()
#     else:
#         print("Sorry! I don't understand your command!")


# class Item:
#     def __init__(self):
#         print("I am created!")
#
#     def total_price(self,
#                     x,
#                     y):
#         return x * y
#
#
# item1 = Item()
# item1.name = "Phone"
# item1.price = 100
# item1.quantity = 5
# print(item1.total_price(item1.price, item1.quantity))
#
# item2 = Item()
# item2.name = "Laptop"
# item2.price = 1000
# item2.quantity = 3
# print(item2.total_price(item2.price, item2.quantity))

# print("hello" + " " + "world")
#
# a, b, c = 3, 4, 5
# print(a, c)

# myString = "hello"
# myFloat = 10.0
# myInt = 20
# myName = "Pollab"
#
# # testing code
# if myString == "hello":
#     print("String: %s, %s." % (myString, myName))
#     # print("String: {}, {}.".format(myString, myName))
#     if isinstance(myFloat, float) and myFloat == 10.0:
#         print("Float: %f" % myFloat)
#     if isinstance(myInt, int) and myInt == 20:
#         print("Integer: %d" % myInt)

# myList = ["Potato", 3, 23.54]
#
# # myList.append("Potato")
# # myList.append(3)
# # myList.append(23.54)
#
# print(myList[2])
#
# for x in myList:
#     print(x)

# numbers = [1, 2, 3]
# strings = ['hello', 'world']
# names = ['Jhon', 'Eric', 'Jessica']
#
# second_name = names[1]
#
# print(numbers)
# print(strings)
# print("The second name on the names list is %s" % second_name)

# even_numbers = [2, 4, 6, 8]
# odd_numbers = [1, 3, 5, 7]
#
# print(even_numbers + odd_numbers)
#
# print([1, 2, 3] * 3)

# x = object()
# y = object()
#
# x_list = [x] * 10
# y_list = [y] * 10
# big_list = x_list + y_list
#
# print("x_list contains %d objects" % len(x_list))
# print("y_list contains %d objects" % len(y_list))
# print("big_list contains %d objects" % len(big_list))
#
# if x_list.count(x) == 10 and y_list.count(y) == 10:
#     print("Almost there...")
# if big_list.count(x) == 10 and big_list.count(y) == 10:
#     print("Great!")
#
astring = "Joy Bangladesh"
print(astring[::-1])

