#(задача 1) Считать из файла input.txt 10 чисел
#(числа записаны через пробел). Затем записать их
#произведение в файл output.txt.

proizv = 1
with open('input.txt') as file1: #закрывает файл автоматически
    s = file1.read()
s = s.split(' ')
for i in range(len(s)):
    proizv *= int(s[i])
#print(s, proizv)
file2 = open('output.txt','w')
file2.write(str(proizv))
file2.close()#обязательно

#проверка
file2 = open('output.txt')
print(file2.read())
file2.close()
