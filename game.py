from robo import robo
from roboMedico import roboMedico
from roboLutador import roboLutador

r1 = roboMedico("Fofinho Pereira")
r2 = roboLutador("Fofao Oliveira")

r3 = roboMedico("Bravinho da Silva")
r4 = roboLutador("Bravão Santos")

r5 = r4 + r3
print(r5)