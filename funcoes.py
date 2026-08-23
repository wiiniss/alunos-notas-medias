# Substituindo os códigos principais para funções
def linhas():
     print('-'*25)
# Apenas 25 linhas para deixar os textos mais bonitos

def cadastrar_aluno(alunos):
 nome = input('\nDigite o nome: ').strip().title()
 idade = int(input('Digite a idade: '))
    
 while True:
        nota = float(input('Digite a nota de 0 a 10: '))
    
        if nota < 0 or nota > 10:
              print('Nota inválida')
        else:
              break
 aluno = {'nome': nome, 'idade': idade, 'nota': nota}
 alunos.append(aluno)
# Cadastrando os alunos.
# O loop na nota para definir que dentro do limite de 0 a 10 continuara repetindo a condicao de digitar a nota até ter um numero válido
# Recebe os parametros do dicionario para nome, idade e nota
# e adiciona o dicionario na lista principal com o .append


def listar_alunos(alunos):
    if not alunos:
        print('Não existem alunos.')
    else:
        for aluno in alunos:

            linhas()
            print(f'\nnome: {aluno['nome']}')
            print(f'idade: {aluno['idade']}')
            print(f'nota: {aluno['nota']}\n')
# Lista todos os alunos e caso nao tenha nenhum aluno ele retorna um texto          

  
def buscar_aluno(alunos):
      
     busca = input('Digite um nome: ').strip().lower()
     encontrou = False

     for aluno in alunos:
           if busca == aluno['nome'].lower():
              
               print(f'\nnome: {aluno['nome']}')
               print(f'idade: {aluno['idade']}')
               print(f'nota: {aluno['nota']}')

               encontrou = True

     if not encontrou:
              print('Aluno não encontrado.')
# Ele busca algum aluno que tenha na lista formatando a entrada para sempre ficar sem espaços e letra minusculas para evitar os erros de formataçao do nome (letra maiuscula e minuscula). o nome escrito de forma errada ainda gera o testo 'Aluno não encontrado'


def remover_aluno(alunos):
        remover = input('Digite um nome: ')
        encontrou = False

        for aluno in alunos:
           if remover == aluno['nome'].lower().strip():
              alunos.remove(aluno)
              print('Aluno removido.')
              encontrou = True
              break
            
        if not encontrou:
           print('Aluno não encontrado.')
# Remove o aluno com o loop para a variavel sempre estar em falso e caso encotnre ela se torna True e volta para o loop do menu principal


def media_alunos(alunos):
         if not alunos:
            print('Não existem alunos.')
         else:
            total = 0

            for aluno in alunos:
             total = total + aluno['nota']

            media = total / len(alunos)
            print(f'\nA média geral das notas é: {media:.2f}')
# Calcula a media total de todos os alunos na lista