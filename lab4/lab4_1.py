#(задача 1) Допишите программу, которая принимает
#список чисел и, с помощью множеств, определяет
#количество различных чисел внутри списка

s = set(input())
space = " "
s = s.difference(space)
#print(s)
print("кол-во разных чисел:", len(s))