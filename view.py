
def greetings():
    print(' _____________________________________________________')
    print('|                                                     |')
    print('|    Привет, это консольный телефонный справочник!    |')
    print('|_____________________________________________________|')



def goodbye():
    print(' ___________________________')
    print('|                           |')
    print('|    До скорых встреч...    |')
    print('|___________________________|')
    print()



def error():
    print('Ошибка ввода!')



def show_contacts(data: list, text_str='Все контакты'):
    print(text_str)
    for item in data:
        list_item = item.split(':')
        print('               Фамилия: ' + list_item[0] +
               ' Имя: ' + list_item[1] + 
               ' Отчество: ' + list_item[2] + 
               ' Телефон: ' + list_item[3], end='')



def success(res):
    print('Данные успешно сохранены.')



def not_success(res):
    print('Что-то пошло не так.')

    

def menu():
    print()
    print('Команды работы со справочником: ')
    print('                                 1 - Показать все контакты.\n'
          '                                 2 - Добавить контакт.\n'
          '                                 3 - Поиск контакта.\n'
          '                                 4 - Изменить контакт.\n'
          '                                 5 - Удалить контакт.\n'
          '                                 6 - Выход из справочника.'
        )
    




if __name__ == '__main__':
    menu()

