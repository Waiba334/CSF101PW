def read_txt_file(inputfile):
    with open(inputfile,'r') as f:
        data = f.readlines()
    return data 

def read_line_from_file(inputfile, ):
    with open(inputfile, 'r') as f:
        lines = f.readlines()
    return lines 


def main():
    text_data = read_txt_file("./input.txt")
    print('data from input:', text_data[0])
    print('data from input:', text_data[1])
    print('data from input:', text_data[2])

main() 