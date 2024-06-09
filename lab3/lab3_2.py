#(задача 2) Напишите программу, которая решает обратную задачу
#по отношению к заданию 1. Из строки типа  Y4g2ke3A3BV
#восстанавливает исходную.

s = input("введите символы: ")
count = 1
s_decoded = ""
s_convert = ""
s += "\0" #символ в конец строки для обработки последнего символа
for i in range(1, 25):
    #комбинация символ-множитель
    if (s[i-1].isalpha()) and (s[i].isdigit()):
        s_convert += ((s[i-1])*(int(s[i])))
        s_decoded += s_convert
        s_convert = ""
        i += 1
    #множитель-символ
    elif (s[i-1].isdigit()) and (s[i].isalpha()):
        i += 1
    #символ-символ
    elif (s[i-1].isalpha()) and (s[i].isalpha()):
        s_convert += s[i-1]
        s_decoded += s_convert
        s_convert = ""
        i += 1
print(s_decoded)
