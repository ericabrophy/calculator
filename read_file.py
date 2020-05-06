import sys
import re

#load a file
def load_file():
    try:
        user_file = input("Enter your file path: ")
        with open (user_file, "r") as file:
            file_read = file.readlines()
            new_list = []
            for i in range(len(file_read)):
                delete = file_read[i].replace('\n','')
                new_list.append(delete)
            return new_list
    except IOError:
        print("There are errors in the file.")
        sys.exit()

def user_file_input():
    user_input = load_file()
    input_equation_list = []
    for line in user_input:
        input_equation_list.append(re.findall("[a-zA-Z]|[\d\.]+|[^a-zA-Z0-9]|[\t]+", line))
    return input_equation_list
