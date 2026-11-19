# Desafio 6: lê vários números, calcula uma das opções: soma, média, maior ou menor valor.

# A função 'def rodar()' serve para executar este programa quando ele for chamado por outro código.
# Caso queira testar este arquivo diretamente, apague a linha do 'def rodar()' e ajuste a indentação (espaços).
def rodar():
    print("Executando o código do exercício 6...")
    print("Digite uma quantidade de números e escolha se quer calcular a soma, a média, o maior ou o menor valor.")

    
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
    


