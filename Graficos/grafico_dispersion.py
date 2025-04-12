import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("dispersion.csv")

sns.scatterplot(x="tiempo",y="dinero",data=df,)
# with open ("cofla_ingresos.csv","a",encoding="utf-8") as file:
#     file.write(f"\nTotal ingresos, {total_ingresos}")

plt.show()