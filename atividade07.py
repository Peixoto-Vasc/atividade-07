# Enunciado: Uma loja aplica um imposto de 12% sobre o valor dos produtos. Crie um programa que receba o preço de um produto e calcule o preço final com o imposto incluído.
produto = int(input("Digite o preço do seu produto:"))
imposto = produto * 12/100
valorfinal = produto + imposto
print(f"O valor final com imposto de 12% ficou: {valorfinal}")