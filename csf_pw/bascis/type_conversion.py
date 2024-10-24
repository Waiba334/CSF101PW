#12
age = 20  #int
age_str = str(age)  #replacing int in str sentence
message = "I am " + age_str + " years old"
print(message)

#13
num_str = "42"             
num_int = int(num_str)      #converting str to an int 
print(num_int)

#14
non_num_str = "Hello"
try:
    non_num_int = int(non_num_str)   #non numeric str to an int 
    print(non_num_int)
except ValueError as e:
    print(f"Error: {e}")


