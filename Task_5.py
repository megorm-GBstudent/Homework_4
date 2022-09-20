# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
# 2*a+2*b
# 4*b-2*a
# 6*b+2*a-2*a

num_dict = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
letter_dict = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'v', 'x', 'y', 'z']
op_dict1 = ['+', '-']
op_dict2 = ['*', '/']


def string_split(string):
    symbols = []

    for symbol in string:
        symbols.append(symbol)

    return symbols


file1 = open('file1.txt', 'r')
file1 = string_split(*file1)
print(file1)

file2 = open('file2.txt', 'r')
file2 = string_split(*file2)
print(file2)

last_operator = ''
last_type = ''
file1_math = []
file2_math = []

math_part = ''

for symbol in file1:
    if symbol in num_dict:
        #print(symbol, 'num')
        last_type = 'num'
        math_part = math_part + symbol

    if symbol in letter_dict:
        #print(symbol, 'letter')
        last_type = 'letter'
        math_part = math_part + symbol

    if symbol in op_dict1:
        #print(symbol, 'operator1')
        last_type = 'operator1'
        file1_math.append(math_part)
        file1_math.append(symbol)
        math_part = ''
        continue

    if symbol in op_dict2:
        #print(symbol, 'operator2')
        last_type = 'operator2'
        math_part = math_part + symbol
file1_math.append(math_part)
math_part = ''

for symbol in file2:
    if symbol in num_dict:
        #print(symbol, 'num')
        last_type = 'num'
        math_part = math_part + symbol

    if symbol in letter_dict:
        #print(symbol, 'letter')
        last_type = 'letter'
        math_part = math_part + symbol

    if symbol in op_dict1:
        #print(symbol, 'operator1')
        last_type = 'operator1'
        file2_math.append(math_part)
        file2_math.append(symbol)
        math_part = ''
        continue

    if symbol in op_dict2:
        #print(symbol, 'operator2')
        last_type = 'operator2'
        math_part = math_part + symbol
file2_math.append(math_part)
math_part = ''

file3_math = []
for i in file1_math:
    file3_math.append(i)
file3_math.append('+')
for i in file2_math:
    file3_math.append(i)

print(file1_math)
print(file2_math)
result = ''
for i in file3_math:
    result += i
print(result)

file3 = open('file3.txt', 'w+')
file3.write(result)
print(*file3)


