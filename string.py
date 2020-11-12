функции и методы строк

 КОНКАНТЕНАЦИЯ(прибавление строк)

ДУБЛИРОВАНИЕ СТРОКИ(умножаем строки)

ДОСТУП ПО ИНДЕКСУ
S = 'hello world'
print(S[0]) #'s'

ИЗВЛЕЧЕНИЕ СРЕЗА(START:END:STEP)
s = 'spameggs'
print(s[3:5]) #'me'
print(s[2:-2]) #'ameg'
print(s[:6]) #'spameg'
print(s[1:]) #'pameggs'
print(s[:]) #'spameggs'
print(s[::-1]) #'sggemaps'

 При вызове методов необходимо помнить, что строки в Python относятся к категории неизменяемых последовательностей,
то есть все функции и методы могут лишь создавать новую строку.

 ***************** Таблица "Функции и методы строк" *********************
"""

S = 'str'; S = "str"; S = '''str'''; S = """str"""	# Литералы строк
S = "s\np\ta\nbbb" #	Экранированные последовательности
S = r"C:\temp\new" #	Неформатированные строки (подавляют экранирование)
S = b"byte" #	Строка байтов

string = 'string'
S.find(str) #([start],[end]) 	Поиск подстроки в строке. Возвращает номер первого вхождения или -1
S.rfind(str) #([start],[end])	Поиск подстроки в строке. Возвращает номер последнего вхождения или -1
S.index(str) #([start],[end])	Поиск подстроки в строке. Возвращает номер первого вхождения или вызывает ValueError
S.rindex(str) #([start],[end])	Поиск подстроки в строке. Возвращает номер последнего вхождения или вызывает ValueError
S.replace()(#шаблон, замена)	Замена шаблона
S.split()#(символ) Разбиение строки по разделителю
S.isdigit()	# Состоит ли строка из цифр
S.isalpha()	# Состоит ли строка из букв
S.isalnum() #	Состоит ли строка из цифр или букв
S.islower() #	Состоит ли строка из символов в нижнем регистре
S.isupper() #	Состоит ли строка из символов в верхнем регистре
S.isspace() #	Состоит ли строка из неотображаемых символов (пробел, символ перевода страницы ('\f'), "новая строка" ('\n'), "перевод каретки" ('\r'), "горизонтальная табуляция" ('\t') и "вертикальная табуляция" ('\v'))
S.istitle() #	Начинаются ли слова в строке с заглавной буквы
S.upper() #	Преобразование строки к верхнему регистру
S.lower() #	Преобразование строки к нижнему регистру
S.startswith(str) #	Начинается ли строка S с шаблона str
S.endswith(str) #	Заканчивается ли строка S шаблоном str
S.join(список) #	Сборка строки из списка с разделителем S

ord(символ) #	Символ в его код ASCII
chr(число) #	Код ASCII в символ

S.capitalize() #	Переводит первый символ строки в верхний регистр, а все остальные в нижний
S.center(width, [fill]) #	Возвращает отцентрованную строку, по краям которой стоит символ fill (пробел по умолчанию)
S.count(str, [start],[end]) #	Возвращает количество непересекающихся вхождений подстроки в диапазоне [начало, конец] (0 и длина строки по умолчанию)
S.expandtabs([tabsize]) #	Возвращает копию строки, в которой все символы табуляции заменяются одним или несколькими пробелами, в зависимости от текущего столбца. Если TabSize не указан, размер табуляции полагается равным 8 пробелам
S.lstrip([chars]) #	Удаление пробельных символов в начале строки
S.rstrip([chars]) #	Удаление пробельных символов в конце строки
S.strip([chars]) #	Удаление пробельных символов в начале и в конце строки
S.partition(шаблон) #	Возвращает кортеж, содержащий часть перед первым шаблоном, сам шаблон, и часть после шаблона. Если шаблон не найден, возвращается кортеж, содержащий саму строку, а затем две пустых строки
S.rpartition(sep) #	Возвращает кортеж, содержащий часть перед последним шаблоном, сам шаблон, и часть после шаблона. Если шаблон не найден, возвращается кортеж, содержащий две пустых строки, а затем саму строку
S.swapcase() #	Переводит символы нижнего регистра в верхний, а верхнего – в нижний
S.title()	# Первую букву каждого слова переводит в верхний регистр, а все остальные в нижний
S.zfill(width) #	Делает длину строки не меньшей width, по необходимости заполняя первые символы нулями
S.ljust(width, fillchar=" ") #	Делает длину строки не меньшей width, по необходимости заполняя последние символы символом fillchar
S.rjust(width, fillchar=" ") #	Делает длину строки не меньшей width, по необходимости заполняя первые символы символом fillchar
S.format(*args, **kwargs) #	Форматирование строки



ФОРМАТ СТРОК (на подобии конкантенации)
a = 'ada'
b = 'john'
print(f'hello {a} {b}')


МНОЖЕСТВЕННЫЕ ПРИСВАИВАНИЯ
а = 0
b = 1
a,b = 0,1