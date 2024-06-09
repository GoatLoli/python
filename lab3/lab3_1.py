#(задача 1) Напишите программу, которая принимает на вход строку символов
#(заглавные и прописные буквы латинского алфавита), которые могут повторятся,
#например: YYYYggkeeeAAABV . Заглавные и строчные буквы различаются. Программа
#должна преобразовать (закодировать) строку в сжатый формат: Y4g2ke3A3BV

#Число после символа – количество повторений, если символ однократный – едениwe
#выводить не надо.

s = input("введите символы: ")
count = 1
s_coded = ""
s += "\0" #символ в конец строки для обработки последнего символа
#print(len(s))
for i in range(1, len(s)):
    if s[i] == s[i-1]:
        count += 1
    else:
        #символ встречается более одного раза, добавляем его кол-во
        if count > 1:
            s_coded += s[i-1] + str(count)
        else:
            s_coded += s[i-1]
        count = 1  #сброс
print(s_coded)

