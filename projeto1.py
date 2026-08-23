from funcoes import cadastrar_aluno, listar_alunos, buscar_aluno, remover_aluno, media_alunos, linhas

alunos = []

while True: 

#Menu feito dentro do while para sempre estar no loop 

    linhas()
    print('   MENU PRINCIPAL')
    linhas()
    print('1. Adicionar aluno')
    print('2. Listar todos os alunos')
    print('3. Buscar aluno pelo nome') 
    print('4. Remover aluno')
    print('5. Mostrar média geral das notas')
    print('6. Sair')
    linhas()

# declarando a variavel opção para fazer o menu ser interativo

    opcao =  int(input('\nDigite um número válido do menu: '))

    if opcao == 1:
       cadastrar_aluno(alunos)

    elif opcao == 2:
      listar_alunos(alunos)


    elif opcao == 3:
       buscar_aluno(alunos)

     
    elif opcao == 4:
       remover_aluno(alunos)


    elif opcao == 5:
       media_alunos(alunos)

    
    elif opcao == 6:
      break
# Quebra o loop e termina o programa

