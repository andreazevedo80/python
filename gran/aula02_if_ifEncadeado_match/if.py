# Estrutura de condição simples e composta

n1 = 10
n2 = 4
n3 = 6
n4 = 2

soma = n1 + n2 + n3 + n4
media = soma / 4

print("A soma das notas é: ", soma)
print("A média do aluno é: ",media)
print("")
if media >= 7:
    print("O aluno está Aprovado")
else:
    print("O aluno está Reprovado")


# Estrutura de condição simples e composta usando o método Object Calisthenics

n1 = 10
n2 = 4
n3 = 6
n4 = 2

soma = n1 + n2 + n3 + n4
media = soma / 4

print("A soma das notas é: ", soma)
print("A média do aluno é: ",media)
print("")
aprovado = media >= 7
if aprovado:
    print("O aluno está Aprovado")
if not aprovado:
    print("O aluno está Reprovado")
