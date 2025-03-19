'''
A Multiplicação Inteira de n-bits recebe dois números inteiros x e y de n-bits e retorna o resutado de x * y.

Assim, novamente:

implemente o algortimo abaixo;
teste-o para os 3 casos de valores inteiros: com 4 bits, com 16 bits e com 64 bits. Nestes testes, contabilize o número de iterações que o algoritmo executa, e o tempo gasto.
O algoritmo está dado abaixo:

MULTIPLY(x, y, n) 
   IF (n = 1)
      RETURN x * y.
   ELSE
      m ← ⎡ n / 2 ⎤.
      a ← ⎣ x / 2^m ⎦; b ← x mod 2^m.
      c ← ⎣ y / 2^m ⎦; d ← y mod 2^m.
      e ← MULTIPLY(a, c, m).
      f ← MULTIPLY(b, d, m).
      g ← MULTIPLY(b, c, m).
      h ← MULTIPLY(a, d, m).
      RETURN 2^(2m)*e + 2^m*(g + h) + f.
Ajuste a assinatura da sua implementação para receber tipo inteiros long (em java).
'''

import random
import time


def multiply(x,y,n):
    global iterations
    iterations += 1
    if(n==1):
        return x*y
    else:
        m = n//2
        a = x//2**m
        b = x % 2**m
        c = y//2**m
        d = y % 2**m
        e = multiply(a,c,m)
        f = multiply(b,d,m)
        g = multiply(b,c,m)
        h = multiply(a,d,m)
        return 2**(2*m)*e + 2**m*(g + h) + f
    
tam = [4, 16, 64]
for t in tam:
    iterations = 0

    x = random.randint(2**(t-1), 2**t - 1)
    y = random.randint(2**(t-1), 2**t - 1)

    start_time = time.time()
    result = multiply(x, y, t)
    end_time = time.time()

    print(f"\nMultiplicação de {t} bits:")
    print(f"x = {x}, y = {y}")
    print(f"Resultado: {result}")
    print(f"Tempo gasto: {end_time - start_time:.6f} segundos")
    print(f"Iterações: {iterations}")