import pyAesCrypt
import os

#дешифрование файла
def decription(file,password):
    buffer_size = 512 * 1024

    pyAesCrypt.decryptFile(
        str(file),
        str(os.path.splitext(file)[0]),
        password,
        buffer_size
    )

    print("Файл  "+ str(os.path.splitext(file)[0]) + ' дешифрован')




#функция сканирования директорий
def walk_by_dirs_de(dir,password):
    for name in os.listdir(dir):
        path = os.path.join(dir,name)

        if os.path.isfile(path):
            try:
                decription(path,password)
            except Exception as ex:
                print(ex)
        else:
            walk_by_dirs_de(path,password)

