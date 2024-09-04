'''
2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...),
escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência. 
IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código; 
'''
def pertence_fibonacci(numero):
    '''Verifica se um número pertence à sequência de Fibonacci e retorna a sequência até o número fornecido.'''
        
    fib_1 = 0
    fib_2 = 1
    sequencia = [fib_1, fib_2] 
    
    if numero == 0 or numero == 1:
        return True, [0] if numero == 0 else [0, 1]

    while fib_2 < numero:
        fib_1, fib_2 = fib_2, fib_1 + fib_2
        sequencia.append(fib_2)  
    
    pertence = numero == fib_2
    return pertence, sequencia

numero = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))
pertence, sequencia = pertence_fibonacci(numero)
print("Sequência de Fibonacci:", sequencia)

if pertence:
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")

