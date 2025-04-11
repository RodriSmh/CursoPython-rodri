import pandas as pd
df = pd.read_csv("..\\Archivos\\datos.csv")
df['apellido'].replace("Pérez","Paez",inplace=True)
print(df["apellido"])

#eliminando filas faltantes
# df = df.dropna()
#eliminar filas repetidas
# df = df.drop_duplicates()
# creando un csv 
df.to_csv("datos_limpios.csv")