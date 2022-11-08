# FAZER SEU CÓDIGO AQUI:

print('\033[036m='*50)
print('           Universidade de Vila Velha')
print('A maior universidade particular do Espirito Santo')
print('='*50)


alunos = []
medias = []
quantidadeAprovado = 0
numeroDeAlunos = int(input('Quantos alunos tem na sua sala? '))
nomeDosAlunos = numeroDeAlunos
totalDeAlunos = numeroDeAlunos



while numeroDeAlunos > 0:
    alunos.append(input('Nome do aluno: '))
    nota1 = float(input('Nota da primeira AOP - * Nota entre 0.0 a 1.0 *: '))
    if nota1 > 1:
        print(f'A nota da primeira AOP, só pode valer até 1 ponto, e você colocou {nota1}')
        exit()
    nota2 = float(input('Nota da segunda AOP - * Nota entre 0.0 a 2.0 *: '))
    if nota2 > 2:
        print(f'A nota da segunda AOP, só pode valer até 2 ponto, e você colocou {nota2}')
        exit()
    nota3 = float(input('Nota da terceira AOP - * Nota entre 0.0 a 1.0 *: '))
    if nota3 > 1:
        print(f'A nota da terceira AOP, só pode valer até 1 ponto, e você colocou {nota3}')
        exit()
    nota4 = float(input('Nota da prova regular - * Nota entre 0.0 a 6.0 *: '))
    if nota4 > 6:
        print(f'A nota da prova 4, só pode valer até 6 ponto, e você colocou {nota4}')
        exit()
    medias.append(nota1 + nota2 + nota3 + nota4)
    numeroDeAlunos = numeroDeAlunos - 1
    print(' ')


while nomeDosAlunos > 0:
    nomeDosAlunos = nomeDosAlunos - 1
    if medias[nomeDosAlunos] < 7:
        print('\033[033m='*50)
        notarecuperacao = float(input(f'Aluno {alunos[nomeDosAlunos]} está quase reprovando, por favor, ensira a nota da prova de recuperação: '))
        
        if notarecuperacao >= 5:
            print('\033[032m='*50)
            print(f'{alunos[nomeDosAlunos]} foi aprovado(a)! e teve a nota final de: {notarecuperacao}')
            quantidadeAprovado = quantidadeAprovado + 1

        else:
            print('\033[031m='*50)
            print(f'{alunos[nomeDosAlunos]} foi Reprovado(a) pois ficou com a média de {notarecuperacao}! ')

    else:
        print('\033[032m='*50)
        print(f'{alunos[nomeDosAlunos]} foi aprovado(a)! e teve a nota final de: {medias[nomeDosAlunos]}')
        quantidadeAprovado = quantidadeAprovado + 1

print('\033[035m='*50)
porcentagem = (quantidadeAprovado * 100) / totalDeAlunos
porcentagemReprovados = (porcentagem - 100) * -1
print(f'Quantidade Aprovado: {porcentagem: .2f}%')
print(f'Quantidade Reprovados: {porcentagemReprovados: .2f}%')


