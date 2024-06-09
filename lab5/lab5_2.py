#(задача 2) Дан файл в котором записаны в столбик
#(каждое на отдельной строке) целые числа, всего 10 чисел.
#Отсортировать их по возрастанию цифр и записать в другой файл

with open('5_2inp.txt') as file1:
    s = file1.read()
s = s.split('\n')
#print(s)
for i in range(len(s)):
    s[i] = int(s[i])
s.sort()
#print(s)
file2 = open('5_2outp.txt','w')
file2.write(str(s))
file2.close()

#проверка
file2 = open('5_2outp.txt')
print(file2.read())
file2.close()
