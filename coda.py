#Juego piedra, papel o tijeras
import random
opciones = ["piedra", "papel", "tijera"]
compu = random.choice(opciones)
user = input("¿Piedra, papel o tijera?").lower()
print(f"opción de la comprutadora: {compu}")
print(f"opción de el jugador: {user}")

if user == compu:
    print("empate")
elif (user == "piedra" and compu == "tijera") or (user == "papel" and compu == "piedra") or (user == "tijera" and compu == "papel"):
    print("Ganaste!!")
else:
    print("Perdiste")