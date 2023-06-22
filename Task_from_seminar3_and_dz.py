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


#В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
#Не учитывать знаки препинания и регистр символов.
#За основу возьмите любую статью из википедии или из документации к языку.
import re
import pprint
text = 'Капибара, или водосвинка (Hydrochoerus hydrochoeris) является родственницей всем известной морской свинки и напоминает ее увеличенную в десятки раз копию./' \
       ' Это самый крупный представитель отряда грызунов на планете.' \
       ' Длина ее тела более 1 метра, высота в холке — выше полуметра, а живая масса тела от 50 до 75 килограммов (рекордная живая масса — 91 килограмм).' \
       ' Самки крупнее и тяжелее самцов. Своими размерами капибара напоминает молодую домашнюю свинью.' \
       ' Голова крупная, морда почти квадратная, ноздри широко расставлены, глаза и уши небольшие.' \
       ' В ротовой полости находится 20 зубов, резцы оранжевого цвета и растут всю жизнь.' \
       ' Тело бочкообразной формы, хвост рудиментарный.' \
       ' На передних конечностях по 4 пальца, на задних по 3 пальца.' \
       ' Между пальцами лап расположены плавательные перепонки.' \
       ' Задние конечности длиннее передних.'



my_dict = dict()

words = re.sub(r'\W', ' ', text).lower().split()

for word in words:
    if word in my_dict:
        my_dict[word] += 1
    else:
        my_dict[word] = 1



pprint.pprint(my_dict)