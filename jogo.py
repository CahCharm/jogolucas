nome = input("Digite seu nome: ") #digita valor, "pergunta"

idade = None #nenhum -> idade

while True: #while enquanto a cond que ta na frente for vdd ele faz
    try: #tenta executar o que esta dentro dele, se nn der certo -> except
        idade = int(input("Digite sua idade: "))  #todo inpt por padrao é um txt- int p/ converter o txt
        if idade < 0:  # verifica se a idade é negativa, tbm válidas
            print("Por favor, digite uma idade válida.") 
        else:
            break 
    except ValueError:  #captura exceções (except), caso try nn der certo
        print("Por favor, digite um número inteiro.") 

faixas = [
    (16, "Você ainda não pode votar."), 
    (18, "Voto opcional (facultativo)."),  
    (70, "Voto obrigatório.")
]


situacao = "" 


for limite, mensagem in faixas: #outro loop 
    if idade < limite:  # verifica se a idade é menor que o limite
        situacao = mensagem  
        break  # sai do laço 


print(f"\nOlá, {nome}!") 
print(f"Com {idade} anos: {situacao}") 
