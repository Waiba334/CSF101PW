#11
x = 10 #Global variable

def print_x():
    x = 20     #Local variable
    print(f"Local x: {x}")

print_x()
print(f"Gobal x: {x}")

#12
count = 0  #Global variable

def incerment():    #function
    global count
    count += 1 
    print(f"Count: {count}")

incerment()
incerment()
print(f"Final count: {count}")

#13
def outer():
    x = "outer"   

    def inner():
        nonlocal x
        x = "inner"
        print(f"Inner x: {x}")

    inner()
    print(f"Outer x: {x}")

outer()