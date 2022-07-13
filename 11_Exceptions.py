
# ~ Создайте и выполните функцию с блоком try - except обрабатывающим 
# ~ попытку распечатать несуществующую переменную.
def variable_print():
    try:
        print(vp)
    except Exception as e:
        print(e)

# ~ Создайте и выполните функцию перевода списка строк в список целых 
# ~ чисел с блоком try - except, обрабатывающим ошибки преобразования.
# ~ В случае ошибки выводить сообщение на экран и не добавлять новый 
# ~ элемент в итоговый список.        
def process_print_list(inputs):
    for my_input in inputs:
        try:
            print(int(my_input))
        except Exception as e:
            print(e)
            # ~ break

# ~ Создайте и выполните функцию с блоком try - except - finally, 
# ~ обрабатывающим попытку записать строку в файл, открытый на чтение. 
# ~ В блоке finally выполнить закрытие файла.
def process_open_file():
        try:
            f=open("demofile.txt","r")
            f.write("Привет!")
        except:
            print("Ошибка записи в файл")
        else:
            print('Ошибок нет')
        finally:
            f.close()
            print('Файл закрыт') 
        
# ~ Точка входа в программу
def main():
    variable_print()
    print("")
    numbers=['2','3','Hello','7','-11','16','7','0','22']
    process_print_list(numbers)
    print("")
    process_open_file()
    return 0

if __name__ == '__main__':
    main()
