# Desafio 7: blibioteca de exercícios de lógica de programação em Python.

# o import com o nome dos demais arquivos permite que você execute os exercícios de 1 a 6, chamando a função 'rodar()' de cada arquivo.

import desafio
import desafio2
import desafio3
import desafio4
import desafio5
import desafio6

mais = 's'
while mais == 's':

    print("--- MENU DE EXERCÍCIOS ---")
    print("Escolha qual exercício você quer executar (de 1 a 6):")
    escolha = input("Digite o número: ")

    if escolha == "1":
        desafio.rodar() 
    elif escolha == "2":
        desafio2.rodar()
    elif escolha == "3":
        desafio3.rodar()
    elif escolha == "4":
        desafio4.rodar()
    elif escolha == "5":
        desafio5.rodar()
    elif escolha == "6":
        desafio6.rodar()
    else:
        print("Opção inválida! Digite um número de 1 a 6.")
    mais = input("você quer fazer mais alguma coisa? (s/n): ")
print("Obrigado por usar o programa!")