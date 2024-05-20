# -*- coding: utf-8 -*-
print("\t\t\t Шифр «подвійний квадрат» Уітстона")
def create_matrix(key):
    key=''.join(sorted(set(key), key=key.index))
    abetka='абвгдеєжзиіїйклмнопрстуфхцчшщьюя'
    abetka=''.join(ch for ch in abetka if ch not in key)
    table=key+abetka
    matrix=[]
    for i in range(0, len(table), 8):
        matrix.append(list(table[i:i+8]))
    return matrix
def create_pairs():
    global text
    text=text.lower().replace(' ', '')
    pairs=[]
    i=0
    filler='х';
    while i<len(text):
        if i == len(text) - 1:
            pairs.append((text[i], filler))
        elif text[i] == text[i+1]:
            pairs.append((text[i], filler))
        else:
            pairs.append((text[i], text[i+1]))
        i+=2
    return pairs
def encripting(pairs):
    global coded_text
    for pair in pairs:
        for row in table1:
            if pair[0] in row:
                i1,j1=table1.index(row), row.index(pair[0])
        for row in table2:
            if pair[1] in row:
                i2,j2=table2.index(row),row.index(pair[1])
        coded_text+=table2[i2][j1]+table1[i1][j2]
    return coded_text

def decoding(pairs):
    global coded_text
    for pair in pairs:
        for row in table2:
            if pair[0] in row:
                i1,j1=table2.index(row), row.index(pair[0])
        for row in table1:
            if pair[1] in row:
                i2,j2=table1.index(row),row.index(pair[1])
        coded_text+=table1[i2][j1]+table2[i1][j2]
    return coded_text
while True:
    option=int(input("Вам треба кодувати чи декодувати повідомлення?(1/2): "))
    text=input("Введіть повідомлення: ")
    key1=input("Введіть перше кодове слово: ")
    key2=input("Введіть друге кодове слово: ")
    table1=create_matrix(key1)
    table2=create_matrix(key2)
    pairs=create_pairs()
    coded_text='';
    if option==1:
        coded_text=encripting(pairs)
    elif option==2:
        coded_text=decoding(pairs) 
    print(coded_text)
