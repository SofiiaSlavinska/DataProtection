# -*- coding: utf-8 -*-
print("\t\t\t Шифр Полібія")
abetka=["а", "б", "в", "г", "ґ", "д", "е", "є", "ж", "з", "и", "і", "ї", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ь", "ю", "я"]
polybius_square=[abetka[i:i+6] for i in range(0, len(abetka), 6)]
while True:
    option=int(input("Вам треба кодувати чи декодувати повідомлення?(1/2): "))
    text=input("Введіть повідомлення: ")
    coded_text='';
    if option==1:
        for letter in str(text):
            for i, row in enumerate(polybius_square):
                if letter in row:
                    j=row.index(letter)
                    coded_text+=str(i+1)+str(j+1)
    if option==2:
        for i in range(0, len(text), 2):
            row=int(text[i])-1
            print(row)
            col=int(text[i+1])-1
            print(col)
            coded_text+=polybius_square[row][col]
    print(coded_text)



    
