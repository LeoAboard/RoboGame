import random
from robo import robo

class roboMedico(robo):
    def __init__(self, nome):
        super().__init__(nome)
        self.poder_de_cura = round(random.random(), 2)

    def curar(self, robo2:'robo') -> None:
        if self.vida >= robo2.vida:
            robo2.vida = robo2.vida + self.poder_de_cura
        else:
            print("A cura falhou...")