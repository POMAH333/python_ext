# 1. Напишите функцию для транспонирования матрицы
from re import match

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

print("исходная матрица:\n", matrix)


def matrix_transposition(matrix):
    print([[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))])


print("транспонированная матрица:")
matrix_transposition(matrix)


# 2. Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.


def kwargs_to_dict(**kwargs):
    result = {}
    for key, value in kwargs.items():
        try:
            result[value] = key
        except:
            result[str(value)] = key
    return result


print(kwargs_to_dict(bananas=23, apples=(234, 345), peaches=[234, 3456, 567]))

# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.
# Начальная сумма равна нулю
# Допустимые действия: пополнить, снять, выйти
# Сумма пополнения и снятия кратны 50 у.е.
# Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# После каждой третей операции пополнения или снятия начисляются проценты - 3%
# Нельзя снять больше, чем на счёте
# При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# Любое действие выводит сумму денег

MULTIPLICITY_FACTOR = 50
WITHDRAWAL_PERCENT = 0.015
WITHDRAWAL_MIN = 30
WITHDRAWAL_MAX = 600
OPERATIONS_FIX = 3
OPERATIONS_PERCENT = 0.03
BALANCE_MAX = 5000000
KING_TAX = 0.1

client_balance: int = 0
operations_counter = 0
history_list = []


def deposit_account(acc_balance, operation_count, operation_list):
    deposit_amount = int(input(f'Введите сумму пополнения, кратную {MULTIPLICITY_FACTOR}: '))
    if deposit_amount > 0 and deposit_amount % MULTIPLICITY_FACTOR == 0:
        acc_balance += deposit_amount
        operation_list.append(deposit_amount)
    else:
        print(f'Сумма пополнения не кратна {MULTIPLICITY_FACTOR}')
    print(f'Баланс вашего счета: {acc_balance}')
    operation_count += 1
    return acc_balance, operation_count, operation_list


def withdraw_account(acc_balance, operation_count, operation_list):
    withdraw_amount = int(input(f'Введите сумму снятия, кратную {MULTIPLICITY_FACTOR}: '))
    if withdraw_amount % MULTIPLICITY_FACTOR == 0:
        percent = client_balance * WITHDRAWAL_PERCENT
        if percent < WITHDRAWAL_MIN:
            percent = WITHDRAWAL_MIN
        elif percent > WITHDRAWAL_MAX:
            percent = WITHDRAWAL_MAX
        if withdraw_amount + percent > acc_balance:
            print('Недостаточно средств на счету')
        else:
            acc_balance -= withdraw_amount + percent
            operation_list.append(int(- withdraw_amount - percent))
    else:
        print(f'Сумма снятия не кратна {MULTIPLICITY_FACTOR}')
    print(f'Баланс вашего счета: {acc_balance}')
    operation_count += 1
    return acc_balance, operation_count, operation_list


def check_balance():
    global client_balance
    global operations_counter
    global history_list
    if client_balance > BALANCE_MAX:
        tax = client_balance * KING_TAX
        client_balance -= tax
        print(f'Баланс вашего счета после снятия налога на операцию: {client_balance}')
        history_list.append(int(-tax))
    if operations_counter % OPERATIONS_FIX == 0 and operations_counter != 0:
        interest = client_balance * OPERATIONS_PERCENT
        client_balance += interest
        print(f'Баланс вашего счета после начисления процентов: {client_balance:}')
        history_list.append(int(-interest))


def menu():
    global client_balance
    global operations_counter
    global history_list
    actions = input(f'Для работы с банкоматом выберите действие:\n1 - Пополнить\n2 - Снять\n3 - История операций\n4 - '
                    f'Выйти\n')
    if actions == '1':
        check_balance()
        client_balance, operations_counter, history_list = deposit_account(client_balance, operations_counter,
                                                                           history_list)
        menu()
    if actions == '2':
        check_balance()
        client_balance, operations_counter, history_list = withdraw_account(client_balance, operations_counter,
                                                                            history_list)
        menu()
    if actions == '3':
        check_balance()
        print(f'История операций: {history_list}')
    if actions == '4':
        check_balance()
        print(f'Баланс вашего счета: {client_balance}')


menu()
