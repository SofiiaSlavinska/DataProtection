# -*- coding: utf-8 -*-
print("\t\t\t Шифр Трітеміуса")
abetka=[" ", "а", "б", "в", "г", "ґ", "д", "е", "є", "ж", "з", "и", "і", "ї", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ь", "ю", "я"]
print("\t\t\t Шрифт Трітеміуса")
while True:
    option=int(input("Вам треба кодувати чи декодувати повідомлення?(1/2): "))
    text=str(input("Введіть текст українською: ")) #1 рядок
    key_word=str(input("Введіть ключове слово: ")) #3 рядок
    key_text = (key_word*(len(text)//len(key_word)+1))[:len(text)]
    text_index = list(map(abetka.index, text)) #2 рядок
    key_word_index = list(map(abetka.index, key_text))#4 рядок
    if option==1:
        sum_index=[(a + b)%33 for a, b in zip(text_index, key_word_index)] #5 і 6 рядок
    if option==2:
        sum_index = [(a - b + 33) if a < b else (a - b) for a, b in zip(text_index, key_word_index)]
    coded_text = ''.join(abetka[i] for i in sum_index) #7 рядок
    print(coded_text)
