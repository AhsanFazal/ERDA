import pandas as pd
import numpy as np
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import seaborn as sns

#data = pd.read_excel (r'D:\Documenten\TU Delft\ERDA&AI\Q4a_seperate.xls')
#df = pd.DataFrame (data, columns = ['MTOW', 'Payload'])

data = pd.read_excel (r'D:\Documenten\TU Delft\ERDA&AI\Q4a_seperate.xls')
df = pd.DataFrame (data, columns = ['MTOW', 'Range'])

model = TSNE(learning_rate = 5)
transformed = model.fit_transform(df)

xs = transformed[:,0]
ys = transformed[:,1]


plt.scatter(xs, ys)
plt.show()

#output = []
#tsne = TNSE(df)
#df_embedded = TSNE(n_components = 1).fit_transform(df)


print(transformed)
