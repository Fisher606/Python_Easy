#Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
#Программа должна подсказывать «больше» или «меньше» после каждой попытки.

import random

print("Я загадаю число от 1 до 1000, у тебя 10 попыток что бы угадать, я немного подскажу")

num = random.randint(1,1000)

a = int(input(f"Первая попытка  "))
if a == num :
        print(f"Тьфу угадал, это было число {num}")
        quit()
elif a < num :
        print("Подсказка -> Больше")
elif a > num:
        print("Подсказка -> Меньше")

b = int(input(f"Вторая попытка  "))
if b == num :
        print(f"Тьфу угадал, это было число {num}")
        quit()
elif b < num :
        print("Подсказка -> Больше")
elif b > num:
        print("Подсказка -> Меньше")

с = int(input(f"Третья попытка  "))
if с == num :
        print(f"Тьфу угадал, это было число {num}")
        quit()
elif с < num :
        print("Подсказка -> Больше")
elif с > num:
        print("Подсказка -> Меньше")

d = int(input(f"Попытка № 4 "))
if d == num :
        print(f"Тьфу угадал, это было число {num}")
        quit()
elif d < num :
        print("Подсказка -> Больше")
elif d > num:
        print("Подсказка -> Меньше")

f = int(input(f"Попытка № 5 "))
if f == num :
        print(f"Тьфу угадал, это было число {num}")
        quit()
elif f < num :
        print("Подсказка -> Больше")
elif f > num:
        print("Подсказка -> Меньше")

g = int(input(f"Попытка № 6 "))
if g == num :
        print(f"Тьфу угадал, это было число {num}")
        quit()
elif g < num :
        print("Подсказка -> Больше")
elif g > num:
        print("Подсказка -> Меньше")

k = int(input(f"Попытка № 7 "))
if k == num :
        print(f"Тьфу угадал, это было число {num}")
        quit()
elif k < num :
        print("Подсказка -> Больше")
elif k > num:
        print("Подсказка -> Меньше")

j = int(input(f"Попытка № 8 "))
if j == num :
        print(f"Тьфу угадал, это было число {num}")
        quit()
elif j < num :
        print("Подсказка -> Больше")
elif j > num:
        print("Подсказка -> Меньше")

x = int(input(f"Попытка № 9 "))
if x == num :
        print(f"Тьфу угадал, это было число {num}")
        quit()
elif x < num :
        print("Подсказка -> Больше")
elif x > num:
        print("Подсказка -> Меньше")

z = int(input(f"Последний шанс "))
if z == num :
        print(f"Тьфу угадал, это было число {num}")
        quit()
elif z < num :
        print("Подсказка -> Больше")


print(f"Ты не смог отгадать число, я загадал цифру {num}")