import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("bigotes.csv")

sns.boxplot(x="categoria",y="valor",data=df)

plt.show()