# piedra_papel_tijera.py
# Juego simple contra la computadora: primera versión

import random

opciones = ["piedra", "papel", "tijera"]

print("¡Bienvenido! Vamos a jugar a Piedra, Papel o Tijera.")
print("Escribí tu jugada (piedra/papel/tijera).")

ronda = 1
puntos_usuario = 0
puntos_pc = 0

while True:
    try:
        rondas_totales = int(input("Ingrese la cantidad de rondas que desea jugar: "))
        if rondas_totales > 0:
            break
        else:
            print("Debe ser un numero mayor a 0.")
    except ValueError:
        print("Entrada inválida. Debe ingresar un número entero.")

while ronda <= rondas_totales:
    print(f"\nRonda {ronda}")
    jugada_usuario = input("Tu jugada: ").strip().lower()
    
    #Vuelve a pedir la jugada hasta que sea valida 
    while jugada_usuario not in opciones:
        print("Entrada no válida. Debe ser piedra, papel o tijera.")
        jugada_usuario = input("Ingrese nuevamente su jugada: ").strip().lower()
 
    jugada_pc = random.choice(opciones)
    print(f"La computadora eligió: {jugada_pc}")
 
    if jugada_usuario == jugada_pc:
        print("Empate.")
        ronda += 1
    elif (
        (jugada_usuario == "piedra" and jugada_pc == "tijera") or
        (jugada_usuario == "papel" and jugada_pc == "piedra") or
        (jugada_usuario == "tijera" and jugada_pc == "papel")
    ):
        print("¡Ganaste la ronda!")
        puntos_usuario += 1
        ronda += 1
    else:
        print("Perdiste la ronda.")
        puntos_pc += 1
        ronda += 1
    
    #Para que el juego se interrumpa si alguno ya no puede ser alcanzado
    
    if puntos_usuario > rondas_totales / 2:
        print (f"FIN DEL JUEGO: GANASTE, ya no podes ser alcanzado")
        break
    elif puntos_pc > rondas_totales / 2:
        print (f"FIN DEL JUEGO: PERDISTE, ya no podes alcanzar al rival")
        break
      

print("\n=== Resultado final ===")
print(f"Tus puntos: {puntos_usuario} | Puntos de la PC:{puntos_pc}")

if puntos_usuario > puntos_pc:
    print("¡Ganaste el juego! 🎉")
elif puntos_usuario < puntos_pc:
    print("La computadora ganó el juego.")
else:
    print("Empate total.")