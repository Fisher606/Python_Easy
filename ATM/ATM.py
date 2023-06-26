# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции - функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.

from ATM_Getting_money import get_money
from ATM_Giving_Money import give_money

amount_of_money = 0
operations_count = 0

while True:
    print ("1 - снять, 2 - пополнить, q - выйти")
    print ("Средства - ", amount_of_money)
    user_answer = input("Выберите действия ")
    if user_answer == '1':
        amount_of_money, operations_count = get_money(int(input("Сколько? ")), amount_of_money, operations_count)
    elif user_answer == '2':
        amount_of_money, operations_count = give_money(int(input("Сколько? ")), amount_of_money, operations_count)
    elif user_answer == 'q':
        print('До свидания!')
        break