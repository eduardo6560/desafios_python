# Desafio 6: lê vários números, calcula uma das opções: soma, média, maior ou menor valor.

# A função 'def rodar()' serve para executar este programa quando ele for chamado por outro código.
# Caso queira testar este arquivo diretamente, apague a linha do 'def rodar()' e ajuste a indentação (espaços).
def rodar():
    print("Executando o código do exercício 6...")
    print("Faça um programa que leia vários números e mostre no final a soma, a média, o maior e o menor valor. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.")

    
    print("soma = s, média = m, maior = max, menor = min")
    escolhas = input("o que você quer fazer? (s, m, max, min): ")
    g = int(input("quantos números você quer digitar? "))
    c = 0
    if g <= 0:
        print("Quantidade inválida.")
        return

    while c < g:
        c += 1
        n = int(input("número:"))
        if c == 1:
            s = n
            max = n
            min = n
        else:
            s += n
            if n > max:
                max = n
            if n < min:
                min = n

    if escolhas == "s":
        print(f"soma = {s}")
    elif escolhas == "m":
        print(f"média = {s/g}")
    elif escolhas == "max":
        print(f"maior = {max}")
    elif escolhas == "min":
        print(f"menor = {min}")
    else:
        print("Opção inválida.")
    


