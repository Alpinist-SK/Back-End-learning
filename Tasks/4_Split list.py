#На вход подается строка чисел, из которой формируется список. 
#Напишите программу, создающую вложенный список, элементами 
#которого являются все возможные подсписки исходного списка, включая пустой.


spis_str = input("Введите исходный список:\n").split(sep = " ")   #Ввод данных
spis = []
for i in range(len(spis_str)):
    spis += [int(spis_str[i])]
print(f"\nИсходный список: {spis}")

def my_decision(sp):                  #Моё решение
    result = [[j] for j in sp]
    result.insert(0, [])
    for k in range(len(sp) - 1):
        for c in range(k + 1, len(sp)):
            result.append(sp[k : c + 1])
    return sorted(result, key = len)


def dicision1(sp):
    print([[]] + [lst[j:i + j + 1] for lst in [sp] for i in range(len(lst)) for j in range(len(lst) - i)])



print("\n\n1. Моё решение.")
print(f"\nСписок включаящий в себя все подсписки исходного:\n{my_decision(spis)}")

print("\n\n2. Решение с сайта.\n")
dicision1(spis)


