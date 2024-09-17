print("\nEscreva um texto para que ele seja exibido na tela: ")
#Não é necessario colocar o tipo "string" antes do comando "input" na hora de ler uma variável, como por exemplo: {num = int(input())} pois o comando "input" por padrão já é configurado para ler strings.
texto = (input("Informe seu texto:  "))
print("\nO texto que você informou:  {} ".format(texto))
#Além da interpolação de variáveis usando o comando ".format", semelhante à linguagem CSharp(C#) que usamos um "$" antes das aspas que iniciam o texto, é possível fazer a interpolação colocando um "f" antes das aspas que inicia o texto à ser imprimido pelo print, veja um exemplo abaixo.
print(f"\nO texto que você informou: '{texto}'")