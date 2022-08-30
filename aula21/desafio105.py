def turma(* notas, sit=False):
    '''
    -> Função para analisar notas e situações de vários alunos
    :param notas: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    '''
    sala = {}
    sala['total'] = len(notas)
    sala['maior'] = max(notas)
    sala['menor'] = min(notas)
    sala['média'] = (sum(notas)/len(notas))
    if sit:
        if sala['média'] >= 7:
            sala['situação'] = 'BOA'
        elif sala['média'] >= 5:
            sala['situação'] = 'RAZOÁVEL'
        else:
            sala['situação'] = 'RUIM'
    print(sala)


turma(5.5, 2.5, 1.5, sit=True)
