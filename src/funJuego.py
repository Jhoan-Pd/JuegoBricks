def iniciar_juego():
    print("¡Iniciando juego!!!")

def mover_personaje(direccion):
    print(f"Moviendo personaje hacia {direccion}")

def finalizar_juego():
    print("¡Fin del juego!!")

def calcular_puntaje(base, multiplicador):
    return base * multiplicador

# Ejecución
iniciar_juego()
mover_personaje("derecha")
finalizar_juego()