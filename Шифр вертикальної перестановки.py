# -*- coding: utf-8 -*-
import pandas as pd
print("\t\t\t Шифр  вертикальної перестановки")
def encripting():
    global coded_text
    table = [list(text[i:i+max_num]) for i in range(0, len(text), max_num)]
    df = pd.DataFrame(table)
    column_dict = {i: new_order[i] for i in range(max_num)}
    df = df.rename(columns=column_dict)
    df = df.sort_index(axis=1)
    coded_text = ''.join(''.join(df[col].dropna().tolist()) for col in df)
    return coded_text
def decoding():
    global coded_text
    rows = len(text) // max_num
    table = [list(text[i:i+rows]) for i in range(0, len(text), rows)]
    df = pd.DataFrame(table).T
    column_dict = {new_order[i]: i for i in range(max_num)}
    df = df.rename(columns=column_dict)
    df = df.sort_index(axis=1)
    coded_text =''.join(df.values.flatten().tolist()) 
    return coded_text
while True:
    option=int(input("Вам треба кодувати чи декодувати повідомлення?(1/2): "))
    text=input("Введіть повідомлення: ")
    key=input("Введіть шифр(послідовність чисел): ")
    coded_text=''
    max_num = max(int(digit) for digit in str(key))
    new_order = [int(digit) - 1 for digit in str(key)]
    if option==1:
        coded_text=encripting()
    elif option==2:
        coded_text=decoding()
    print(coded_text)
