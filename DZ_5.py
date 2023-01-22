import os
import shutil
import sys
import pathlib


def autor_info():
    print(f'Autor Skarlet')

while True:
    delete = input( 'Удалить папку или файл: ')
    if os.rmdir(f'{delete}'):
        pass
    file_copy = input("Введите название папки для копирования:  ")
    if shutil.copy(f'{file_copy}', f'{file_copy}.copy'):
        pass
    print('Просмотр пути и содержимого рабочей директории: ')
    print("Путь:", os.getcwd())
    print('Содержимое',os.walk(top=r"C:\Users\black\PycharmProjects\pythonProject5"))
    print('Список файлов и папок:', os.listdir())
    print('Посмотреть только папки:')
    folders_path = pathlib.Path(r"C:\Users\black\PycharmProjects\pythonProject5")
    content = os.listdir(folders_path)
    folders = []
    for folder in content:
        if os.path.isdir(os.path.join(folders_path, folder)):
            folders.append(folder)
    print(folders)
    print('Посмотреть только файлы:')
    files_path = pathlib.Path(r"C:\Users\black\PycharmProjects\pythonProject5")
    content_1 = os.listdir(folders_path)
    files = []
    for file in content_1:
        if os.path.isfile(os.path.join(files_path, file)):
            files.append(file)
    print(files)
    print('Просмотр информации об операционной системе: ', sys.platform)
    print('Создатель программы: ', autor_info())
    print('Сыграть в викторину:',open('victory.py'))
    print('Мой банковский счет:', open('check.py'))
    break

