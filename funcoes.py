# Substituindo os códigos principais para funções

def cadastrar_aluno(alunos):
 nome = input('\nDigite o nome: ')
 idade = int(input('Digite a idade: '))
    
 while True:
        nota = float(input('Digite a nota de 0 a 10: '))
    
        if nota < 0 or nota > 10:
              print('Nota inválida')
        else:
              break
 aluno = {'nome': nome, 'idade': idade, 'nota': nota}
 alunos.append(aluno)


def listar_alunos(alunos):
    if not alunos:
        print('Não existem alunos.')
    else:
        for aluno in alunos:

            print(f'\nnome: {aluno['nome']}')
            print(f'idade: {aluno['idade']}')
            print(f'nota: {aluno['nota']}\n')

            
        