#9
import os

def file_exists(filename):
    return os.path.exists(filename)

print(f"'sample.text' exists: {file_exists('sample.txt')}")
print(f"'nonexistent.txt' exists: {file_exists('nonexistent.txt')}")

#10
import os 

def rename_file(old_name, new_name):
    os.rename(old_name, new_name)

rename_file('sample.txt', 'renamed_sample.txt')
print("File renamed successfully.")
print(f"'renamed_sample.txt' exists: {file_exists('renamed_sample.txt')}")

#11
import os 

def delete_file(filename):
    if os.path.exists(filename):
        os.remove(filename)
        print(f"{filename} has been deleted.")
    else:
        print(f"{filename} does not exist.")

delete_file('binary_sample.bin')

#12
import os 

def create_directory(directory_name):
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)
        print(f"Directory '{directory_name}' created successfully.")
    else:
        print(f"Directory '{directory_name}' already exists.")

create_directory('new_folder')

#13
import os 

def list_file(directory):
    files = os.listdir(directory)
    for file in files:
        print(file)

print("Files in the current directory:")
list_file('.')

#14
import shutil

def copy_file(source, destination):
    shutil.copy2(source, destination)
    print(f"File copied from {source} to {destination}")

copy_file('renamed_sample.txt', 'new_folder/copied_sample.txt')

#15
import csv

def read_csv_file(filename):
    with open(filename, 'r', newline='') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            print('.'.join(row))

with open('sample.csv', 'w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(['Name', 'Age', 'City'])
        csv_writer.writerow(['Alice', '30', 'New York'])
        csv_writer.writerow(['Bob', '25', 'Los Angeles'])

print("Contents of sample.csv:")
read_csv_file('sample.csv')
