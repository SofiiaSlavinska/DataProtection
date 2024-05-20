# -*- coding: utf-8 -*-
import pandas as pd
print("\t\t\t Шифр  стандартної перестановки")
def encripting(df):
    global coded_text
    column_dict = {i: new_order[i] for i in range(max_num)}
    df = df.rename(columns=column_dict)
    df = df.sort_index(axis=1)
    coded_text = ''.join(df.values.flatten().tolist())
    return coded_text
def decoding(df):
    global coded_text
    original_order = {new_order[i]: i for i in range(max_num)}
    df = df.rename(columns=original_order)
    df = df.sort_index(axis=1)
    coded_text = ''.join(df.values.flatten().tolist())
    return coded_text
while True:
    option=int(input("Вам треба кодувати чи декодувати повідомлення?(1/2): "))
    text=input("Введіть повідомлення: ")
    key=input("Введіть шифр(послідовність чисел): ")
    coded_text=''
    max_num = max(int(digit) for digit in str(key))
    new_order = [int(digit) - 1 for digit in str(key)]
    table = [list(text[i:i+max_num]) for i in range(0, len(text), max_num)]
    df = pd.DataFrame(table)
    if option==1:
        coded_text=encripting(df)
    elif option==2:
        coded_text=decoding(df)
    print(coded_text)
