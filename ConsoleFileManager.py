def ConsoleFManager():
    import os
    import shutil
    import platform
    from victorina import victorina as V
    from account import my_account

    print('** Консольный менеджер файлов **')

    while True:
        print('1. Создать папку')
        print('2. Удалить (файл/папку)')
        print('3. Копировать (файл/папку)')
        print('4. Просмотр содержимого рабочей директории')
        print('5. Просмотр папок')
        print('6. Просмотр файлов')
        print('7. Просмотр информации об операционной системе')
        print('8. Создатель программы')
        print('9. Играть в Викторину')
        print('10. Мой банковский счет')
        print('11. Смена рабочей директории')
        print('12. Выход')

        choice = input('Выберите пункт меню: ')

        if choice == '1':
            create_name = input('Введите название новой папки: ')
            if not os.path.exists(create_name):
                os.mkdir(create_name)
                print('Папка успешно создана')
            else:
                print('Такаое название уже существует, попробуйте другое: ')
            pass
        elif choice == '2':
            del_name = input('Введите имя (файла/папки) для удаления: ')
            if not os.path.isdir(del_name):
                os.remove(del_name)
            else:
                os.rmdir(del_name)
            print('Обьект успешно удален!')
            pass
        elif choice == '3':
            copy_name = input('Введите название копируемого обьекта: ')
            new_copy_name = input('Введите новое название: ')
            if not os.path.isdir(copy_name):
                shutil.copyfile(copy_name, new_copy_name)
            else:
                shutil.copytree(copy_name, new_copy_name)
            print('Копирование успешно!')
            pass
        elif choice == '4':
            print('Содержимое рабочей директории: ')
            print(os.listdir())
            pass
        elif choice == '5':
            for i in os.listdir():
                if os.path.isdir(i):
                    print(i)
            print('Доступные папки: ')
            pass
        elif choice == '6':
            for i in os.listdir():
                if os.path.isfile(i):
                    print(i)
            print('Доступные файлы: ')
            pass
        elif choice == '7':
            print('Информация о системе: ')
            print(platform.uname())
            pass
        elif choice == '8':
            print('Байдин К.С., начинающий програмист.')
            pass
        elif choice == '9':
            V()
            pass
        elif choice == '10':
            my_account()
            pass
        elif choice == '11':
            print(os.getcwd())
            new_dir = input('Введите путь к новому месту рабочей директории: ')
            os.chdir(new_dir)
            print(os.getcwd())
            print('Дирректория изменена')
            pass
        else:
            break


ConsoleFManager()
