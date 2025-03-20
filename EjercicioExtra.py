inventory = {}
option = 0 # Inicializo la variable para que acceda al while
while option != 4:
    print('--- Menú de opciones ---')
    print()
    print('1- Agregar un producto.')
    print ('2- Eliminar un producto.')
    print('3- Mostrar los productos.')
    print ('4- Salir.')
    option = input('Seleccione la opción deseada: ')
    if (option.isdigit()): # Chequea que no se haya ingresado un String.
        option = int(option)
        if option == 1:
            product_name = input('Ingrese el nombre del producto:  ')
            product_quantity = int(input('Ingrese la cantidad del producto: '))
            if product_name in inventory:
                inventory[product_name] += product_quantity
            else:
                inventory[product_name] = product_quantity
        elif option == 2:
            print('Ingrese el nombre del producto que desea eliminar')
            product_name = input()
            if product_name in inventory: # Verifica si se encuentra
                del(inventory[product_name]) # Si se encuentra, es eliminado
            else:
                print('El producto ingresado no se encuentra en el inventario.')
        elif option == 3:
            print('Inventario: ')
            print(inventory)
        elif option == 4:
            break # Termina la ejecución del programa
        else:
            print('Ingrese un valor válido.')
    else:
        print('Ingrese un valor correcto.')
