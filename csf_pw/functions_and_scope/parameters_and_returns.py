#6
def greet_with_default(name="Guest"):   #name parameter
    print(f"Hello, {name}!")

greet_with_default()
greet_with_default("Bob")   #valu of guest

#7
def calculate_rectangle_area(width, height):  #function
    return width * height       #function to be return with multiplying w nad h

area = calculate_rectangle_area(5, 3)
print(f"The area of the rectangle is: {area}")

#8
def print_info(**kwargs):    #function that take any no of key word arguments
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="New York")

#9
def min_max(number):    #function min_max
    return min(number), max(number)

result = min_max([5, 2, 8, 1, 9])    #value to be pickeed from here
print(f"Min: {result[0]}, Max: {result[1]}")

#10
def safe_divide(a, b):        #function
    if b == 0: 
        return "Cannot divide by zero"
    return a / b

print(safe_divide(10, 2))
print(safe_divide(5, 0))
