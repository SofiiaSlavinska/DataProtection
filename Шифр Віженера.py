# -*- coding: utf-8 -*-
print("\t\t\t Шифр Віженера")
def generate_vigenere_square(num_key):
    square = []
    shifted_abetka = ''.join(abetka[int(i) - 1] for i in str(num_key))
    shifted_row = shifted_abetka[0:] + shifted_abetka[:0]
    while len(shifted_row) < 33:
            shifted_row += abetka[len(shifted_row)]
    for i in range(33):
        square.append(shifted_row)
        shifted_row = shifted_row[1:] + shifted_row[:1]
    return square
def encrypt_vigenere(text, key_word, num_key):
    square = generate_vigenere_square(num_key)
    global coded_text
    global abetka
    for i, char in enumerate(text):
        if char in abetka:
            row = abetka.index(char)
            col = abetka.index(key_word[i % len(key_word)])
            coded_text += square[row][col]
        else:
            coded_text += char
    return coded_text
def decrypt_vigenere(text, key_word, num_key):
    square = generate_vigenere_square(num_key)
    global coded_text
    global abetka
    for i, char in enumerate(text):
        if char in abetka:
            row = abetka.index(key_word[i % len(key_word)])
            col = square[row].index(char)
            coded_text += abetka[col]
        else:
            coded_text += char
    return coded_text
while True:
    abetka = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'
    option = int(input("Вам треба кодувати чи декодувати повідомлення? (1/2): "))
    text = input("Введіть повідомлення: ")
    num_key = input("Введіть цифровий ключ: ")
    key_word = input("Введіть ключ-слово: ")
    coded_text = ''
    if option == 1:
        coded_text = encrypt_vigenere(text, key_word, num_key)
    elif option == 2:
        coded_text = decrypt_vigenere(text, key_word, num_key)
    print(coded_text)
