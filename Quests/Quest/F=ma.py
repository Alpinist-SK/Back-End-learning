def check_float(text: str) -> bool:   #Функция для проверки на возможность преобразования в float
    try:
        float(text)
        return(True)
        
    except ValueError:
        return(False)
    

print('''Сила - это произведение массы на ускорение (F = ma)
                    
Введите массу m (kg):''')

m = input()

while  check_float(m) == False or float(m) < 0:                   #Валидация значения массы
    print ('''\nНекорректное значение! Масса должна быть числом, которое больше или равно нулю.\n\nВведите массу m (kg):''')
    m = input()

if float(m) == 0:
    F: float = 0.0
    
else:
    print('\nВведите ускорение (м/c^2):')
    a = input()
    
    while  check_float(a) == False:                                   #Валидация значения ускорение
         print ('\nНекорректное значение! Ускорение должно быть числом.\n\nВведите ускорение (м/c^2):')
         a = input()
    
    F: float = float(m)*float(a)
    

print(f'\nСила: F = {F} (Н)')