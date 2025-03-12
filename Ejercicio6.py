my_list = []
even_list = [] # Pares
odd_list = []   #Impares

number = int(input('Ingrese el numero para agregar a la lista.'))
while (number != 0):
  my_list.append(number)
  number = int(input('Ingrese el número a agregar.'))
for i in range(len(my_list)):
  if (my_list[i] % 2 == 0):
    even_list.append(my_list[i])
  else:
    odd_list.append(my_list[i])

# Mostrar las listas
print (f'Lista de números pares: ')
for i in range(len(even_list)):
  print(even_list[i])
print (f'Lista de números impares: ')
for i in range(len(odd_list)):
  print(odd_list[i])