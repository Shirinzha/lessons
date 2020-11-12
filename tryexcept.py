# try:
#     number = int(input("Введите число: "))
#     print("Введенное число:", number)
# except:
#     print("Преобразование прошло неудачно")

# print("Завершение программы")





# try:
#    number = int(input('Enter number: '))
#    result = 100/number
#    print(result)
# except ZeroDivisionError:
#    print('Exception cathced')
# except ValueError:
#    print('Value Error')





# try:
#     number = int(input("Введите число: "))
#     print("Введенное число:", number)
# except ValueError:
#     print("Преобразование прошло неудачно")
# print("Завершение программы")








# while True:
#     try:
#         number1 = int(input("Введите первое число: "))
#         number2 = int(input("Введите второе число: "))
#         print("Результат деления:", number1/number2)
#     except ValueError:
#         print("Преобразование прошло неудачно")
#     except ZeroDivisionError:
#         print("Попытка деления числа на ноль")
#     except Exception:
#         print("Общее исключение")
#     print("Завершение программы")








# #####    Блок finally   #####

# '''
# При обработке исключений также можно использовать необязательный блок finally. Отличительной особенностью этого блока является то, что он выполняется вне зависимости, было ли сгенерировано исключение:
# '''

# try:
#     number = int(input("Введите число: "))
#     print("Введенное число:", number)
# except ValueError:
#     print("Не удалось преобразовать число")
# finally:
#     print("Блок try завершил выполнение")
# print("Завершение программы")

# '''
# Как правило, блок finally применяется для освобождения используемых ресурсов, например, для закрытия файлов.
# '''










# #####   Получение информации об исключении   #####

# '''
# С помощью оператора as мы можем передать всю информацию об исключении в переменную, которую затем можно использовать в блоке except:
# '''

# try:
#     number = int(input("Введите число: "))
#     print("Введенное число:", number)
# except ValueError as e:
#     print("Сведения об исключении", e)
# print("Завершение программы")







# #####    Генерация исключений   #####

# '''
# Иногда возникает необходимость вручную сгенерировать то или иное исключение. Для этого применяется оператор raise.
# '''

# try:
#     number1 = int(input("Введите первое число: "))
#     number2 = int(input("Введите второе число: "))
#     if number2 == 0:
#         raise Exception("Второе число не должно быть равно 0")
#     print("Результат деления двух чисел:", number1/number2)
# except ValueError:
#     print("Введены некорректные данные")
# except Exception as e:
#     print(e)
# print("Завершение программы")








