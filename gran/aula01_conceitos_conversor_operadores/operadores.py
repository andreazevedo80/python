n1 = int(input("Digite um número inteiro diferente de 0: "))
n2 = int(input("Digite outro número inteiro diferente de 0: "))
media = 6
minimo = 5

# Variáveis Operados aritméticos
soma = n1 + n2
subtracao = n1 - n2
multiplicacao = n1 * n2
divisao = n1 / n2
resto = n1 % n2

print("Operadores Aritméticos")

print("A soma dos números é: ", soma)
print("A subtracao dos números é: ", subtracao)
print("A multiplicao dos números é: ", multiplicacao)
print("A divisao dos números é: ", divisao)
print("O resto da divisão dos números é:  ", resto)

#Variáveis Operadores relacionais
igualdade = n1 == n2
diferenca = n1 != n2
menorque = n1 < n2
maiorque = n1 > n2
menorOuIgual = n1 <= n2
maiorOuIgual = n1 >= n2


print ("")
print("Operadores Relacionais")
print("O número ", n1, "é igual o número ", n2, " ? ", igualdade)
print("O número ", n1, "é diferente do número ", n2, " ? ", diferenca)
print("O número ", n1, "é menor que o número ", n2, " ? ", menorque)
print("O número ", n1, "é maior que o número ", n2, " ? ", maiorque)
print("O número ", n1, "é menor ou igual ao número ", n2, " ? ", menorOuIgual)
print("O número ", n1, "é maior ou igual ao número ", n2, " ? ", maiorOuIgual)


#Variáveis Operadores Lógico
aprovado = n1 >= minimo and n2 >= minimo and ((n1 + n2)/2) >= media
aprovadoD  = n1 >= minimo or n2 >= minimo and ((n1 + n2)/2) >= media
reprovado = not aprovado and not aprovadoD

print("")
print("O aluno foi aprovado?" " (nota 01 e nota 2, maior ou igual a nota mínima", "(", minimo, ")", "e média, maior ou menor que a média ", "(",media,")" ,") ?", aprovado)
print("O aluno foi aprovado com dependência?" " (nota 01 ou nota 2, maior ou igual a nota mínima", "(", minimo, ")", "média, maior ou menor que a média ", "(",media,")" ,") ?", aprovadoD)
print("o aluno foi reprovado?", reprovado)