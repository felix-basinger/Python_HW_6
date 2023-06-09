# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.

from random import randint

list_length = int(input("Enter the length of your array: "))

my_list = [randint(1, 5) for i in range(list_length)]
st = set(my_list)
new_list = list(st)

dct = {}
count = 0
for i in new_list:
    dct[i] = count

for i in my_list:
    for k, v in dct.items():
        if i == k:
            dct[i] = v + 1

for k, v in dct.items():
    if v == 2:
        count += 1
    elif v % 2 == 0 and v > 2:
        res = v / 2
        count += res
    elif v % 2 != 0 and v > 2:
        res_2 = v - 1
        if res_2 % 2 == 0 and res_2 > 2:
            res_2 = v / 2
            count += res_2
        elif res_2 == 2:
            count += 1

print(my_list)
print(dct)
print(int(count))
