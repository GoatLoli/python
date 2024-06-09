#(задача 6) Дан текст (строка). Выведите все слова,
#встречающиеся в тексте, по одному на каждую строку.
#Слова должны быть отсортированы по убыванию их количества
#появления в тексте, а при одинаковой частоте появления —
#в лексикографическом порядке.

list1 = "такса любит сосиску.. сосиска вкусна такой собаке, как такса!"
point = [".", ",", "!"]
a = ""
list1 = list1.replace(".", "")
list1 = list1.replace(",", "")
list1 = list1.replace("!", "")
a = list1.split(" ")

n = len(a)
list2 = {}

for i in range(len(set(a))):
    count = 1
    f = ""
    for j in range(1, len(a)):
        if a[0]==a[j]:
            f = a[j]
            count += 1
    for j in range(count):

        if f in a:
            a.remove(f)
        else:
            f = a[0]
            a.pop(0)
    list2[f] = count
#print(sl)
sort = sorted(list2, key=lambda x: (-list2[x], x))

for i in sort:
    print(i)
