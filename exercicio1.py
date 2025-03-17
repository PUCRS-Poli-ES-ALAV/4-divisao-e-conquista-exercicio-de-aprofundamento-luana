'''
Vamos começar com um algorítmo já estudado e conhecido (em AEDI). 
O Merge Sort é um algorítmo de ordenação baseado nos seguintes passos:

recursivamente ordene a metade esquerda do vetor
recursivamente ordene a metade direita do vetor
mescle (faça o merge) das duas metades para ter o vetor ordenado.
Assim:

implemente o algortimo abaixo;
teste-o para vetores de inteiros com conteúdos randômicos, e tamanho 32, 2048 e 1.048.576. Nestes testes, contabilize o número de iterações que o algoritmo executa, e o tempo gasto;
MERGE-SORT(L: List with n elements) : Ordered list with n elements
    IF (list L has one element)
        RETURN L.
    Divide the list into two halves A and B.
    A ← MERGE-SORT(A).
    B ← MERGE-SORT(B).
    L ← MERGE(A, B).
    RETURN L. 
'''
import random
import time

iterations = 0

def merge(left, right):
    global iterations
    result = []
    
    # se esta vazio
    if not left:
        return right
    if not right:
        return left
    
    if left[0] < right[0]: # primeiro elemento de cada metade
        iterations += 1
        result.append(left[0]) # adiciona o menor elemento na lista
        result.extend(merge(left[1:], right))  # chama para o resto dos elementos tirando o primeiro elemento
                                               # repassa as duas metades sem o primeiro elemento
    else:
        iterations += 1
        result.append(right[0])
        result.extend(merge(left, right[1:]))
    
    return result

def merge_sort(l):
    global iterations
    if len(l) <= 1:
        return l
    
    mid = len(l) // 2 #seleciona o meio, // realiza a divisão inteira
    left = merge_sort(l[:mid])
    right = merge_sort(l[mid:])
    
    return merge(left, right)


random_list = [random.randint(1, 10000) for _ in range(32)]
sorted_list = merge_sort(random_list)
print(f"Lista: {sorted_list}")
