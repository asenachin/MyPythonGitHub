print("Управляющие структуры")
print("")

do_print=True
do_print=False
if do_print:
    print("Условие выполнено")
print("После условия")
print("")

is_sql_connection=True
is_sql_connection=False
if is_sql_connection:
    print("Есть соединение")
else:
    print("Соединение отсутствует")
print("")

sql_server="MS SQL"
sql_server="MySQL"
if sql_server=="MS SQL":
    print("Microsoft SQL Server")
elif sql_server=="MySQL":
    print("MySQL Server")
elif sql_server=="SQLite":
    print("SQLite Server")
else:
    print("SQL сервер не найден")
print("")

if a%2==0:
    print("a четное")
else:
    print("a нечетное")    
print("")


# ~ Сравнение двух целочисленных переменных
print("Сравнение двух целочисленных переменных")
x=input("Введите первое целое число x? ")
y=input("Введите второе целое число y? ")
if x==y:
    print("Числа равны")
elif x>y:
    print("x больше y")
elif x<y:
    print("x меньше y")
else:
    print("Не должно быть напечатано")
print("")

# ~ Определение делимости числа на 3
print("Определение делимости числа на 3")
a=input("Введите натуральное число? ")
print('Тип введённого значения всегда будет ',type(a))
a=int(a) # преобразуем 'str' в 'int'
if a % 3==0:
    print("Делится без остатка")
else:
    print("Делится с остатком")    
print("")

# ~ Сравнение двух логических переменных
x=bool(input("Введите 1 (true) или <Enter> (false)? "))
y=bool(input("Введите ещё раз 1 (true) или <Enter> (false)? "))
print("x=",x)
print("y=",y)
if x==False and y==False:
    print("False=2")
elif x==False and y==True:
    print("False=1")
elif x==True and y==False:
    print("False=1")
elif x==True and y==True:
    print("False=0")
else:
    print("Значения логических переменных не равны True или False")
print("")

# ~ Сравнение двух логических переменных вариант №2
x=input("Введите True или False? ")
y=input("Введите ещё раз True или False? ")
if x=="False" and y=="False":
    print("False=2")
elif x=="False" and y=="True":
    print("False=1")
elif x=="True" and y=="False":
    print("False=1")
elif x=="True" and y=="True":
    print("False=0")
else:
    print("Значения логических переменных не равны True или False")

