# choice = "y"

# while choice.lower() == "y":
#     print("Привет")
#     choice = input("Для продолжения нажмите Y, а для выхода любую другую клавишу: ")
# print("Работа программы завешена")







Программа по вычислению факториала
# number = int(input("Введите число: "))
# i = 1
# factorial = 1
# while i <= number: 
#     factorial *= i
#     i += 1
#     print('This time i is:', i)
#     print('Factorial = ', factorial)
# print("Факториал числа", number, "равен", factorial)










Программа по вычислению факториала
# number = int(input("Введите число: "))
# factorial = 1
# for i in range(1, number+1):
#     factorial *= i
#     print(f'factorial = {factorial}')
# print("Факториал числа", number, "равен", factorial)








Примеры вызовов функции range:
# print(list(range(5)))     
# print(list(range(1, 5)))   
# print(list(range(2, 10, 2)))
# print(list(range(5, 0, -1)))

Например, выведем последовательно все числа от 0 до 4:
# for i in range(5):
#     print(i)






Одни циклы внутри себя могут содержать другие циклы. Рассмотрим на примере вывода таблицы умножения:
# for i in range(1, 10):
#     for j in range(1, 10):
#         print(i * j, end="\t")
#     print("\n")








Программа Обменный пункт
# print("Для выхода нажмите Y")
 # while True:
#     data = input("Введите сумму для обмена: ")
#     if data.lower() == "y":
#         break  # выход из цикла
#     money = int(data)
#     cache = round(money / 69.7, 2)
#     print("К выдаче", cache, "долларов")
# print("Работа обменного пункта завершена")






Программа Обменный пункт
# print("Для выхода нажмите Y")
# while True:
#     data = input("Введите сумму для обмена: ")
#     if data.lower() == "y":
#         break  # выход из цикла
#     money = int(data)
#     if money < 0:
#         print("Сумма должна быть положительной!")
#         continue
#     cache = round(money / 69.7, 2)
#     print("К выдаче", cache, "долларов")
# print("Работа обменного пункта завершена")







# for n in range(2, 10):
#     for x in range(2, n):
#         if n % x == 0:
#             print(n, 'equals', x, '*', n//x)
#             break
#     else:
#         # цикл потерпел неудачу, не найдя множитель
#         print(n, 'is a prime number')

# print(list(range(2, 3)))







