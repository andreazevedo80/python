# Estrutura de condição simples e composta encadeado

n1 = 10
n2 = 7
n3 = 5
n4 = 7

soma = n1 + n2 + n3 + n4
media = soma / 4

print("A soma das notas é: ", soma)
print("A média do aluno é: ",media)
print("")
if media >= 7:
    print("O aluno está Aprovado")
elif media >= 5:
    print("O aluno está de Recuperação")
else:
    print("O aluno está Reprovado")
