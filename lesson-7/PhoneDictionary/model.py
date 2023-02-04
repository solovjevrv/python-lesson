import view

def writeContacts(contactsList):
    data = open('phone_dictionary', mode="w", encoding="utf-8")
    for item in contactsList:
        data.writelines(item + "\n")
    data.close()

def readContacts():    
    data = open('phone_dictionary', mode="r", encoding="utf-8")
    contactsList = data.readlines()
    view.printContactsList(contactsList)
    data.close()