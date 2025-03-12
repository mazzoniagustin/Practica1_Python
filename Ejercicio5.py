my_list = []

number = int(input('Ingrese un número'))
while number != 0:
  my_list.append(number)
  number = int(input('Ingrese un número'))
for i in range(len(my_list)):
  if (my_list[i] < 0):
    break
  print(my_list[i])
