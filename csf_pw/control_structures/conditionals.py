#1
number = 10      #int variable
if number > 0:                          #this is if elif and else statement
    print ("The number is positive.")
else:
    print ("The number is non-positive.")

#2
number =  0              #int variable
if number > 0:
    print ("The number is positive.")   #if else statement for separate cases
elif number <0:
    print ("The number is negative.")
else:
    print ("The number is zero.")

#3
score = 85      #int variable
if score >= 90:
    grade = "A"
elif score >= 80:     #using the if else statement for assignning grades
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    print ="D"
else:
    grade = "F"
print(f"Your grade is: {grade}")

#4
number = 7     #int variable                    
result = "even" if number % 2 == 0 else "odd"   #using ternary operator with if and else statemnt 
print(f'The number is {result}')

#5
num1 = 10  #int variable
num2 = 5   
operator = "+"

if operator == "+":          #addition
    result = num1 + num2    
elif operator == "-":        #subtraction
    result = num1 - num2 
elif operator == "*":        #multiplication
    result = num1 * num2 
elif operator == "/":        #division
    result = num1 / num2 if num2 != 0 else "Error: Division by zero"   #ternary operator
else:
    result = "Error: Invalid operator"

print(f"Result: {result}")

#15
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

number = 17
if is_prime(number):
    print(f"{number} is a prime.")
else:
    print(f"{number} is not prime.")