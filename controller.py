import view, model

def start():
    view.greetings()    
    while True:
        view.menu()
        answer = input('Введите номер команды: ')

        if answer == '1':
            data = model.get_data()
            view.show_contacts(data)


        elif answer == '2':
            contact = input('Введите данные контакта через пробел: ')
            res = model.add_contact(contact)
            if res:
                view.success(res)
            else:
                view.not_success(res)


        elif answer == '3':
            contact = input('Введите имя и/или фамилию контакта для поиска через пробел: ')
            resul = model.find_contact(contact)
            lst = []
            lst.append(resul)
            if len(resul) != 0:
                view.show_contacts(lst, 'Найденный контакт: ')
            elif len(resul) == 0:
                print('Контакт не найден.')



        elif answer == '4':
            contact = input('Введите имя и/или фамилию контакта для изменения через пробел: ')
            resu = model.find_contact(contact)
            lst = []
            lst.append(resu) 
            if len(resu) != 0:
                view.show_contacts(lst, 'Контакт который хотим изменить: ')
                contact = input('Введите новые данные контакта через пробел: ')
                yes_no = input('Точно хотите изменить? [да/нет]: ')
                if yes_no == 'да':
                    new_contact = model.change_contact(lst, resu, contact)
                    n_c = ' '.join(resu.split(':'))[:-1]
                    print(f'Контакт "{n_c}" успешно изменен на "{new_contact}".')

                elif yes_no == 'нет':
                    print('Так вроде хотели же?... ну в следующий раз...')



            else:
                print('Контакт не найден.')   


        elif answer == '5':
            contact = input('Введите имя и/или фамилию контакта для удаления через пробел: ')
            resu = model.find_contact(contact)
            lst = []
            lst.append(resu) 
            if len(resu) != 0:
                yes_no = input('Точно хотите удалить? [да/нет]: ')
                if yes_no == 'да':
                    view.show_contacts(lst, 'Хотим удалить контакт: ')
                    model.delete_contact(lst, resu)
                    print(f'Контакт {resu} успешно удален.')

                elif yes_no == 'нет':
                    print('Так вроде хотели же?... ну в следующий раз...')    


            elif len(resul) == 0:
                print('Контакт не найден.')   


        elif answer == '6':
            view.goodbye()
            break


        else:
            view.error()


