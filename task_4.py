#З дана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
#многочлена и записать в файл многочлен степени k.
#*Пример:*
#- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random
a = random.randint(0, 100)
b = random.randint(0, 100)
c = random.randint(0, 100)
print(a)
print(b)
print(c)
if a == 0:
    a1 = ''
else:
    a1 = str(a)+'*x^2'
if b == 0:
    b1 = ''
else:
    b1 = str(b)+'*x'
if c == 0:
    c1 = ''
else:
    c1 = str(c)
print(a1+'+'+b1+'+'+c1+'=0')

file5 = open('file5.1.txt', 'w+')
file5.write(a1+'+'+b1+'+'+c1+'=0')
print(*file5)