nome = [""]

nomes = input('Olá, Tudo bem com o Sr.(a)? Seja bem vindo ao programa de cadastro. Por favor, digite seu nome:')

escolha = input("Digite a opção que deseja: \n 1-Cadastar \n 2-Consultar \n 3-Excluir \n 4-Sair \n ")


if 'Adicionar':
    print('Escolha o nome que deseja cadastrar:')
elif 'Consultar':
    print('Deseja consultar a lista:')
elif 'Excluir':
    print('Qual nome deseja excluir:')
else:
    print('Saindo do programa...')