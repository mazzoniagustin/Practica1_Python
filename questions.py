import random
# Preguntas para el juego
questions = [
  "¿Qué función se usa para obtener la longitud de una cadena en Python?",
  "¿Cuál de las siguientes opciones es un número entero en Python?",
  "¿Cómo se solicita entrada del usuario en Python?",
  "¿Cuál de las siguientes expresiones es un comentario válido en Python?",
  "¿Cuál es el operador de comparación para verificar sidos valores son iguales?",
]
# Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers = [
  ("size()", "len()", "length()", "count()"),
  ("3.14", "'42'", "10", "True"),
  ("input()", "scan()", "read()", "ask()"),
  (
    "// Esto es un comentario",
    "/* Esto es un comentario */",
    "-- Esto es un comentario",
    "# Esto es un comentario",
  ),
  ("=", "==", "!=", "==="),
]
# Índice de la respuesta correcta para cada pregunta, el el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]

# El usuario deberá contestar 3 preguntas
score = 0.0
questions_to_ask = random.sample(list(zip(questions,answers, correct_answers_index)), k=3) # En esta linea, se cambia el choices por sample para no repetir.
for question, ans, correct_index in questions_to_ask:
  # Se selecciona una pregunta aleatoria
  print(question)
# Se muestra la pregunta y las respuestas posibles
  for i, option in enumerate(ans):
    print(f"{i + 1}. {option}")
  # El usuario tiene 2 intentos para responder correctamente
  for intento in range(2):
    user_input = input("Respuesta: ")
    if (not user_input.isdigit() or (int(user_input) - 1 < 0) or (int(user_input) - 1 > 4)): #Se verifica si lo ingresado es un digito o no.
      print(f'Respuesta no válida.')
      import sys
      sys.exit(1)
    user_input = int(user_input)
    # Se verifica si la respuesta es correcta
    user_input -= 1 # Ajustoel indice
    if user_input == correct_index:
        print("¡Correcto!")
        score += 1
        break
  else:
    # Si el usuario no responde correctamente después de 2 intentos,
    # se muestra la respuesta correcta
    print("Incorrecto. La respuesta correcta es:")
    print(ans[correct_index])
    score -= 0.5
  # Se imprime un blanco al final de la pregunta
  print()
print (f'El juego terminó! El puntaje final fue de {score} puntos.')