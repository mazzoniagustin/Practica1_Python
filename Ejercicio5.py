my_list = []

number = int(input('Ingrese un número: '))
while number != 0:
    my_list.append(number)
    number = int(input('Ingrese un número: '))
for num in my_list:  # Otra forma de recorrer el for sin el range.
    if (num < 0):
      break
    print(num)
