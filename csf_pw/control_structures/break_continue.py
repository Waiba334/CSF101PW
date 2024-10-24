#11
count = 0 
while True:        #while loops
    print(count)
    count += 1     #count starts with addition operator
    if count >= 5:
        break      #count breaks which means the condition id met in another word the count of addition is finished
print("Loop ended")

#12
for num in range(1, 6):
    if num % 2 == 0:      #from the range(1, 6) 2 num which have zero remainder
        continue          #it will continue to find zero remainder from the given range
    print(num)            #acctualy have to print 2 but it  will print 3

#13
numbers = [4, 2, 7, 1, 8, 3, 6]    #the int variable
search_for = 8          #the paritcular number that to be found

for num in numbers:
    if num == search_for:
        print(f"Found {search_for}!")     #condition made
        break           #the condition is met
    print(f"Not found {search_for}...")

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


#14
import random       #random module

secret_number = random.randint(1, 10)      #selected element numbers
attempts = 0

while True:
    guess = int(input("Guess the number (1-10):"))
    attempts+= 1

    if guess == secret_number:
        print(f"Congratulations! You guessed it in {attempts} attempts.")
    elif guess <secret_number:
        print("Too low. Try again")        #comments
    else:
        print("Too high. Try again")
    