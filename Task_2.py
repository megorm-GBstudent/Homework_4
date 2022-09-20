# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def check(number):
    is_simple = True
    for i in range(2, number - 1):
        if number % i == 0:
            is_simple = False
    return is_simple


#########################################################

start_number = int(input('Введите число: '))
_start_number = start_number

list_of_simple = []
result = []

for i in range(2, start_number):
    if check(i):
        list_of_simple.append(i)
    # print(list_of_simple)

start_number = _start_number
while start_number != 1:
    for i in range(0, len(list_of_simple)):
        if start_number % list_of_simple[i] == 0:
            result.append(list_of_simple[i])
            start_number = start_number // list_of_simple[i]
            # print(start_number)
            # print(result)
print(result)