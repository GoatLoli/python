#(задача 4) На входе дана строка текста. Словом
#считается последовательность непробельных символов
#идущих подряд, слова разделены одним или большим числом
#пробелов или символами конца строки
#Для каждого слова из этого текста подсчитайте, сколько раз
#оно встречалось в этом тексте ранее

list1 = "one.  two one two.   three. two"
list1 = list1.replace('.','')
list1 = list1.split()
#print(list1)
n = len(list1)
list2 = {}
for i in range(n):
    list2[i] = list1[i]
#print(list1,list2)
result = ""
for i in range(n-1, -1, -1):
    count = 0
    for j in range(i-1, -1, -1):
        if list2[i] == list2[j]:
            count += 1
    result = str(count) + result
print(result)
