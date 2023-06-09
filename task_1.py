# Задача 30: Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии

a = int(input("Enter a: "))
n = int(input("Enter n: "))
d = int(input("Enter d: "))

my_list = []

while n != 0:
    result = a + (n - 1) * d
    my_list.append(result)
    n -= 1
print(sorted(my_list))