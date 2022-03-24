from perceptron.Dendrita import Dendrita
import pandas as pd


class ConjuntoDeDendritas:
    '''Conjunto que contiene cada dendrita del perceptrón. Aquí está 
    contenido los pesos de cada columna, puesto que son valores comunes
    de cada dendrita.'''

    lista_pesos: list
    '''Lista de pesos. Cada columna del dataset tiene su peso.'''

    columnas_de_caracteristicas: pd.DataFrame
    '''Columnas de caracteristicas del dataset.'''

    conjunto_dendritas: list[Dendrita]
    '''Lista de dendritas. Cada dendrita tiene su valor y peso.'''

    def __init__(
        self,
        columnas_de_caracteristicas: pd.DataFrame
        ) -> None:
        self.columnas_de_caracteristicas = columnas_de_caracteristicas

    def __crearDendritas(self) -> None:
        '''Selecciona cada muestra del dataset y c'''