'''
Este programa exibe a tabuada de qualquer número escolhido pelo usuário.
Ele repete o processo até que o usuário decida parar digitando 'n'.
'''

continuar = True
'''
- Define uma variável (continuar) booleana (verdadeiro ou falso).
- Serve como controle do laço while, para repetir ou parar o programa.
- Inicialmente, é definido como verdadeiro (True).
'''

while continuar:    
    n = int(input("Qual tabuada você quer? "))
    print("-" * 15)
    print("Tabuada do", n)
    print("-" * 15)
    for i in range(1, 11):
        
        print(f"{n} x {i} = {n * i}")
    continuar = input("Deseja continuar? (s/n): ")
    continuar = True if continuar == "s" else False

'''
while continuar:
- Laço de repetição que continua rodando enquanto continuar for True.
- Usado para permitir que o usuário veja várias tabuadas sem precisar reiniciar o programa.
- O laço while continua enquanto a variável for verdadeira.
- Quando o usuário digita "n", a variável se torna falsa (False) e o Laço while para.
- O laço while é uma estrutura de repetição que executa um bloco de código enquanto a condição for verdadeira.


n = int(input("Qual tabuada você quer? "))
- Pergunta ao usuário qual número ele quer ver a tabuada.
- int() converte a entrada (que é texto) para número inteiro.
- O número digitado pelo usuário é armazenado na variável n.
- A variável n é usada para calcular a tabuada.

"–" * 15 imprime uma linha com 15 traços.

for i in range(1, 11):
- Laço que repete de 1 até 10.
- Mostra as multiplicações de n com os valores de 1 a 10.
- i é a variável que controla o laço.

print(f"{n} x {i} = {n * i}")
- Mostra o resultado da multiplicação usando f-string.
- f-strings são modernas e deixam o código mais limpo e fácil de ler.
- Substitui o valor de n e i na string, mostrando a multiplicação.

continuar = input("Deseja continuar? (s/n): ")
continuar = True if continuar == "s" else False
- A primeira linha pega a resposta do usuário.
- A segunda transforma a resposta em True ou False:
- Se digitar "s" → continua (True)
- Se digitar qualquer outra coisa → para (False)
- Isso permite que o usuário decida se quer continuar vendo mais tabuadas ou não.
- O programa termina quando o usuário digita "n".
'''