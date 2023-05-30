import view, model

def start():
    view.greetings()
    while True:
        view.menu()
        answer = int(input("Введите номер команды "))
        if answer == 1:
            date = model.data()
            view.show_contacts(date)
        elif answer == 2:
            contact = input("Введите данные для добавления ")
            res = model.add_contact(contact)
            view.result(res)
        elif answer == 3:
            contact = input("Введите данные для поиска ")
            res = model.find_contact(contact)
            view.show_contacts(res)
        elif answer == 4:
            break
        else:
            view.error()