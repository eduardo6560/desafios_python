# Desafio 1: crie um programa que leia N números inteiros e mostre o segundo maior número digitado.

# A função 'def rodar()' serve para executar este programa quando ele for chamado por outro código.
# Caso queira testar este arquivo diretamente, apague a linha do 'def rodar()' e ajuste a indentação (espaços).

def rodar():
    print("Executando o código do exercício 1...")
    n = int(input("quantos números você quer digitar? "))
    c = 0
    g = 0
    g2 =0

    while c < n:
        n2 = int(input("Digite um número inteiro: "))
        if n2 > g2 and n2 < g:
            g2 = n2
        elif n2 > g:
            g2 = g
            g = n2
        else:
            pass

        c += 1

    print(f"Saída: {g2}")