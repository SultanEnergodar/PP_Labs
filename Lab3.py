import re

def find_digits(input_string):
    digits = re.findall('\d', input_string)
    return digits if digits else None

input_string = input("Input string: ")
result = find_digits(input_string)

if result:
    digit_str = ', '.join(result)
    print("Answer: {}".format(digit_str))
else:
    print("No numbers")