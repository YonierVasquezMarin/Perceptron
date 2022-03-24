import pandas as pd
from Perceptron import Perceptron

# >>> Crear un dataframe sencillo
# df = pd.DataFrame()

# df['Nombre'] = ['Juan', 'Laura', 'Pepe']
# df['Edad'] = [42, 40, 37]

# print('CANTIDAD FILAS\n', len(df))
# print('EL DATAFRAME COMPLETO\n',df)
# print()
# print('COLUMNA DE NOMBRES\n', df['Nombre'])
# for i in range(len(df['Nombre'])):
#     print('El nombre ', i+1, ' es ', df['Nombre'][i])


# >>> Obtener un dataframe de excel
# df = pd.read_excel('C:/Users/yonie/Documents/Datasets/Puerta OR.xlsx')
# print(df)


# >>> Trabajando con las columnas del dataframe
datos = {
    'A': [0, 0, 1, 1],
    'B': [0, 1, 0, 1],
    'A_OR_B': [0, 1, 1, 1]
    }
df = pd.DataFrame(data=datos)
perceptron = Perceptron(
    df_tabla_datos=df,
    nombres_cols_caracteristicas=['A', 'B'],
    nombre_col_valores_deseados='A_OR_B',
    lista_pesos=[]
)