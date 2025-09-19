while True:
    print('\n---contact calendar----')
    print('1.add contacts')
    print('2.list contacts')
    print('3.remove contacts')
    print('4.to go out')
    capture_action = input('[a]dd , [l]istar, [r]emove, [o]ut    ')

    if capture_action == "a": 
        print('you chose to add')
        add_information = input('     ')
        with open("contacts.txt", 'a', encoding="UTF-8") as arquivo:
            arquivo.write(add_information + '\n')
            print("contact was saved successfully!")          
    elif capture_action == "l":
        with open("contacts.txt", 'r', encoding="UTF-8") as arquivo:
            list_name = arquivo.read().splitlines()
        print('lista txt', list_name)  
    elif capture_action == "r":
        name_remove = input('escolha algo para remover?     ')
        with open("contacts.txt", 'r', encoding="UTF-8") as arquivo:
            list_remove = arquivo.readlines()
            print(list_remove)
        maintained_contact = []
        for contact in list_remove:
            if name_remove != contact.strip():
                maintained_contact.append(contact)
        with open("contacts.txt", 'w', encoding="UTF-8") as arquivo:
            for contact in maintained_contact:
                arquivo.write(contact)
        print("Contact removed successfully!")

    elif capture_action == 'o':
        print('leave the progam...')
        break
    else:
        print("invalid option, try again.")