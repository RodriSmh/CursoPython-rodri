import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("cofla_ingresos.csv")

sns.barplot(x="fuente",y="ingresos",data=df,)
total_ingresos = df['ingresos'].sum()
# with open ("cofla_ingresos.csv","a",encoding="utf-8") as file:
#     file.write(f"\nTotal ingresos, {total_ingresos}")

plt.show()