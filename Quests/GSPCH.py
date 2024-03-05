#Генератор случайных чисел

from random import randint 

def valid_number(number):   
    
    if number.isdigit() == True and int(number) > 0:
        return True
    
    else:    
        return False
 

def print_result(spis) -> str:
    
    spis = sorted(spis)
    res = ''
    
    for i in spis:
        res += str(i) + ' '
        
    return res



print('Добро пожаловать в генератор случайных чисел! \n\nВведите первое число диапозона.')


x = input()

while valid_number(x) != True:
    print('\nНеккоректное значение! Введите целое число больше нуля.')
    x = input()
    

print('\nВведите второе число диапозона.')

y = input()

while valid_number(y) != True or int(y) < int(x):
    if valid_number(y) != True:
        print('\nНеккоректное значение! Введите целое число больше нуля.')
    elif int(y) < int(x):
        print('\nНеккоректное значение! Второе число диапазона не может быть меньше первого.')
    y = input()
    

print('\nСколько чисел нужно сгенирировать?')

n = input()

while valid_number(n) != True or int(n) > int(y) - int(x) + 1:
    if valid_number(n) != True:
        print('\nНеккоректное значение! Введите целое число больше нуля.')
    elif int(n) > int(y) - int(x) + 1:
        print('\nНеккоректное значение! Количество сгенирированных чисел не может быть больше \nколичества чисел в заданном диапазоне.')
    n = input()
        
        
index1 = 1
num = 0
result = []

while index1 <= int(n):                               #Генерация случайных чисел
    num = randint (int(x), int(y))
    if num not in result:
        result.append(num)
        index1 += 1
    
    
print(f"\nСлучайные числа: {print_result(result)}")