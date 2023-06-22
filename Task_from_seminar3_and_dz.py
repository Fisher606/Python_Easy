#Дан список повторяющихся элементов.
#Вернуть список с дублирующимися элементами.
#В результирующем списке не должно быть дубликатов.

from random import randint
numbers = []
for i in range(10):
    numbers.append(randint(1, 6))

new_list = []
for elem in set(numbers):
    if numbers.count(elem) > 1:
        new_list.append(elem)

res = [*set(numbers)]

print("Список с повторяющимися элементами", f'{numbers}')
print("Список дубликатов", f'{new_list}')
print("Список без дубликатов", f'{res}')


