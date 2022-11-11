# FAZER SEU CÓDIGO AQUI:

alunos = []
medias = []
quantidadeAprovado = 0
numeroDeAlunos = 2  #Modifique o numero de alunos com base no que voce quiser 😎👍
nomeDosAlunos = numeroDeAlunos
totalDeAlunos = numeroDeAlunos


while numeroDeAlunos > 0:
    alunos.append(input('\033[036mNome do aluno: '))
# ---------------------------------------------------------------------------------- #
    nota1 = float(input('\033[036mNota da primeira AOP - * Nota entre 0.0 a 1.0 *: '))
    while nota1 > 1 or nota1 < 0:
        nota1 = float(input(f'\033[031mA nota da primeira AOP, só pode valer até 1 ponto e você colocou {nota1},por favor, digite a nota da AOP 1 novamente?  '))
# ---------------------------------------------------------------------------------- #
    nota2 = float(input('\033[036mNota da segunda AOP - * Nota entre 0.0 a 2.0 *: '))
    while nota2 > 2 or nota2 < 0:
        nota2 = float(input(f'\033[031mA nota da segunda  AOP, só pode valer até 2 pontos e você colocou {nota2},por favor, digite a nota da AOP 2 novamente? '))
# ---------------------------------------------------------------------------------- #
    nota3 = float(input('\033[036mNota da terceira AOP - * Nota entre 0.0 a 1.0 *: '))
    while nota3 > 1 or nota3 < 0:
        nota3 = float(input(f'\033[031mA nota da terceira AOP, só pode valer até 1 ponto e você colocou {nota3},por favor, digite a nota da AOP 3 novamente? '))
# ---------------------------------------------------------------------------------- #
    nota4 = float(input('\033[036mNota da prova regular - * Nota entre 0.0 a 6.0 *: '))
    while nota4 > 6 or nota4 < 0:
        nota4 = float(input(f'\033[031mA nota da prova 4, só pode valer até 6 ponto e você colocou {nota4},por favor, digite a nota da prova novamente?  '))
# ---------------------------------------------------------------------------------- #
    medias.append(nota1 + nota2 + nota3 + nota4)
    numeroDeAlunos = numeroDeAlunos - 1
    print(' ')

while nomeDosAlunos > 0:
    nomeDosAlunos = nomeDosAlunos - 1
    if medias[nomeDosAlunos] < 7:
        print('\033[033m=' * 50)
        notarecuperacao = float(input(f'Aluno {alunos[nomeDosAlunos]} está quase reprovando, por favor, ensira a nota da prova de recuperação: '))
        notarecuperacao = (notarecuperacao + medias[nomeDosAlunos]) / 2
    

        if notarecuperacao >= 5:
            print('\033[032m=' * 50)
            print(f'{alunos[nomeDosAlunos]} foi aprovado(a)! e teve a nota final de: {notarecuperacao}')
            quantidadeAprovado = quantidadeAprovado + 1

        else:
            print('\033[031m=' * 50)
            print(f'{alunos[nomeDosAlunos]} foi Reprovado(a) pois ficou com a média de {notarecuperacao}! ')

    else:
        print('\033[032m=' * 50)
        print(f'{alunos[nomeDosAlunos]} foi aprovado(a)! e teve a nota final de: {medias[nomeDosAlunos]}')
        quantidadeAprovado = quantidadeAprovado + 1

print('\033[035m=' * 50)
porcentagem = (quantidadeAprovado * 100) / totalDeAlunos
porcentagemReprovados = (porcentagem - 100) * -1
print(f'Quantidade Aprovado: {porcentagem: .2f}%')
print(f'Quantidade Reprovados: {porcentagemReprovados: .2f}%')
