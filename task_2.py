# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.
from random import randint

list_length = int(input("Enter the length of your array: "))
my_list = [randint(1, 5) for i in range(list_length)]
count = 0

for i in range(len(my_list) - 2):
    if my_list[i] < my_list[i + 1] > my_list[i + 2]:
        count += 1

print(my_list)
print(count)
