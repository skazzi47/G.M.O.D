# É SEMELHANTE AO CONSOLE.READLINE DO CSharp , e além disso ele já integra uma mensagem antes da leitura da variável, poupando uma linha de codigo para escrever por exemplo("insira o valor da variável") na linha de codigo acima.
num = int(input("Informe o 1º número: "))
num2 = int(input("Informe o 2º número: "))
#É possível fazer a atribuição de valor a uma variável sem o uso do ;
result = num + num2
#Essa linha de código faz a interpolação de variáveis usando o comando ".format" como mostrado abaixo, direto no comando "print" sem a necessidade de criar uma variável só para isso.
print("| {} + {} = {} |".format(num, num2, result))