from sklearn import svm
import numpy as np
import pandas as pd

data = pd.read_excel (r'D:\Documenten\TU Delft\ERDA&AI\Q4a_seperate.xls')
df = pd.DataFrame (data, columns = ['MTOW', 'Range'])

