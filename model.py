# обработка

phone_book = []
path = 'phonebook.txt'

def get_phone_book():
    global phone_book
    return phone_book

def update_phone_book(contact: list):
    global phone_book
    phone_book.append(contact)

def open_phone_book():
    global phone_book
    global path
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
        for line in data:
            phone_book.append(line.strip().split(';'))

def save_phone_book():
    global phone_book
    global path
    data = []
    for line in phone_book:
        data.append(';'.join(line))
    with open(path, 'w', encoding='UTF-8') as file:
        data = file.write('\n'.join(data))

def search_contact(search: str):
    global phone_book
    search_results = []
    for line in phone_book:
        for field in line:
            if search in field:
                search_results.append(line)
                break
    return search_results

def show_index():
    global phone_book
    # for i, word in enumerate(phone_book, 1):
    #     print(f'{i} {word}')
    length = len(phone_book)
    for i in range(length):
        print(str(i + 1), phone_book[i])

def delete(j):
    global phone_book
    phone_book.pop(j-1)

def change(j, contact: list):
    global phone_book
    phone_book[j-1] = contact
