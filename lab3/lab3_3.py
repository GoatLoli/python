#(задача 3) Напишите программу,  которая выводит
#текстовое написание числа. Число вводится пользователем
#в диапазоне от 1 до 1000. Например, при вводе числа 17 –
#выводится «семнадцать».

cifra = input("введите число:")
perevod = ""
ed = ["один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
dec_ed = ["одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать",\
          "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"]
dec = ["десять", "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят",\
       "восемьдесят", "девяносто"]
sto = ["сто", "двести", "триста", "четыреста", "пятьсот", "шестьсот", "семьсот", "восемьсот",\
       "девятьсот"]

#1000
if cifra == "1000":
    print("тысяча")
    
#100-999 [0][1][2]
elif len(cifra) == 3:
    if int(cifra) > 100 and (cifra[1] != "1"): #если не просто 100 и не содержит 11-19
        perevod = (sto[(int(cifra[0])) - 1] + " " + dec[(int(cifra[1])) - 1]\
                  + " " + ed[(int(cifra[2])) - 1])
    elif int(cifra) > 100 and (cifra[1] == "1"): #112 212 312 и т.д.
        perevod = (sto[int(cifra[0])-1] + " " + dec_ed[int(cifra[2])-1])
    elif (cifra[1] == cifra[2] == "0"): #100 200 300
        perevod = sto[int(cifra[0])-1]

#10-99 [0][1]
elif len(cifra) == 2:
    if int(cifra) > 19 and (cifra[1] != "0"):
        perevod = (dec[(int(cifra[0])) - 1] + " " + ed[(int(cifra[1])) - 1])
    elif (int(cifra) > 10) and (int(cifra) < 20):
        perevod = dec_ed[int(cifra[1])-1]
    else:
        perevod = dec[(int(cifra[0])) - 1]

#1-9
elif len(cifra) == 1:
    perevod = ed[(int(cifra[0])) - 1]
print(perevod)
