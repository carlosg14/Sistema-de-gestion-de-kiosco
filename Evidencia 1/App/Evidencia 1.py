

def login():
    pass

def nuevo_usuario():
    pass

def nueva_contra():
    pass

def menu():

    n = '\nSeleccione una opcion: '

    while True:
        print('\n' * 10)
        print("""
            
        ██████  ██ ███████ ███    ██ ██    ██ ███████ ███    ██ ██ ██████   ██████  
        ██   ██ ██ ██      ████   ██ ██    ██ ██      ████   ██ ██ ██   ██ ██    ██ 
        ██████  ██ █████   ██ ██  ██ ██    ██ █████   ██ ██  ██ ██ ██   ██ ██    ██ 
        ██   ██ ██ ██      ██  ██ ██  ██  ██  ██      ██  ██ ██ ██ ██   ██ ██    ██ 
        ██████  ██ ███████ ██   ████   ████   ███████ ██   ████ ██ ██████   ██████    
                                                                             
            """)

        print('\n 1- Inicie sesion.')
        print('\n 2- Registrate.')
        print('\n 3- ¿Olvido su contraseña?.')
        print('\n 4- Salir.')
        opcion = input(n)

        if opcion == '1':
            pass
        elif opcion == '2':
            pass
        elif opcion == '3':
            pass
        elif opcion == '4':
            break
        else:
            n += '(Opcion invalida.......)\n'

if __name__ == "__main__":
    menu()
