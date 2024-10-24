#1 area of rectangle
length = int(input("Enter length in cm: "))   
width = int(input("Enter width in cm: "))
area = length * width            #formula or condition 
print(f"Area of rectangle = {area}")

#2 even or odd
num = int(input("Enter a number to check even od odd: "))   #using input to check even or odd int variable
if num % 2 == 0:                               # num should be divisible by 2 with 0 remainder
    print(f"Number is even: {num}")
else:
    print(f"Number is odd: {num}")

#3 largest number
a = int(input("Enter first number: "))
b = int(input("ENter second number: "))
c = int(input("Enter third number: "))
if (a >= b) and (a >= c):
    largest = a                     #condition
elif (b >= a) and (b >= c):
    largest = b                    #condition
else:
    largest = c 
    
print(largest, "is the largest number")                     #condition


#4 convert tem celsius to fahrenheit
c = int(input("Enter tempture in celsius: "))
f = int(input("Enter tempture in farhrenheit: "))
fahrenheit = (c*9 /5) + 32 
print(fahrenheit, "is the tempture in fahrenheit")

#5 calculate the sum off all the numbers from 1 to n
num = int(input("number: "))
sum = 0                     #where num will be added like if 
for i in range(num+1):       # num is 5 then 1+2+3+4+5 which is the sum
    sum += i
print(f"The sum of numbers from 1 to n is: {sum}")
    
#6 Check if a given year is a leap year
year = int(input("Enter the year(eg:2018): "))
if (year % 4 == 0) or (year % 100 == 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not leap year")

#7 Generate the first n terms of the Fibonacci sequence.
def rec_fib(n):                              #I have used py algorithm recursive solution 
    if n > 1:                                #recursion is when you have a call directly to the function itself.
        return rec_fib(n-1) + rec_fib(n-2)   #In our case, in fact, we call the function rec_fib within the same function rec_fib.
    return n 

n = int(input("Enter the n term: "))

for i in range(0 , n + 1):
    print(rec_fib(i))

#8 Calculate the factorial of a given number.
def factorial(x):                   #I again used py algorithms recursive  solution   #formule to calculate the factorial number is n! = n*(n-1)*(n-2),,,,,,,,
    if x < 0:    #first condition
        return("does not exist for negative integer!")
    elif x == 1 or x == 0:    #second condition 
        return 1
    else:
        return (x * factorial(x-1))  #the main condition the recusive call to the function
    
n = int(input("Enter the number: "))

result = factorial(n)   #call of function
print(f"The factorial of {n} = {result}")


            
