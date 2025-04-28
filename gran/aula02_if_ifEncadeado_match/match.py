
'''
Este programa pede ao usuário para digitar um número de 1 a 7 e, com base nesse número, imprime o dia da semana correspondente (1 = Domingo, 2 = Segunda, etc.). Se o número for diferente de 1 a 7, ele mostra "Número inválido".
'''

dia = int(input("Digite um número de 1 a 7: "))

'''
input(...): exibe uma mensagem pedindo que o usuário digite algo.

int(...): transforma o que o usuário digitar (que vem como texto) em número inteiro.

O valor é guardado na variável dia.
'''

'''
# Usando o if-elif-else para verificar o dia da semana
if dia == 1:
    print("Domingo")
elif dia == 2:
    print("Segunda")
elif dia == 3:
    print("Terça")
elif dia == 4:
    print("Quarta")
elif dia == 5:
    print("Quinta")
elif dia == 6:
    print("Sexta")
else:
    print("Sábado")    
'''

# Usando o match-case para verificar o dia da semana
match dia:
    case 1:
        print("Domingo")
    case 2:
        print("Segunda")
    case 3:
        print("Terça")
    case 4:
        print("Quarta")
    case 5:
        print("Quinta")
    case 6:
        print("Sexta")
    case 7:
        print("Sábado")
    case other:
        print("Número inválido")
    
'''
match é uma estrutura nova (a partir do Python 3.10) parecida com o switch de outras linguagens.

Cada case verifica se dia é igual ao número.

case other: é como um “caso padrão”, ou seja, para valores que não foram previstos.
'''

'''
Quando usar esse tipo de código:
- Quando você quer fazer escolhas baseadas em um único valor (como menus, seleções por número, opções de usuário).
- A estrutura match-case é ideal quando há muitas comparações simples, deixando o código mais limpo que vários if...elif...else.
'''

