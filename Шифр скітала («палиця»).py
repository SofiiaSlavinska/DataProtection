# -*- coding: utf-8 -*-
print("\t\t\t Шифр  скітала («палиця»)")
def encripting():
    global coded_text
    table = []
    text_index = 0
    for i in range(rows):
        row = []
        for j in range(columns):
            if text_index < len(text):
                row.append(text[text_index])
                text_index += 1
            else:
                row.append('')
        table.append(row)
    for row in table:
        print(row)
    for j in range(len(table[0])):
        column = [row[j] for row in table]
        coded_text+=''.join(column)
    return coded_text
def decoding():
    global coded_text
    table = []
    text_index = 0
    for i in range(columns):  
        row = []
        for j in range(rows):  
            if text_index < len(text):
                row.append(text[text_index])
                text_index += 1
            else:
                row.append('')
        table.append(row)
    table = list(map(list, zip(*table)))
    for row in table:
        coded_text += ''.join(row)
    return coded_text
while True:
    option=int(input("Вам треба кодувати чи декодувати повідомлення?(1/2): "))
    text=input("Введіть повідомлення: ")
    rows=int(input("Введіть кількість рядків: "))
    columns=int(input("Введіть кількість стовпців: "))
    coded_text=''
    if option==1:
        coded_text=encripting()
    elif option==2:
        coded_text=decoding()
    print(coded_text)
