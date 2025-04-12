import copy


class Enemigo:
    def clonar(self):
        return copy.deepcopy(self) #devolver una copia exacta del objeto


class Zombi(Enemigo):
    def __init__(self, vida, daño, velocidad):
        self.vida = vida
        self.daño = daño
        self.velocidad = velocidad

    def __str__(self):
        return f"Zombi {{vida={self.vida}, daño={self.daño}, velocidad={self.velocidad}}}" #como se vera el zombi

# Simulación del juego
def juego():
    zombi_base = Zombi(100, 10, 1.5) #se crea un zombi base

    zombi1 = zombi_base.clonar()
    zombi2 = zombi_base.clonar()

    # Personalizar clones
    zombi1.vida = 120
    zombi2.velocidad = 2.0

    print("Zombi base:", zombi_base)
    print("Zombi 1:", zombi1)
    print("Zombi 2:", zombi2)

# Ejecutar
juego()
