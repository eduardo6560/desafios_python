# Desafio 5: Faça um programa que leia N números inteiros. Em seguida, mostre na tela o maior número e a média dos valores lidos.

# A função 'def rodar()' serve para executar este programa quando ele for chamado por outro código.
# Caso queira testar este arquivo diretamente, apague a linha do 'def rodar()' e ajuste a indentação (espaços).
def rodar():
    print("Executando o código do exercício 5...")
    q = int(input("quantos números você quer digitar? "))
    c = 1
    s = 0
    m = 0
    if q > 0:
        n = int(input("número:"))
        s = n
        max = n
        while c < q:
                
            c += 1
            n = int(input("número:"))
            s += n
            if n > max:
                max = n
        m = s / c
        print(f"soma: {s}")
        print(f"média: {m}")
        print(f"max: {max}")
    else:
        print("Você digitou um número inválido.")