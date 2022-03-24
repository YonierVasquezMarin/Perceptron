import pandas as pd


class Perceptron:
    '''Neurona artificial de una sola capa la cual tiene como objetivo obtener
    los pesos correctos de un dataset, para poder predecir valores del dataset
    respectivo.'''

    theta: float = 0.0
    factor_aprendizaje: float = 0.0
    epocas: int = 0
    listas_caracteristicas: list = []
    lista_pesos: list = []
    listas_valores_deseados: list = []
    cantidad_muestras: int = 0
    
    nombres_columnas_caracteristicas: list = []
    nombre_columna_valores_deseados: str = ''

    def __init__(self, df_tabla_datos: pd.DataFrame, nombres_cols_caracteristicas: list, nombre_col_valores_deseados: str) -> None:
        self.cantidad_muestras = len(self.lista_caracteristicas)

    def entrenar(self) -> None:
        '''Hallar de forma iterativa los pesos buscados.'''
        hayErrores: bool = True

        while hayErrores:
            hayErrores = False

            for i in range(self.cantidad_muestras):
                pass

    def hallar_axion(self, n_registro: int) -> None:
        '''Hallar el valor de salida de la neurona artificial. En la teoría, 
        este valor se representa con la variable "z".'''
        z: float = 0