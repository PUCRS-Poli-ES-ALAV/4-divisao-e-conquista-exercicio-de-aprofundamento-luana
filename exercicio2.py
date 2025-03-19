'''
O algoritmo a seguir (que não utiliza divisão-e-conquista) encontra o maior valor em um vetor.

Assim, novamente:

implemente o algortimo abaixo;
teste-o para vetores de inteiros com conteúdos randômicos, e tamanho 32, 2048 e 1.048.576. Nestes testes, contabilize o número de iterações que o algoritmo executa, e o tempo gasto;
long maxVal1(long A[], int n) {  
    long max = A[0];
    for (int i = 1; i < n; i++) {  
        if( A[i] > max ) 
           max = A[i];
    }
    return max;
}

'''

import random
import time

def maxVal1(A):
    global iterations
    max = A[0]
    for i in range(1,len(A)): 
        iterations += 1
        if(A[i] > max ):
           max = A[i]
    return max

tam = [32,2048,1048576]
for t in tam:
    iterations = 0
    start_time = time.time()
    random_list = [random.randint(1, 10000) for _ in range(t)]
    max_value = maxVal1(random_list)
    end_time = time.time()
    print("Valor Maximo: ", max_value)
    print("Tempo gasto: ", end_time - start_time)
    print("Iterações: ", iterations)