import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from numpy.ma.core import remainder

#loading and defining the data
companies = pd.read_csv('1000_Companies.csv')
x = companies.iloc[:, :-1]
y = companies.iloc[:, 4]
# print(companies.head())

#data visualization
sns.heatmap(companies.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title('correlation heatmap')
# plt.show()

#encoding categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer

label_encoder = LabelEncoder()
companies['State'] = label_encoder.fit_transform(companies['State'])
print(companies.head())

column_transformer = ColumnTransformer(
                    transformers = [('encoder', OneHotEncoder(), [3])],
                    remainder = 'passthrough')
x = column_transformer.fit_transform(x)
print(x)