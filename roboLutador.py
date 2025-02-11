import random
from robo import robo

class roboLutador(robo):
    def __init__(self, nome):
        super().__init__(nome)
        self.dano_max = 0.3
        self.poder = round(random.uniform(self.dano_max, 1), 2)

    def atacar(self, robo2:'robo') -> None:

        if self.vida > 0.009:
            robo2.vida = (1 - self.poder) * robo2.vida
            print(f"{self.nome} ATACOU {robo2.nome}")
            print(f"{robo2.nome}: Ouch!")
            print(f"{robo2.vida:.2f}\n")

            if(isinstance(robo2, roboLutador) and robo2.vida > 0.009):

                self.vida = (1 - robo2.poder) * self.vida
                print(f"{robo2.nome} ATACOU {self.nome}")
                print(f"{self.nome}: Ouch!")
                print(f"{self.vida:.2f}\n")
            else:
                print(f"{robo2.nome} está fraco e não pode atacar!\n")
        else:
            print(f"{self.nome} está fraco e não pode atacar!\n")
            
