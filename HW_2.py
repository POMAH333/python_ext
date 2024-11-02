'''
1. Решить задачи, которые не успели решить на семинаре.
'''

'''
2. Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата.
'''

num = int(input('Введите целое число: '))

transform = num
hex_str = ''
while transform > 0:
  remains = transform % 16
  if remains < 10:
    hex_str = str(remains) + hex_str
  elif remains == 10:
    hex_str = 'a' + hex_str
  elif remains == 11:
    hex_str = 'b' + hex_str
  elif remains == 12:
    hex_str = 'c' + hex_str
  elif remains == 13:
    hex_str = 'd' + hex_str
  elif remains == 14:
    hex_str = 'e' + hex_str
  else:
    hex_str = 'f' + hex_str
  transform //= 16

hex_str = '0x' + hex_str
print(f'Шестнадцатеричное представление: {hex_str}')
print(f'Проверка: {hex(num)}')


print('')
print('')
print('')
'''
3. Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions
'''

from fractions import Fraction

fract_1 = str(input('Введите первую дробь: '))
fract_2 = str(input('Введите вторую дробь: '))

split_fract_1 = fract_1.split('/')
split_fract_2 = fract_2.split('/')

num_1 = int(split_fract_1[0])
den_1 = int(split_fract_1[1])
num_2 = int(split_fract_2[0])
den_2 = int(split_fract_2[1])

sum_num = int(num_1 * den_2 + num_2 * den_1)
sum_den = int(den_1 * den_2)

comp_num = int(num_1 * num_2)
comp_den = int(den_1 * den_2)

gcd = sum_num
reduce = sum_den
while reduce != 0:
  gcd, reduce = reduce, gcd % reduce

sum_num //= gcd
sum_den //= gcd

gcd = comp_num
reduce = comp_den
while reduce != 0:
  gcd, reduce = reduce, gcd % reduce

comp_num //= gcd
comp_den //= gcd

print(f'Сумма: {int(sum_num)}/{int(sum_den)}')
print(f'Произведение: {int(comp_num)}/{int(comp_den)}')
print(f'')
print('Проверка')
x = Fraction(fract_1)
y = Fraction(fract_2)
print(f'Сумма: {x + y}')
print(f'Произведение: {x * y}')