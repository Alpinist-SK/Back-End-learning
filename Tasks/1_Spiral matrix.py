#На вход программе подаются два натуральных числа n и m. 
#Напишите программу, которая создает матрицу размером n х m, 
#заполнив ее по спирали числами от 1 до n x m. Спираль начинается 
#левом верхнем углу и закручивается по часовой стрелке.

def show_matrix(A):                               #Функция для отображения матрицы
    strmax = []
    for a in A:
        strmax.append(max(a))
    mmax = max(strmax)
    for i in range(len(A)):
        for j in range(len(A[i])):
            print(A[i][j], end = " " * (len(str(mmax)) + 1 - len(str(A[i][j]))))
        print()


def my_decision(a, b):
    result = [[0 for i in range(b)] for j in range(a)] #Формируем пустую матрицу
    ymax = len(result)       #Верхняя граница пустых значений в столбце
    xmax = len(result[0])    #Верхняя граница пустых значений в строке
    xmin = 0        #Нижняя граница пустых значений в строке
    ymin = 0        #Нижняя граница пустых значений в столбце
    x = 0          #Текущий индекс стобца
    y = 0          #Текущий индекс строки
    i = 1          #Текущее значение

    while i <= nm:
        for j in range(x, xmax):
            result[y][j] = i
            i += 1
            x += 1
        x -= 1 #Коррекция
        y += 1
        ymin += 1
   
        for k in range(y, ymax):
            result[k][x] = i
            i += 1
            y += 1
        y -= 1
        xmax -= 1

        for c in reversed(range(xmin, x)):
            result[y][c] = i
            i += 1
            x -= 1
        ymax -= 1

        for t in reversed(range(ymin, y)):
            result[t][x] = i
            i += 1
            y -= 1
        xmin += 1
        x += 1

    return result

def decision1(a, b):
    result = [[0 for i in range(b)] for j in range(a)] #Формируем пустую матрицу
    dx, dy, x, y = 0, 1, 0, 0

    for i in range(1, a * b + 1):
        result[x][y] = i
        if result[(x + dx) % a][(y + dy) % b]:

            dx, dy = dy, -dx
        x += dx
        y += dy
    return result

def decision2(a, b):
    result = [[0 for i in range(b)] for j in range(a)] #Формируем пустую матрицу
    x, y, dx, dy = 0, 0, 1, 0
    
    for i in range(1, a * b + 1):
        result[y][x] = i
        nx, ny = x + dx, y + dy
        if 0 <= nx < b and 0 <= ny < a and result[ny][nx] == 0:
            x, y = nx, ny
        else:
            dx, dy = -dy, dx
            x, y = x + dx, y + dy
    return result


a, b = input("Введите два натуральных числа n и m (Формат: n, m): ").split(sep = ", ")      #Вводим значение

a = int(a)
b = int(b)
nm = a * b

print('\n1. Моё решение:')
show_matrix(my_decision(a, b))

print('\n2. Решение N1:')
show_matrix(decision1(a, b))

print('\n3. Решение N2:')
show_matrix(decision2(a, b))