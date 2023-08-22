import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sbs
dataset=pd.read_csv('/content/student-mat.csv')

dataset.head()
dataset.info()

dfn=dataset[['traveltime','studytime']]

dfn.head()

sbs.lineplot(dfn,dashes=True)
plt.show()

sbs.lineplot(dfn['studytime'],dashes=True)
plt.show()

sbs.lineplot(dfn['traveltime'],dashes=True)
plt.show()

sbs.lineplot(x='traveltime',y='studytime',data=dfn)
plt.show()

from scipy.stats import norm

corelation=dfn.corr()
print(corelation)
sbs.heatmap(corelation,cmap="YlGnBu")

covar=dfn.cov()
print(covar)
sbs.heatmap(covar,cmap="YlGnBu")
plt.show()