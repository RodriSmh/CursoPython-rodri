import pandas as pd
df = pd.read_csv("datos.csv", encoding="utf-8")
nombres = df["nombre"]
#print(nombres)
cadena ="0123456789"
# uso de slicing
#print(cadena[0:5])
df_ordenado= df.sort_values("edad", ascending=False)
#print(df_ordenado)

df_concatenado= pd.concat([df, df_ordenado])
print(df_concatenado),
filas_totales,columnas_totales = df_concatenado.shape
print(f"filas_totales: {filas_totales}, columnas_totales: {columnas_totales}")
df_info=df_concatenado.describe()
print(f"\n{df_info}")
#loc
df_elemento = df.loc[2,"nombre"]
#iloc es con indices
df_elemento = df.iloc[2,0]
# pasando todos los nombres
nombres = df.iloc[:,0]
# usando condiciones 
mayor_30= df.loc[df["edad"]>30,:]
print(mayor_30)
