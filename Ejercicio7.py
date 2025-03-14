my_list = []
cadena = ''

number = int(input("Ingrese un número (0 para finalizar): "))
while number != 0:
    my_list.append(number)
    number = int(input("Ingrese un número (0 para finalizar): "))
for num in my_list:
    if (num % 3 != 0):
        cadena += str(num) + " - "
print(cadena)
