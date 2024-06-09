#(задача 2) Напишите программу, в которой с помощью псевдографики
#состоящей из звездочек * выводится треугольник Серпинского
#Реализовать минимум 3 итерации, приняв за минимально возможный
#треугольник состоящий из 3 *

import functools
n = int(input("размер треугольника: (рекомендуется <= 5) "))

def serp(n):

    def tri(t, i):
       space = " " * (2**i)
       return [space + x + space for x in t] + [x + " " + x for x in t]

    return functools.reduce(tri, range(n), ["*"])

print("\n".join(serp(n)))
