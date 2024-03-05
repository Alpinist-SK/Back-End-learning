#Магический квадрат – это квадратная таблица размера n х n, 
#составленная из всех чисел 1, 2, 3 … n2 таким образом, что 
#суммы по каждому столбцу, каждой строке и каждой диагонали 
#равны между собой. Напишем программу, которая определяет, 
#можно ли считать матрицу магическим квадратом.

def my_desicion(A, n):                          #Моё решение
    B = {j for i in A for j in i}
    
    if B == set(range(1, n ** 2 + 1)):   #Проверка, что матрица состоит из числе 1,2 ... n^2
        P1 = True
    else:
        return False
    
    P2 = True
    for i in range(n):                 #Проверка, что суммы всех строк равны                  
        P2 = P2 and sum(A[i]) == sum(A[0])

    P3 = True                        #Проверка, что суммы всех столбцов равны
    for j in range(n):     
        S = 0
        for k in range(n):
           S += A[k][j]
        P3 = P3 and S == sum(A[0]) 
   
    S1 = 0
    S2 = 0
    raz = 0
    for c in range(n):                      #Проверка что суммы диагоналей равны
        raz += 1
        for h in range(n):
            if c == h:
                S1 += A[c][h]
        S2 += A[c][n - raz] 
    P4 = True if S2 == S1 and S1 == sum(A[0]) else False
    return P1 and P2 and P3 and P4


def desicion1(A, n):                      #Решение с сайта
    m_const = n * (1 + n ** 2) // 2                                                      
    print(('NO', 'YES')[all(sum(el) == m_const for x in (((A[i][i] for i in range(n)),(A[i][~i] for i in range(n))), A, zip(*A)) for el in x) and set(sum(A, [])) == set(range(1, n ** 2 + 1))])

n = int(input('Введите число n: '))
print('\nВведите матрицу по строкам:')

A = []
for i in range(n):
    C = input().split(sep = ' ')
    C = [int(i) for i in C]
    A.append(C)

print("\n\n1.Моё решение.")
print("\nМатрица является магическим квадратом!" if my_desicion(A, n) == True else "\nМатрица НЕ является магическим квадратом!")

print("\n\n2. Решение с сайта.\n")
desicion1(A, n)