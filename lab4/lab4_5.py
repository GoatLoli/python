#(задача 5) Напишите программу, которая подсчитывает количество
#единиц товаров, приобретенных покупателями онлайн-магазина.
#На вход программе подается число n – количество записей о покупках,
#а затем n строк вида: ID Покупателя ( целое число) Товар(одним словом)
#Количество( целое число).

print("кол-во записей: ")
n= int(input())
a=[]
for i in range(n):
    #id покупателя(число) товар(одно слово) кол-во(число)
    stroka = input("id, товар, кол-во: ")
    a.append(stroka.split())

for i in range(len(a)):
    stroka = ''
    q=a[i][0]


    if q != " ":
        print("id:", q)
        for y in range (len(a)):
            for x in range(len(a[i])-2):
                if q in a[y][x]:
                    stroka =  stroka + a[y][x+1] + " " + a[y][x+2] + ", "
                    a[y][x] = " "
                    a[y][x+1] = " "
                    a[y][x+2] = " "

    print(stroka)
