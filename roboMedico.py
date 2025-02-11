import random
from robo import robo

class roboMedico(robo):
    def __init__(self, nome):
        super().__init__(nome)
        self.poder_de_cura = round(random.random(), 2)

    def curar(self, robo2:'robo') -> bool:
        chance = random.random()

        if(robo2.precisa_de_medico) and (self.vida >= robo2.vida) and (chance > 0.5):
            robo2.vida = robo2.vida + self.poder_de_cura
            print(f"{robo2.nome} foi curado!")
            print(f"{robo2.vida:.2f}\n")
            return True
        else:
            print("A cura falhou...\n")
            return False
