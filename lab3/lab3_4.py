#(задача 4) Напишите программу, которая принимает список
#строк и выводит количество повторений данных строк в списке
#Необходимо реализовать решение с использованием словарей

spisok = ['aaa', 'abc', 'abcd', 'aaa', 'abc', 'abc', 'ddd']
for i in range(len(set(spisok))):
    count = 0
    check = spisok[0]
    for j in range(0, len(spisok)):
        if spisok[0] == spisok[j]:
            count += 1
    print(count)
    
    while check in spisok:
        spisok.remove(check)
