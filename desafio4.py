# Desafio 4: crie um programa que leia N números inteiros e mostre a quantidade de números pares e ímpares digitados, bem como a soma dos números pares e a soma dos números ímpares.

# A função 'def rodar()' serve para executar este programa quando ele for chamado por outro código.
# Caso queira testar este arquivo diretamente, apague a linha do 'def rodar()' e ajuste a indentação (espaços).
def rodar():
    print("Executando o código do exercício 4...")
    q = int(input("quantos números você quer digitar? "))
    c = 0
    sp = 0
    si = 0
    cp = 0
    ci = 0
    while c < q:
        n = int(input("Digite um número inteiro: "))
        if n % 2 == 0:
            cp += 1
            sp += n
        else:
            ci += 1
            si += n
        c += 1
    print(f"Quantidade de números pares: {cp}")
    print(f"Quantidade de números ímpares: {ci}")
    print(f"total da soma dos números pares: {sp}")
    print(f"total da soma dos números ímpares: {si}")
