import model
import view
from tkinter import *
from tkinter import ttk

contactsList = {}


def addContact():
    view.addItem()


def deleteContact():
    contactsList['contacts'].delete(contactsList['contacts'].curselection()[0])
    sendConstactsListToModel()


def addToListBox(contacts):
    contactsList['contacts'].insert(END, contacts)
    sendConstactsListToModel()


def getContactsList():
    return contactsList


def sendConstactsListToModel():
    phoneList = contactsList['contacts'].get(0, END)
    model.writeContacts(phoneList)


def start():
    root = Tk()
    frame = ttk.Frame(root, padding=30)
    frame.grid()

    Label(frame, text='Справочник телефонов', font=("Arial", 16)).grid(
        row=0)
    Label(frame, text='Введите имя').grid(row=1, column=0)
    inputName = Entry(frame)
    inputName.grid(row=1, column=1)
    contactsList['name'] = inputName

    Label(frame, text='Введите фамилию').grid(row=2, column=0)
    inputLastname = Entry(frame)
    inputLastname.grid(row=2, column=1)
    contactsList['lastname'] = inputLastname

    Label(frame, text='Введите номер телефона').grid(
        row=3, column=0)
    inputPhone = Entry(frame)
    inputPhone.grid(row=3, column=1)
    contactsList['phone'] = inputPhone

    addContactBtn = Button(
        frame, text='Добавить контакт', command=addContact).grid(row=4, column=1)

    deleteContactBtn = Button(
        frame, text='Удалить контакт', command=deleteContact).grid(row=6, column=1)

    contacts = Listbox(frame, width=50, height=10)
    contacts.grid(row=6, column=0)
    contactsList['contacts'] = contacts
    model.readContacts()

    root.mainloop()
