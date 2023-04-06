from enc import encription,walk_by_dirs
from  dec import decription,walk_by_dirs_de
import sys
import os

while True:
    print("""1. Зашифровать файл
    2. Дешифровать файл
    3. Зашифровать директорию
    4. Дешифровать директорию
    5. Выход""")
    try:
        command = int(input("Введите номер команды: "))
    except Exception:
        print("Введите цифру!")

    match command:
        case 1:
            pasword = input("Введите пароль для шифрования: ")
            file = os.path(input("Введите имя файла: "))
            encription(file, password)
        case 2:
            password = input("Введите пароль для расшифровки: ")
            file = os.path(input("Введите имя файла: "))
            decription(file,password)
        case 3:
            pasword = input("Введите пароль для шифрования: ")
            dir = os.path(input("Введите имя директории: "))
            walk_by_dirs(dir, password)
        case 4:
            pasword = input("Введите пароль для расшифровки: ")
            dir = os.path(input("Введите имя директории: "))
            walk_by_dirs_de(dir, password)
        case 5:
            print("Выход")
            exit()

