# -*- coding: utf-8 -*-
print("\t\t\t Шифр Плейфера")
abetka='абвгдеєжзиіїйклмнопрстуфхцчшщьюя'
def create_matrix(key):
    key=''.join(sorted(set(key), key=key.index))
    global abetka
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
def encripting():
    global pairs
    global coded_text
    for pair in pairs:
        row1, col1 = next((i, row.index(pair[0])) for i, row in enumerate(matrix) if pair[0] in row)
        row2, col2 = next((i, row.index(pair[1])) for i, row in enumerate(matrix) if pair[1] in row)
        if row1 == row2:
            coded_text += matrix[row1][(col1+1)%5] + matrix[row2][(col2+1)%5]
        elif col1 == col2:
            coded_text += matrix[(row1+1)%5][col1] + matrix[(row2+1)%5][col2]
        else:
            coded_text += matrix[row1][col2] + matrix[row2][col1]
    return coded_text
def decoding():
    global pairs
    global coded_text
    for pair in pairs:
        row1, col1 = next((i, row.index(pair[0])) for i, row in enumerate(matrix) if pair[0] in row)
        row2, col2 = next((i, row.index(pair[1])) for i, row in enumerate(matrix) if pair[1] in row)
        if row1 == row2:
            coded_text += matrix[row1][(col1-1)%5] + matrix[row2][(col2-1)%5]
        elif col1 == col2:
            coded_text += matrix[(row1-1)%5][col1] + matrix[(row2-1)%5][col2]
        else:
            coded_text += matrix[row1][col2] + matrix[row2][col1]
    return coded_text
while True:
    option=int(input("Вам треба кодувати чи декодувати повідомлення?(1/2): "))
    text=input("Введіть повідомлення: ")
    key=input("Введіть кодове слово: ")
    coded_text='';
    matrix=create_matrix(key)
    pairs=create_pairs()
    if option==1:
        coded_text=encripting()
    elif option==2:
        coded_text=decoding()
    print(coded_text)
