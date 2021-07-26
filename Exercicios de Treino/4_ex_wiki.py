# Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% 
# e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. 
# Faça um programa que calcule e escreva o número de anos necessários para que a população do 
# país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

popA = float(input('Qual a população da cidade A: '))
popB = float(input('Qual a população da cidade B: '))
anos = 0
cresA = float(input("informe a taxa de crescimento da população da cidade A "))
cresB = float(input("informe a taxa de crescimento da população da cidade B "))

while (popA < popB):
    popA += round((popA * cresA)/100)
    popB += round((popA * cresA)/100)
    anos = anos + 1

print("Após %i anos o país A ultrapassou o país B em número de habitantes." % anos)
print("País A: %.0f" % popA)
print("País B: %.0f" % popB)
