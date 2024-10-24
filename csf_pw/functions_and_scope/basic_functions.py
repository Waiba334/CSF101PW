#1
def greet():       #using function greet
    print("Hello, World!")

greet()

#2
def greet(name):      #function greet modified
    print(f"Hello {name}!")

greet("Alice")

#3
def square(number):        #function square
    return number ** 2     #exponentiation operator

result = square(5)         #parameter number to square
print(result)

#4
def is_even(number):       #function is_even
    return number % 2 == 0  #remainder/modules

print(is_even(4))
print(is_even(7))

#5 
def print_numbers(n):      #function print_number
    for i in range(1, n + 1):     #for loops where 5 + 1  =  6 
        print(i)               # actual range (1, 6)

print_numbers(5)