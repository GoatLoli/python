#(задача 2.2)Напишите программу, в которой задается натуральное число n и выводится пирамида из 
#n ступенек, i-я ступень должна состоять из чисел от 1 до i и обратно без пробелов.

n = int(input("number of repeats n:"))

for i in range(1, n+1):
    print("".join(str(x) for x in range(1, i + 1)) + \
          "".join(str(x) for x in range(i - 1, 0, -1)))
