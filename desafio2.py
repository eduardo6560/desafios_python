# Desafio 2: crie um programa que leia N números inteiros e mostre a quantidade de números positivos e negativos digitados.

# A função 'def rodar()' serve para executar este programa quando ele for chamado por outro código.
# Caso queira testar este arquivo diretamente, apague a linha do 'def rodar()' e ajuste a indentação (espaços).
def rodar():
    print("Executando o código do exercício 2...")
    c = int(input("quantos números você quer digitar? "))
    cp =0
    cn =0
    while c > 0:

        n = int(input("número:"))
        if n > 0:
            cp += 1
        elif n < 0:
            cn += 1
        c -= 1
    print(f"Quantidade de números positivos: {cp}")
    print(f"Quantidade de números negativos: {cn}")