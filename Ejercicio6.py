my_list = []
even_list = [] # Pares
odd_list = []   #Impares

number = int(input('Ingrese el numero para agregar a la lista.'))
while (number != 0):
  my_list.append(number)
  number = int(input('Ingrese el número a agregar.'))
  
for num in my_list:
  if (num % 2 == 0):
    even_list.append(num)
  else:
    odd_list.append(num)

# Mostrar las listas
print (f'Lista de números pares: ')
for num in even_list:
  print(num)
print (f'Lista de números impares: ')
for num in odd_list:
  print(num)