from read_file import user_file_input
from calculate_functions import MyCalculator


file_input = user_file_input()
for item in file_input:
    MyCalculator.evaluate()
