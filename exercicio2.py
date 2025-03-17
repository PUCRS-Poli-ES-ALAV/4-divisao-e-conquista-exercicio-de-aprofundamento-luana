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

def maxVal1(A):
    max = A[0]
    for i in range(1,len(A)): 
        if(A[i] > max ):
           max = A[i]
    return max

print(maxVal1([556,6,22,0,2,86,32,8647,1,531]))