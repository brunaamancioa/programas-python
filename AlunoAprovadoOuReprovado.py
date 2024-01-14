primeiraNota = float (input('Digite a primeira nota: '))
segundaNota = float (input('Digite a segunda nota: '))
terceiraNota = float(input('Digite a terceira nota: '))

media = (primeiraNota + segundaNota + terceiraNota)/3

if media >=6:
    print ('O aluno foi aprovado. Sua média é {:.2f}.'.format(media))
else:
    print('O aluno foi reprovado. Sua média é {:.2f}.'.format(media))



