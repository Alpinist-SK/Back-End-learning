#Это вариант классической задачи Иосифа Флавия. В кругу стоят n человек, 
#пронумерованных числами от 1 до n. Начинается расчет, при котором 
#каждый k-й по счету человек выбывает из круга, после чего счет 
#продолжается со следующего за ним человека. 
#Напишите программу, определяющую номер человека, 
#который останется в кругу последним.
import copy

def my_decision(n, k):            #Моё решение
    peoples = [i for i in range(1, n + 1)]
    survivors = []
    c = 1                  #индексная переменная
    while len(peoples) > 1:
        survivors.clear()
        for j in peoples:
            if c % k != 0:
                survivors.append(j)
            c += 1
        peoples = copy.deepcopy(survivors)
    return str(peoples)[1 : -1]


def decision1(n, k):                   #Кротчайшее решение
    last = 0
    for i in range(1, n + 1):
        last = (last + k) % i
    return last + 1


def decision_rec(n, k):              #Решение с помощью рекурсии
    if n == 1:
        return 1
    elif n > 1:
        return((decision_rec(n - 1, k) + k) % n)
    


n, k = map(int, input("Введите n и k в (в формате: n, k): ").split(sep = ", "))   #Ввод значений n и k

    
print('\n\n1. Моё решение:')
print(f'\nПоследний выживший из {n} при убийстве каждого {k}-го: {my_decision(n, k)}-й')

print('\n\n2. Самое короткое решение:')
print(f'\nПоследний выживший из {n} при убийстве каждого {k}-го: {decision1(n, k)}-й')

print('\n\n3. Решение с помощью рекурсии:')
print(f'\nПоследний выживший из {n} при убийстве каждого {k}-го: {decision1(n, k)}-й')


