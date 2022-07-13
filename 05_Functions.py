# ~ Создайте функцию печати элементов списка, делящихся на 5
def function_list(numbers):
    for number in numbers:
        if number%5==0:
            print(number, end=' ')
    print("")    
numbers=[2,35,152,71,112,215,7,116,16]
# ~ Напишите код выполнения созданной функции
print("Числа, которые делятся на 5 без остатка:")
function_list(numbers)

print("")

# ~ Создайте функцию простого поиска и возвращения минимального элемента 
# ~ в списке
def get_min_simple(numbers):
    m=numbers[0]
    for number in numbers:
        if number<m:
            m=number
    return m
# ~ Напишите код выполнения созданной функции
numbers=[2,35,152,71,112,215,7,116,16]
my_min=get_min_simple(numbers)
print("Минимальный элемент в списке равен:")
print(my_min)

print("")

# ~ Создайте функцию поиска в списке первого элемента, меньшего my_value
def get_first_exceed(numbers, my_value):
    for number in numbers:
        if number<my_value:
            print("Первое значение в списке меньше заданного:",number)
            break
    else:
        print("Элемент не найден")
numbers=[2,35,152,71,112,215,7,116,16]
# ~ Напишите код выполнения созданной функции
get_first_exceed(numbers, 3)
