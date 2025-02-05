import random
from robo import robo

class roboLutador(robo):
    def __init__(self, nome):
        super().__init(nome)
        self.dano_max = 0.3
        self.poder = round(random.uniform(self.dano_max, 1), 2)

    def atacar(self, robo2:'robo') -> None:
        robo2.vida = (1 - self.poder) * robo2.vida
        print(f"{robo2.nome}: Ouch!")

        if(isinstance(robo2, roboLutador)):
            self.vida = (1 - robo2.poder) * self.vida
            print(f"{self.nome}: Ouch!")
        