print(123)
print(123)
print(123)
test = 5
test2 = "sokol"
asdasd = 5

# Переменные

# int (integer) - это целочисленное число 
number = 5

#float - это вещественное число (дробь)
fnumber = 5.7

# str (string) - строка
name = "Sokol"
age = 55

# bool
status = True

# вывод комментарий
# можно писать что угодно

# Функция вывода (текст указывается в кавычках, переменная например status без кавычек)
print( "Что нужно вывести" )

# Экранирование (если нужно выделить какое-то слово кавычками, нужно около этого слова в двух сторон поставить слэш \" )
print( "Он \"плохой\" человек!")

# Не нужно экранировать в случае
print( 'Он "плохой" человек!' )

# Перенос строки
print( 'Привет \nмир!' )


# Конкатенация (происходит склеивание нижеуказанной строки с переменной name),
print( 'Привет, меня зовут ' + name + "!" )

# в python запрещено конкатенировать разные типы данных, например строка и число, будет выдаваться ошибка
# print( 'Мне' + age + " года!" )

# надо перевести число в строковую переменную
print( "Мне " + str(age) + " лет!" )

# input выводит строку, неважно что это целочисленное или дробь:
# name = input( "Введите свое имя: " )
# age = input( "Укажите свой возраст: " )

# print( "Привет, " + name + "!" )
# print( "Тебе уже , " + age + " лет, это круто!!! =D" )

# Базовые операции: +, -, *, /, ** (возведение в степень), 
# % (по модулю, тоже что и деление только возвращается остаток) унарный минус, округление, ПИ

a = 5
b = 10

c = a + b
d = a * b
f = b/a
g = a ** 2
c1 = b % 3
print( c )
print( d )
print( f )
print( g )
print( c1 )

# унарный минус
a = 10

# К переменной а присваиваем саму себя, только с унарным минусом
# унарный минус меняет знак числа, добавляет минус, и наоборот
a = -a
a = -a

print( a )

# округление
a = 5.65

print( round(a) )

import math

a = 5.65

# floor - это функция принудительного округления в меньшую сторону
print( math.floor(a) )

# ceil - это функция принудительного округления в большую сторону
print( math.ceil(a) )

# ПИ

print( math.pi )



