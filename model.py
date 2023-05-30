def data(): # получаем из файла
  with open('data_file.txt', 'r', encoding='utf-8') as data_file:
    data = data_file.read().split('\n')

  return data

def add_contact(contact): # добавляем контакт
  with open('data_file.txt', 'a', encoding='utf-8') as data_file:
    data_file.write(f'{contact}\n')

  return contact
