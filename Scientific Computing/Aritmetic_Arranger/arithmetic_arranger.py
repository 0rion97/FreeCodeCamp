import numpy as np
import sys

def arithmetic_arranger(problemas,resolucion=False):
    operaciones = []

    # Errores entrada
    number_prob = len(problemas)
    if number_prob > 5:
        return 'Error: Too many problems.'

    for n_ope in range(len(problemas)):
        operaciones.append(problemas[n_ope].split())
    x, y = np.shape(operaciones)

    for n in range(x):
        if operaciones[n][1] != '+' and operaciones[n][1] != '-':
            return "Error: Operator must be '+' or '-'."
        try:
            a = int(operaciones[n][0])
            b = int(operaciones[n][2])
        except:
            return 'Error: Numbers must only contain digits.'

        if len(operaciones[n][0]) > 4 or len(operaciones[n][2]) > 4:
            return 'Error: Numbers cannot be more than four digits.'


    if resolucion is True:
        y +=1
        arranged_problems = ''

        for n_ope in range(len(operaciones)):
            if operaciones[n_ope][1] == '+':
                operacion= int(operaciones[n_ope][0]) + int(operaciones[n_ope][2])
                operaciones[n_ope].append(operacion)
            elif operaciones[n_ope][1] == '-':
                operacion= int(operaciones[n_ope][0]) - int(operaciones[n_ope][2])
                operaciones[n_ope].append(operacion)

        # Creacion del print
        for i in range(x):  #Primera fila
            if len(operaciones[i][0])>len(operaciones[i][2]):
                arranged_problems = arranged_problems + '  ' + operaciones[i][0] + '    '
            else:
                arranged_problems = arranged_problems + '  ' + ' '*(len(operaciones[i][2])-len(operaciones[i][0])) + operaciones[i][0] + '    '
        arranged_problems = arranged_problems[:-4] + '\n'

        for i in range(x): # Segunda Fila
            if len(operaciones[i][0])>len(operaciones[i][2]):
                arranged_problems = arranged_problems + operaciones[i][1] + ' ' + ' '*(len(operaciones[i][0])-len(operaciones[i][2])) +operaciones[i][2] + '    '
            else:
                arranged_problems = arranged_problems + operaciones[i][1] + ' ' + operaciones[i][2] + '    '
        arranged_problems = arranged_problems[:-4] + '\n'

        for i in range(x): # Tercera
            if len(operaciones[i][0])>len(operaciones[i][2]):
                arranged_problems = arranged_problems + '--' + '-'*len(operaciones[i][0]) + '    '
            else:
                arranged_problems = arranged_problems + '--' + '-'*len(operaciones[i][2]) + '    '
        arranged_problems = arranged_problems[:-4] + '\n'

        for i in range(x): # Cuarta
            if len(operaciones[i][0])>len(operaciones[i][2]):
                arranged_problems = arranged_problems + ' '*abs((2 + len(operaciones[i][0])-len(str(operaciones[i][3])))) + str(operaciones[i][3]) + '    '
            else:
                arranged_problems = arranged_problems + ' '*abs((2 + len(operaciones[i][2])-len(str(operaciones[i][3])))) + str(operaciones[i][3]) + '    '
        arranged_problems = arranged_problems[:-4]


        print(arranged_problems)

    else:
        arranged_problems = ''

        for n_ope in range(len(operaciones)):
            if operaciones[n_ope][1] == '+':
                operacion = int(operaciones[n_ope][0]) + int(operaciones[n_ope][2])
                operaciones[n_ope].append(operacion)
            elif operaciones[n_ope][1] == '-':
                operacion = int(operaciones[n_ope][0]) - int(operaciones[n_ope][2])
                operaciones[n_ope].append(operacion)

        # Creacion del print
        for i in range(x):  # Primera fila
            if len(operaciones[i][0]) > len(operaciones[i][2]):
                arranged_problems = arranged_problems + '  ' + operaciones[i][0] + '    '
            else:
                arranged_problems = arranged_problems + '  ' + ' ' * (len(operaciones[i][2]) - len(operaciones[i][0])) + operaciones[i][
                    0] + '    '
        arranged_problems = arranged_problems[:-4] + '\n'

        for i in range(x):  # Segunda Fila
            if len(operaciones[i][0]) > len(operaciones[i][2]):
                arranged_problems = arranged_problems + operaciones[i][1] + ' ' + ' ' * (
                            len(operaciones[i][0]) - len(operaciones[i][2])) + operaciones[i][2] + '    '
            else:
                arranged_problems = arranged_problems + operaciones[i][1] + ' ' + operaciones[i][2] + '    '
        arranged_problems = arranged_problems[:-4] + '\n'

        for i in range(x):  # Tercera
            if len(operaciones[i][0]) > len(operaciones[i][2]):
                arranged_problems = arranged_problems + '--' + '-' * len(operaciones[i][0]) + '    '
            else:
                arranged_problems = arranged_problems + '--' + '-' * len(operaciones[i][2]) + '    '
        arranged_problems = arranged_problems[:-4]

        print(arranged_problems)

    return arranged_problems