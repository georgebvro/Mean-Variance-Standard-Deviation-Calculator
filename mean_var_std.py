import numpy as np

def calculate(list):
    if len(list) < 9:
        raise ValueError('List must contain nine numbers.')
    matrix = np.array(list).reshape(3, 3)
    calculations = {}
    calculations['mean'] = []
    calculations['mean'].append(matrix.mean(axis = 0).tolist())
    calculations['mean'].append(matrix.mean(axis = 1).tolist())
    calculations['mean'].append(matrix.mean().tolist())
    calculations['variance'] = []
    calculations['variance'].append(matrix.var(axis = 0).tolist())
    calculations['variance'].append(matrix.var(axis = 1).tolist())
    calculations['variance'].append(matrix.var().tolist())
    calculations['standard deviation'] = []
    calculations['standard deviation'].append(matrix.std(axis = 0).tolist())
    calculations['standard deviation'].append(matrix.std(axis = 1).tolist())
    calculations['standard deviation'].append(matrix.std().tolist())
    calculations['max'] = []
    calculations['max'].append(matrix.max(axis = 0).tolist())
    calculations['max'].append(matrix.max(axis = 1).tolist())
    calculations['max'].append(matrix.max().tolist())
    calculations['min'] = []
    calculations['min'].append(matrix.min(axis = 0).tolist())
    calculations['min'].append(matrix.min(axis = 1).tolist())
    calculations['min'].append(matrix.min().tolist())
    calculations['sum'] = []
    calculations['sum'].append(matrix.sum(axis = 0).tolist())
    calculations['sum'].append(matrix.sum(axis = 1).tolist())
    calculations['sum'].append(matrix.sum().tolist())
    return calculations