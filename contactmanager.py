class ContactManager():

    phonebook = [] # Array

    # Função que cria os contactos
    def create_contact(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
        self.phonebook.append([self.name, self.phone, self.email]) # Adiciona os Valores inseridos na função
        return print('[+] Contacto Criado com Sucesso!')

    # Função que consulta os dados da array
    def consult(self, id):
        try:
            return print(f'[+] Nome: {self.phonebook[id-1][0]}\n[+] Nº Tele: {self.phonebook[id-1][1]}\n[+] Email: {self.phonebook[id-1][2]}')
        except IndexError:
            return print((f'[!] Contacto Não Foi Encontrado!'))
        
    # Função que remove o contacto
    def delete_contact(self, id_contact):
        if id_contact <= 0: # Se o id for menor ou i,gual a 0
            return print((f'[!] Contacto Não Foi Encontrado!'))
        try:
            del self.phonebook[id_contact-1]
            return print('[!] Contacto Removido!')
        except IndexError:
             return print((f'[!] Contacto Não Foi Encontrado!'))
    
    # Função para contabilizar o numero de contactos
    def length_phonebook(self):
        if len(self.phonebook) == 0:
            print('[!] Lista Telefónica Vazia!')
        else:
            print(f'[!] Total: {len(self.phonebook)} Contacto(s)!')

    # Função para editar contacto
    def edit_contact(self, id_contact, name, phone, email):
        if id_contact <= 0:
            return print((f'[!] Contacto Não Foi Encontrado!'))
        try:
            self.phonebook[id_contact-1][0] = name
            self.phonebook[id_contact-1][1] = phone
            self.phonebook[id_contact-1][2] = email
            return print('[!] Contacto Editado com sucesso!')
        except IndexError:
            return print((f'[!] Contacto Não Foi Encontrado!'))
        
    # Função para aparecer os contactos com um identificador
    def show_contacts(self):
        if len(self.phonebook) > 0:
            print("--======== Contactos ========--")
            for count, value in enumerate(self.phonebook):
                print(f'{count+1} - {value[0]}')

