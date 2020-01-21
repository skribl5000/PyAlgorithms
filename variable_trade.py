# обмен переменных
a = 1
b = 2
print(a, b)
# 1 доп переменная
temp = a
a = b
b = temp
print(a, b)
# 2 additional variable
temp1 = a
temp2 = b
b = temp1
a = temp2
print(a, b)
# создание двух кортежей, которым присваиваются соответствующие значения - происходит быстрее
a, b = b, a
print(a, b)
