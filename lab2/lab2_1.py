#(задача 1) Напишите программу, которая выводит n строк треугольника Паскаля.
# Число n вводится с клавиатуры.

print("num of rows: ")
n = input()
T = []

for i in range(int(n)):
    row = [1]*(i+1)
    for j in range (i+1):
        if (j != 0) and (j != i):
            row[j] = T[i-1][j-1] + T[i-1][j]
    T.append(row)
for k in T:
    print(k)
