from random import choice
from robo import robo
from roboMedico import roboMedico
from roboLutador import roboLutador

r1 = roboMedico("João Impar")
r2 = roboMedico("Maria Par")
r3 = roboMedico("Josefina Impar")
r4 = roboMedico("Pedro Par")

r5 = roboLutador("Carlos Impar")
r6 = roboLutador("Lucas Par")
r7 = roboLutador("Sofia Impar")
r8 = roboLutador("Gabi Par")

lutador_time_par = [r6, r8]
lutador_time_impar = [r5, r7]

medico_time_par = [r2, r4]
medico_time_impar = [r1, r3]

####################################### TIME PAR VS TIME IMPAR #######################################

for i in range(100):

    if i == 0:
        print("START -> VOCÊ É TIME PAR\n")

    if all(r.vida <= 0.009 for r in lutador_time_par):
        print("\nTodos os robôs do time par foram destruídos! FIM DE JOGO")
        exit()
    elif all(r.vida <= 0.009 for r in lutador_time_impar):
        print("\nTodos os robôs do time impar foram destruídos! VITÓRIA!")
        exit()

    print("\nO que fazer a seguir?\n")
    print("1. Atacar\n2. Curar\n3. Reproduzir\n4. Ver status do time\n5. Sair do jogo")   #usuário é sempre time par
    escolha = int(input())

    match escolha:
        case 1:
            print("\n--------------------\n")
            atacante = choice(lutador_time_par)
            alvo = choice([r for r in lutador_time_impar if r != atacante])
            atacante.atacar(alvo)
            print("--------------------\n")
        
        case 2:
            print("\n--------------------\n")
            curador = choice(medico_time_par)
            paciente = min(lutador_time_par)
            if(curador.curar(paciente) == False):
                atacante = choice(lutador_time_impar)
                alvo = choice(medico_time_par)          #se a cura falhar, um médico é atacado
                atacante.atacar(alvo)
            print("--------------------\n")

        case 3:
            print("\n--------------------\n")
            print("Pai deve ser lutador? s/n")
            escolha_rep = input()
            if escolha_rep == 's':
                pai = choice(lutador_time_par)
            else:
                pai = choice(medico_time_par)

            print("Mãe deve ser lutador? s/n")
            escolha_rep = input()
            if escolha_rep == 's':
                mae = choice([r for r in lutador_time_par if r != pai])
            else:
                mae = choice([r for r in medico_time_par if r != pai])

            filho = pai + mae
            if(isinstance(filho, roboLutador)):
                lutador_time_par.append(filho)
            else:
                medico_time_par.append(filho)

            print("--------------------\n")

        case 4:
            print("\n------SEU TIME------\n")
            j = 0
            while j < len(medico_time_par):
                print(f"{medico_time_par[j]}\nTipo: {type(medico_time_par[j]).__name__}\n")
                j += 1

            j = 0
            while j < len(lutador_time_par):
                print(f"{lutador_time_par[j]}\nTipo: {type(lutador_time_par[j]).__name__}\n")
                j += 1

            print("--------------------\n")

        case _:
            print("--------------------\n")
            print("FIM DE JOGO")
            print("--------------------\n")
            exit()

print("EMPATE! FIM DE JOGO.")
