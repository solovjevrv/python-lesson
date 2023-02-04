import controller


def addItem():
    items = controller.getContactsList()
    name = items['name'].get()
    lastName = items['lastname'].get()
    phone = items['phone'].get()
    item = f'{name} {lastName} {phone}'
    controller.addToListBox(item)

def printContactsList(contactsList):
    for item in contactsList:
        controller.addToListBox(item)
