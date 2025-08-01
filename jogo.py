# Entrada do nome e da idade (funções built-in)
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

# Estrutura condicional para verificar se pode votar
if idade < 16:
    situacao = "Você ainda não pode votar."
elif idade >= 16 and idade < 18:
    situacao = "Voto opcional (facultativo)."
elif idade >= 18 and idade <= 70:
    situacao = "Voto obrigatório."
else:
    situacao = "Voto opcional por idade."

# Exibindo o resultado 
print(f"\nOlá, {nome}!")
print(f"Com {idade} anos: {situacao}")
