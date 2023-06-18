# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение * дробей.
# Для проверки своего кода используйте модуль fractions.

import fractions

num_1, denum_1 = map(int, input('Введите первую дробь вида a/b: ').split("/"))
num_2, denum_2 = map(int, input('Введите вторую дробь вида a/b: ').split("/"))

mult_1 = num_1 * num_2
mult_2 = denum_1 * denum_2
sum_mult = num_1 * denum_2 + num_2 * denum_1
mult_3 = denum_1 * denum_2

print(mult_1, mult_1, sum_mult, mult_3)

#Сейчас будет проверочка с помощью модулька fractions

from fractions import Fraction as frac

fr_1 = fractions.Fraction(num_1, denum_1)
fr_2 = fractions.Fraction(num_2, denum_2)
a = num_1 * num_2
b = denum_1 * denum_2
c = num_1 * denum_2 + num_2 * denum_1
d = denum_1 * denum_2

print(a , b , c , d)
