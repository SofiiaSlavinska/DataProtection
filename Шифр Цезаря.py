# -*- coding: utf-8 -*-
abetka=["а", "б", "в", "г", "ґ", "д", "е", "є", "ж", "з", "и", "і", "ї", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ь", "ю", "я"]
print("\t\t\t Шифр Цезаря")
while True:
    option=int(input("Вам треба кодувати чи декодувати повідомлення?(1/2): "))
    text=str(input("Введіть текст українською: "))
    key=int(input("Введіть число зсувів: "))
    new_text='';
    if option==1:
        for letter in text:
            if letter in abetka:
                index=(abetka.index(letter)+key)%len(abetka)
                new_text+=abetka[index]
    if option==2:
        for letter in text:
            if letter in abetka:
                index=(abetka.index(letter)-key)%len(abetka)
                new_text+=abetka[index]       
    print(new_text)

        
        
        
        
