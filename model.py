def get_data():
    with open('contacts.txt', 'r', encoding='utf-8') as file:
       data = file.readlines()
    return data



def add_contact(contact):
    add_data = contact.split()
    res_add_data = add_data[0] + ':' + add_data[1] + ':' + add_data[2] + ':' + add_data[3] 

    with open('contacts.txt', 'a', encoding='utf-8') as file:
        res = file.write(res_add_data)
        file.write('\n')
    return res



def find_contact(contact):
    find_data = contact.split()
    res_find_data = get_data()
    if len(find_data) == 2:
        for item in res_find_data:
            if find_data[0] in item and find_data[1] in item:
                return item
        return []
    elif len(find_data) == 1:
        for item in res_find_data:
            if find_data[0] in item:
                return item
        return []    
    


def delete_contact(ct, resu):
    data = get_data()
    new_data = []
    for item in data:
        if resu not in item:
            new_data.append(item)
    with open('contacts.txt', 'w', encoding='utf-8') as file:
        file.writelines(new_data)



def change_contact(ct, resu, contact):
    delete_contact(ct, resu)
    add_contact('\n' + contact)
    return contact



if __name__ == '__main__':
    print(*get_data())
