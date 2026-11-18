# Desafio 3: crie um programa que leia N números inteiros e mostre a soma, a média e a quantidade de números acima da média digitados.

# A função 'def rodar()' serve para executar este programa quando ele for chamado por outro código.
# Caso queira testar este arquivo diretamente, apague a linha do 'def rodar()' e ajuste a indentação (espaços).
def rodar():
    print("Executando o código do exercício 3...")
    q = int(input("quantos números você quer digitar? "))
    numeros = []
    c = 0
    t = 0
    m = 0
    if q > 0:
        while c < q:
                
                n = int(input("número:"))
                numeros.append(n)
                t += n
                c += 1
                m = t / c

        quantidade = sum(1 for num in numeros if num > m)

        print(f"números: {numeros}")
        print(f"soma: {t}")
        print(f"média: {m}")
        print(f"quantidade de números acima da média: {quantidade}")
    else:
        print("Você não digitou nenhum número válido.")