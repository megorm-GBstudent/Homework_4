#Вычислить число π c заданной точностью d
#*Пример:*
#- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

n = 1
sum = 0
for i in range(10000000):
    if i % 2 == 0:
        sum += 4/n
    else:
        sum -= 4/n
    n += 2
print(sum)








