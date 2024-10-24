#18
name = "Bishal"  #str
age = 20       #int
height = 187  #int
is_student = True  #booleans

person_info = {           #dictionary info
    "name": name,           #this is use  to repercent informatio
    "age": age,               #for the given value 
    "height": height,
    "is_student": is_student 
}
print(person_info)

#19
person_info["favourite_colors"] = "blue"  #adding info to dictionary
print(person_info)

#20
try:
    print(person_info["weight"])  #trying to access a ket that is not in dictionary
except KeyError as e:
    print(f"Error: {e}")


