# -*- coding: utf-8 -*-
print("\t\t\t Шифр Вернама")
while True:
    option=int(input("Вам треба кодувати чи декодувати повідомлення?(1/2): "))
    text=str(input("Введіть повідомлення: "))
    if option==1:
        binary_text = ''.join(format(ord(i), '08b') for i in text)
        key=str(input("Введіть ключ(має міститити "+str(len(binary_text))+" символa/ів): "))
        encrypted_text = ""
        for i in range(len(binary_text)):
           bit = int(binary_text[i]) ^ int(key[i])
           encrypted_text += str(bit)
        print(encrypted_text)
    elif option==2:
        key=str(input("Введіть ключ(має міститити "+str(len(text))+" символa/ів): "))
        decrypted_text = ""
        for i in range(len(text)):
            bit = int(text[i]) ^ int(key[i])
            decrypted_text += str(bit)
        decrypted_text = ''.join(chr(int(decrypted_text[i:i+8], 2)) for i in range(0, len(decrypted_text), 8))
        print(decrypted_text)
