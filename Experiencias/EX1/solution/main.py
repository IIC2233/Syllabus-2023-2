from utils.pretty_print import(
    print_opciones_menu,
    print_usuario,
    print_salida,
    print_canasta,
    print_items,
    print_opcion_invalida
)
from utils.loader import cargar_items
from entities import Usuario

def menu():
    items = cargar_items()
    print_opciones_menu()
    opcion = input('Indique su opcion: ')
    while opcion != 'e':
        '''
        Selecciona una de las siguientes opciones de usuarioBasket:
        a) Crear perfil de usuario
        b) Agregar items a la canasta
        c) Mostrar la canasta
        d) Realizar compra
        e) Salir
        '''
        if opcion == 'a':
            sub = input('Usuario con suscripcion? [S/N]: ')
            if sub == 'S':
                usuario = Usuario(True)
            elif sub == 'N':
                usuario = Usuario(False)
            print_usuario(usuario)

        elif opcion == 'b':
            print_items(items)
            indice = int(input('> Agregar item a la compra: '))
            usuario.agregar_item(items[indice-1])
            items.pop(indice-1)

        elif opcion == 'c':
            print_canasta(usuario)

        elif opcion == 'd':
            usuario.comprar()
            print_usuario(usuario)
        else:
            print_opcion_invalida()
        
        print_opciones_menu()
        opcion = input('Indique su opcion: ')
    print_salida()

if __name__ == '__main__':
    menu()