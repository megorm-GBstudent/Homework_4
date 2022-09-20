#Задайте последовательность чисел. Напишите программу, которая выведет список
#неповторяющихся элементов исходной последовательности.

start_message = input('введите числа через пробел: ')   # задаём список чисел
print('start_message: ', start_message)
list_of_strings = start_message.split()
print(list_of_strings)
list_of_nums = []
for num in list_of_strings:
    list_of_nums.append(int(num))
print(list_of_nums)

def get_unique_numbers(numbers):   # вводим функцию которая будет выделять уникальные числа
    unique_numbers = set(numbers)   # функция set ищет уникальные числа из списка
    return unique_numbers

print(get_unique_numbers(list_of_nums))




