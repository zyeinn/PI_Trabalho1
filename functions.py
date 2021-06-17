from contactmanager import ContactManager
import sys
import time
import os

contacto = ContactManager()

def clear():
    time.sleep(3)
    if os.name == 'nt': # Se o sistema operational for windows, escreve 'cls' no terminal
        os.system('cls')
    else:
        os.system('clear')

def firstoption():
    name = input('[?] Nome: ')
    phone = int(input('[?] Nº Telefone: '))
    if len(str(phone)) != 9: # Restringir o numero de caracters inseridos
        print('[!] O número de telefone que forneceu não tem o comprimento adequado!')
        phone = int(input('[?] Nº Telefone: '))
    email = input('[?] Email: ')

    contacto.create_contact(name, phone, email) # Enviar os dados recebidos pelo utilizador para a class ContactManager e criar um contacto

def secondoption():
    id_contact = int(input('[?] ID: '))
    name = input('[?] Nome: ')
    phone = int(input('[?] Nº Telefone: '))
    if len(str(phone)) != 9: # Restringir o numero de caracters inseridos
        print('[!] O número de telefone que forneceu não tem o comprimento adequado!')
        phone = int(input('[?] Nº Telefone: '))
    email = input('[?] Email: ')
    contacto.edit_contact(id_contact, name, phone, email)

def thirdoption():
    id_contact = int(input('[?] ID: '))
    safemode = input('[!] Digite \'y\' para confirmar!\n~> ').lower() # Pergunta ao Utilizador se quer realmente apagar o contacto
    if safemode == 'y':
        contacto.delete_contact(id_contact)
    else:
        print('[!] Operação Cancelada!')

def fourthoption():
    id_contact = int(input('[?] ID: '))
    contacto.consult(id_contact)

def fifthoption():
    contacto.length_phonebook()

def exitoption():
    safemode = input('[!] Digite \'y\' para confirmar!\n~> ').lower() # Pergunta ao Utilizador se quer realmente sair do programa
    if safemode == 'y':
        print('[-] Saindo...')
        sys.exit()

def menu():
    try:
        print("""--=== Lista Telefónica ===--
[1] Criar Contacto
[2] Editar Contacto
[3] Eliminar Contacto
[4] Consultar Contacto
[5] Número de contactos Existentes
[0] Sair
--========================--""")
        option = int(input('~> '))
        return option
    except ValueError: 
        print('[!] Opção válida!')

def controlMenu(option):
    if option == 1:
        firstoption()
        clear()
    elif option == 2:
        secondoption()
        clear()
    elif option == 3:
        thirdoption()
        clear()
    elif option == 4:
        fourthoption()
        clear()
    elif option == 5:
        fifthoption()
        clear()
    elif option == 0:
       exitoption()