#(задача 2.1) Напишите программу, в которой задается  натуральное число n и выводится 
#лестница из n ступенек, i-я ступенька должна состоять из чисел от 1 до i без пробелов

n = int(input("number of repeats n:"))
k=i=1

for i in range(1, n+1):
    for k in range(1,i+1):
        print(k, end=' ')
    print("")
