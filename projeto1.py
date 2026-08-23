from funcoes import cadastrar_aluno, listar_alunos 

alunos = []

while True: 

#Menu feito dentro do while para sempre estar no loop 

    print('   \nMENU PRINCIPAL\n')
    print('1. Adicionar aluno')
    print('2. Listar todos os alunos')
    print('3. Buscar aluno pelo nome') 
    print('4. Remover aluno')
    print('5. Mostrar média geral das notas')
    print('6. Sair')

# declarando a variavel opção para fazer o menu ser interativo

    opcao =  int(input('\nDigite um número válido do menu: '))

    if opcao == 1:
       cadastrar_aluno(alunos)

   #  if opcao == 1:
   #      nome = input('\nDigite o nome: ')
   #      idade = int(input('Digite a idade: '))
   #      while True:
   #          nota = float(input('Digite a nota de 0 a 10: '))
    
   #          if nota < 0 or nota > 10:
   #           print('Nota inválida')
   #          else:
   #           break

   

# # colocando uma trava para ser digitado apenas nota de 0 a 10 e exibir uma mensagem caso digite algo fora desses parametros        

#         aluno = {'nome': nome, 'idade': idade, 'nota': nota}
#         alunos.append(aluno)

# # a opção 1 é o adicionar aluno onde as informações nome, idade e nota são guardados em forma de dicionario para dentro de uma lista

    elif opcao == 2:
      listar_alunos(alunos)
           
#         if not alunos:
#            print('Não existem alunos.')
#         else:
#            for aluno in alunos:
              
#               print(f'\nnome: {aluno['nome']}')
#               print(f'idade: {aluno['idade']}')
#               print(f'nota: {aluno['nota']}')

# # a opção 2 é a listar todos os alunos que está em uma condição de for para listar todos os alunos que foram cadastrados

#     elif opcao == 3:
#        busca = input('Digite um nome: ')
#        encontrou = False

#        for aluno in alunos:
#           if busca == aluno['nome']:
              
#               print(f'\nnome: {aluno['nome']}')
#               print(f'idade: {aluno['idade']}')
#               print(f'nota: {aluno['nota']}')

#               encontrou = True

#        if not encontrou:
#              print('Aluno não encontrado.')

# # a opção 3 é para buscar um aluno pelo nome e mostrar todos seus dados utilizando o True e False para = encontrou fica false, começa a procurar os nomes, encontrou ? não então continua procurando. Se encontrou vira True e mostra os dados
# # de qualquer forma encontrando ou não ele termina o for, se o encontrou virou True então não acontece nada e volta para o menu principal. Caso continue False ele informa que o aluno não foi encontrado
     
#     elif opcao == 4:
#        remover = input('Digite um nome: ')
#        encontrou = False

#        for aluno in alunos:
#           if remover == aluno['nome']:
#              alunos.remove(aluno)
#              print('Aluno removido.')
#              encontrou = True
#              break
            
#        if not encontrou:
#           print('Aluno não encontrado.')

# # a opção 4 é para remover um aluno cadastrado na lista, com o mesmo conceito de True e False e parando o a busca caso tenha encontrado e removido os dados da lista

#     elif opcao == 5:
#         if not alunos:
#            print('Não existem alunos.')
#         else:
#            total = 0

#            for aluno in alunos:
#             total = total + aluno['nota']

#            media = total / len(alunos)
#            print(f'A média geral das notas é: {media:.2f}')
    
#     elif opcao == 6:
#      break

