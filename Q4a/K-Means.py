import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

data = pd.read_excel (r'D:\Documenten\TU Delft\ERDA&AI\Q4a_seperate.xls')
df = pd.DataFrame (data, columns = ['MTOW', 'Payload'])

output = []
wcss = []
k = 2
while k < 7:
    kmeans = KMeans(n_clusters = k)
    kmeans.fit (df)
    
    output.append(kmeans.labels_)
    wcss.append(kmeans.inertia_)
    k = k + 1

print(output)
print(wcss)

