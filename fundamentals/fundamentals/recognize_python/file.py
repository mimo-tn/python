num1 = 42 # variable declaration, initialize Nubers
num2 = 2.3 # variable declaration, initialize Nubers
boolean = True # variable declaration, initialize Boolean
string = 'Hello World' # variable declaration, initialize Strings
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']# initialize list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}# initialize Dictionary
fruit = ('blueberry', 'strawberry', 'banana')# initialize Tuples
print(type(fruit)) # type check Tuples
print(pizza_toppings[1]) # list access value Sausage
pizza_toppings.append('Mushrooms')# list add value
print(person['name'])# Dictionary acces value John
person['name'] = 'George'# Dictionary change value
person['eye_color'] = 'blue'# Dictionary add value
print(fruit[2])# tuples acces value strawberry

if num1 > 45:# conditional if
    print("It's greater")
else:# conditional else
    print("It's lower") # log it's lower

if len(string) < 5:# conditional if lenght check 
    print("It's a short word!")
elif len(string) > 15:# conditional else if
    print("It's a long word!")
else:# conditional else
    print("Just right!")# log Just right!
"""
for loop
    - start 0
    - stop 4
    - increment x by 1

"""
for x in range(5):
    print(x) # 0 1 2 3 4
"""
for loop
    - start 2
    - stop 4
    - increment x by 1

"""
for x in range(2,5):
    print(x) # 2 3 4
"""
for loop
    - start 2
    - stop 9
    - increment x by 3

"""
for x in range(2,10,3):
    print(x) 2 5 8

"""
while loop
    - start 0
    - stop 4
    - increment x by 3

"""
x = 0
while(x < 5):
    print(x) 0 1 2 3 4
    x += 1

pizza_toppings.pop()#delete the last value of the list
pizza_toppings.pop(1)#delete the second value of the list

print(person) #log statement of Dictionary {'name': 'George', 'location': 'Salt Lake', 'age': 37, 'is_balding': False, 'eye_color':'blue'}
person.pop('eye_color') # Dictionary delete value
print(person)#log statement of Dictionary {'name': 'George', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
"""
for loop
    - start Pepperoni
    - stop Olives
    - break Olives
    - sequence topping by the next value

"""
for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

def print_hello_ten_times():# function
    """
    for loop
        - start 0
        - stop 9
    - increment num by 1
    """
    for num in range(10):
        print('Hello') # hello hello hello hello hello hello hello hello hello hello

print_hello_ten_times() # call function print_hello_ten_times()

def print_hello_x_times(x): #declaration function with parameter x
    """
    for loop
        - start 0
        - stop x-1
    - increment num by 1
    """
    for num in range(x):
        print('Hello') # print hello (x-1) times

print_hello_x_times(4) # call function print_hello_x_times() with 4 in parameter

def print_hello_x_or_ten_times(x = 10): # function declaration with x=10 like parameter
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times() # call function print_hello_x_or_ten_times() with 10 parameter 
print_hello_x_or_ten_times(4)# call function print_hello_x_or_ten_times() with 4 parameter 


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)