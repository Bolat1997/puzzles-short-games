import pyAesCrypt
import os


# функция дешифрования файла

def decryption(file, password):
    # обозначим размер буффера
    buffer_size = 512 * 1024

    # вызываем метод дешифрования
    pyAesCrypt.decryptFile(
        str(file),
        str(os.path.splitext(file)[0]),
        password,
        buffer_size
    )

    # чтобы видеть результат выводим на печать имя
    print("Файл '" + str(os.path.splitext(file)[0]) + "' дешифрован")

    # Удаляем исходный файл
    os.remove(file)


# функция сканирования директорий
def walking_by_dirs(dir, password):
    # перебираем все поддиректории в указанной директории
    for name in os.listdir(dir):
        path = os.path.join(dir, name)

        # если находим файл,то дешифруем его
        if os.path.isfile(path):
            try:
                decryption(path, password)
            except Exception as ex:
                print(ex)




        else:
            walking_by_dirs(path, password)


password = input("Введите пароль для Шифрования")
walking_by_dirs('C:\\Users\Admin\Desktop\Кости', password)