import random

class robo:
    def __init__(self, nome:str):
        self.nome = nome
        self.vida = round(random.uniform(0.1, 1.0), 2)

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, novoNome) -> None:
        self.__nome = novoNome

    @property
    def vida(self) -> float:
        return self.__vida

    @vida.setter
    def vida(self, novaVida) -> None:
        if(novaVida > 1.0):
            novaVida = 1
            
        self.__vida = novaVida

    def __repr__(self) -> str:
        return f"Robô: {self.nome}\nVida: {self.vida:.2f}"

    def __add__(self, robo2:'robo') -> 'robo':
        from roboMedico import roboMedico
        from roboLutador import roboLutador               #evita erro de import circular
        
        if ("-" in self.nome) or ("-" in robo2.nome):
            primeiro_nome = self.nome.split("-")[0]
            segundo_nome = robo2.nome.split("-")[0]
        else:
            primeiro_nome = self.nome.split()[0]
            segundo_nome = robo2.nome.split()[0]

        if(type(self) == type(robo2)):
            
            if(isinstance(self, roboMedico)):
                robo_filho = roboMedico(primeiro_nome + '-' + segundo_nome)

            elif(isinstance(self, roboLutador)):
                robo_filho = roboLutador(primeiro_nome + '-' + segundo_nome)

            else:
                robo_filho = robo(primeiro_nome + '-' + segundo_nome)

        else:
            if(isinstance(self, roboMedico) and isinstance(robo2, roboLutador)) or (isinstance(self, roboLutador) and isinstance(robo2, roboMedico)):
                robo_filho = robo(primeiro_nome + '-' + segundo_nome)

            elif(isinstance(self, roboMedico) or isinstance(robo2, roboMedico)):
                robo_filho = roboMedico(primeiro_nome + '-' + segundo_nome)

            elif(isinstance(self, roboLutador) or isinstance(robo2, roboLutador)):
                robo_filho = roboLutador(primeiro_nome + '-' + segundo_nome)

        print(f"{primeiro_nome + '-' + segundo_nome} nasceu!\n")
        return robo_filho
    
    def precisa_de_medico(self) -> bool:
        if(self.vida < 0.30):
            return True
        else:
            return False
        
    def __lt__(self, robo2:'robo'):
        return self.vida < robo2.vida
