# Calculadora simples
# Autor: Hudson Rodrigo
# Descricao: Calculadora com as 4 operacoes basicas

print("Bem-vindo a calculadora do Hudson!")

# Funcao de soma
def somar(a, b):
    return a + b

# Funcao de subtracao
def subtrair(a, b):
    return a - b

# Funcao de multiplicacao
def multiplicar(a, b):
    return a * b

# Funcao de divisao com protecao contra divisao por zero
def dividir(a, b):
    if b == 0:
        return "Erro: divisao por zero"
    return a / b

# Menu principal
print("=== Calculadora ===")
print("1 - Somar")
print("2 - Subtrair")
print("3 - Multiplicar")
print("4 - Dividir")

opcao = input("Escolha uma opcao: ")
a = float(input("Digite o primeiro numero: "))
b = float(input("Digite o segundo numero: "))

if opcao == "1":
    print("Resultado:", somar(a, b))
elif opcao == "2":
    print("Resultado:", subtrair(a, b))
elif opcao == "3":
    print("Resultado:", multiplicar(a, b))
elif opcao == "4":
    print("Resultado:", dividir(a, b))
else:
    print("Opcao invalida")