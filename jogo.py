
nome = input("Digite seu nome: ") #digita valor, "pergunta"

idade = None 

while True:  # laço que continua até que a condição de parar funcione
    try: #tenta executar o que esta dentro dele 
        idade = int(input("Digite sua idade: "))  
        if idade < 0:  # verifica se a idade é negativa, tbm válidas
            print("Por favor, digite uma idade válida.") 
        else:
            break  # sai do loop se a idade for válida
    except ValueError:  #captura exceções (except), caso try nn der certo
        print("Por favor, digite um número inteiro.") 

faixas = [
    (16, "Você ainda não pode votar."), 
    (18, "Voto opcional (facultativo)."),  
    (70, "Voto obrigatório.")
]


situacao = ""  # variável que armazena a mensagem correspondente à situação de voto


for limite, mensagem in faixas:  # laço que percorre cada faixa etária 
    if idade < limite:  # verifica se a idade é menor que o limite
        situacao = mensagem  # atribui a mensagem correspondente
        break  # sai do laço 


print(f"\nOlá, {nome}!") 
print(f"Com {idade} anos: {situacao}") 
