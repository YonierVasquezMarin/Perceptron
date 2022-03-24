import pandas as pd

from perceptron.ConjuntoDeDendritas import ConjuntoDeDendritas


class Perceptron:
    '''Neurona artificial de una sola capa la cual tiene como objetivo obtener
    los pesos correctos de un dataset, para poder predecir valores del dataset
    respectivo.'''

    theta: float = 0.0
    factor_aprendizaje: float = 0.0
    epocas: int = 0

    df_tabla_datos: pd.DataFrame

    listas_caracteristicas: list = []
    lista_pesos: list = []
    listas_valores_deseados: list = []

    cantidad_muestras: int = 0
    
    nombres_cols_caracteristicas: list[str] = []
    nombre_cols_valores_deseados: str = ''

    conjunto_dendritas: ConjuntoDeDendritas

    def __init__(   
        self,
        df_tabla_datos: pd.DataFrame,
        nombres_cols_caracteristicas: list[str],
        nombre_col_valores_deseados: str,
        lista_pesos: list[float]) -> None:
        '''contructor del perceptron'''

        self.df_tabla_datos = df_tabla_datos
        self.nombres_cols_caracteristicas = nombres_cols_caracteristicas
        self.cantidad_muestras = len(self.df_tabla_datos)

        self.__prepararConjuntoDendritas()

    def entrenar(self) -> None:
        '''Hallar de forma iterativa los pesos buscados.'''
        # hayErrores: bool = True

        # while hayErrores:
        #     hayErrores = False

        #     for i in range(self.cantidad_muestras):
        #         pass

    def hallar_axion(self, n_registro: int) -> None:
        '''Hallar el valor de salida de la neurona artificial. En la teoría, 
        este valor se representa con la variable "z".'''
        # z: float = 0

    def __prepararConjuntoDendritas(self) -> None:
        '''Sólo selecciona las columnas de las características del dataset y las envía
        al conjunto de dendritas. Se omita la columna de los valores deseados.'''
        df_columnas_de_caracteristicas: pd.DataFrame = pd.DataFrame()

        # Seleccionar solo las columnas de caracteristicas
        for (col_nombre, col_valores) in self.df_tabla_datos.iteritems():
            for nombre_caracteristica in self.nombres_cols_caracteristicas:
                if col_nombre == nombre_caracteristica:
                    df_columnas_de_caracteristicas[col_nombre] = col_valores

        # Enviar el dataframe con las caracteristicas al Conjunto de Dendritas
        self.conjunto_dendritas = ConjuntoDeDendritas(df_columnas_de_caracteristicas)