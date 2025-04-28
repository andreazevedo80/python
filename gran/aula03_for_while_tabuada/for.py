'''
Este programa exibe a tabuada do 2, do 1 ao 10, usando várias formas diferentes de escrever o mesmo print.
Ou seja, ele mostra que dá pra exibir o mesmo resultado usando diferentes estilos de formatação em Python.
'''

'''
 Laço for com range:
 - Repete o bloco de código para cada número de 1 até 10 (inclusive 1, exclusivo 11).
 - A variável i assume os valores de 1 a 10, um por vez.
 - Dentro do Laço, usamos i para calcular o resultado da multiplicação.
 - O resultado é impresso na tela.
 - O range(1, 11) significa que o loop começa em 1 e vai até 10 (11 não entra).
 - O range é uma função que gera uma sequência de números.
 - O i é a variável que vai receber cada número da sequência.
 - O i é incrementado automaticamente a cada iteração do loop.
'''

for i in range(1, 11):
    #escrevendo o print de várias formas
    
    # 1ª forma (forma mais simples)
    print("2 x ", i, " = ", 2 * i)
    '''
    - As vírgulas separam os valores e o Python insere um espaço automático entre eles.
    - Isso é útil para imprimir várias coisas juntas.
    - Mas pode ser confuso, pois não dá pra controlar o espaçamento.
    - O resultado é: 2 x 1 = 2, 2 x 2 = 4, etc.
    '''
    
    # 2ª forma (usando o método format())
    print("2 x {} = {}".format(i, 2 * i))
    '''
    - Os {} são "espaços" que serão preenchidos pelos valores dentro de .format().
    - O primeiro {} é substituído por i e o segundo {} por 2 * 1.
    '''
    
    #3ª forma (usando f-string)
    print(f"2 x {i} = {2 * 1}")
    '''
    - f-strings são mais modernas, simples e legíveis.
    - O f antes da string permite inserir variáveis diretamente com {}.
    -- É mais fácil de ler e entender.    '''
    
    # 4ª forma (usando o método join())
    print("2 x " + str(i) + " = " + str(2 * (i)))
    '''
    - Concatena strings usando +.
    - Usa str() para transformar números em texto (senão dá erro).
    - 
    '''
    
    # 5ª forma (usando o método %)
    print ("2 x %d = %d" % (i, 2 * i))
    '''
    - %d é um "espaço" para número inteiro.
    - É uma forma mais antiga, mas ainda usada.
    - %d formata o número como inteiro (ex: 2, 4).
    - % é o operador de formatação.
    - Isso é útil para mostrar números inteiros.
    '''
    
    # 6ª forma (usando o método % com float)
    print ("2 x %.2f = %.2f" % (i, 2 * i))
    '''
    - %.2f é um "espaço" para número decimal com 2 casas.
    - %f é para float (número decimal).
    - %.2f formata o número como float com 2 casas decimais (ex: 2.00, 4.00).
    - Isso é útil para mostrar valores monetários ou precisões.
    '''
    
    # 7ª forma (usando o método % com float e str)
    print ("2 x %.2f = %s" % (i, 2 * i))
    '''
    - Mesmo esquema, mas o resultado (%s) vira texto (string).
    - %s é um "espaço" para string (texto).
    - %s formata o número como string (ex: "2", "4").
    - Isso é útil quando você quer misturar texto e números.
    '''

'''
Quando usar essas formas?

Forma                       |	Quando usar
Simples com vírgulas	    |   Rápida e fácil, mas com menos controle
.format()                   |	Boa compatibilidade com versões mais antigas do Python
f-string                    |	Recomendada! Moderna, clara e prática
+ e str()                   |	Funciona, mas é menos elegante
%                           |	Antiga, mas ainda usada em alguns códigos legados
'''