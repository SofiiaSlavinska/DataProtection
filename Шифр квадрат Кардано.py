# -*- coding: utf-8 -*-
print("\t\t\t Шифр квадрат Кардано ")
def encripting(text, key, abetka):
    square = [['' for _ in range(a)] for _ in range(a)]
    for _ in range(a):
        for i in range(a):
            for j in range(a):
                if key[i][j] == '1' and text:
                    square[i][j] = text.pop(0)
                elif square[i][j] == '' and abetka: #заповнення порожніх клітинок
                    square[i][j] = abetka[0]
                    abetka = abetka[1:]
        key = list(map(list, zip(*key[::-1])))  #поворот ключа
    coded_text=''.join([''.join(row) for row in square])
    return coded_text
def decoding(text, key, coded_text):
    square = [[text[i*a+j] for j in range(a)] for i in range(a)]
    for _ in range(a): 
        for i in range(a):
            for j in range(a):
                if key[i][j] == '1':
                    coded_text += square[i][j]
        key = list(map(list, zip(*key[::-1])))  
    return coded_text
while True:
    option=int(input("Вам треба кодувати чи декодувати повідомлення?(1/2): "))
    a=int(input("Введіть сторону квадрата: "))
    text=input("Введіть повідомлення: ")
    text=list(text)
    key=input("Введіть ключ: ")
    key = [bin(int(x)).replace("0b", "").zfill(a) for x in str(key)]
    abetka='абвгдеєжзиіїйклмнопрстуфхцчшщьюя'
    coded_text='';
    if option==1:
        coded_text=encripting(text, key, abetka)
    elif option==2:
        coded_text=decoding(text, key, coded_text) 
    print(coded_text)
