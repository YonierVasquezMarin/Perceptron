from perceptron.ConjuntoDeDendritas import ConjuntoDeDendritas


class Dendrita:
    '''Una entrada del perceptrón. Se compone del valor de entrada multiplicado
    por su peso.'''

    valor_entrada: float
    '''Un valor de entre el conjunto de valores de cada muestra.'''

    peso: float
    '''El peso que le corresponde a la columna donde está el valor actual.'''

    def __init__(self, valor_entrada: float, peso: float) -> None:
        '''kkk'''
        self.valor_entrada = valor_entrada
        self.peso = peso
