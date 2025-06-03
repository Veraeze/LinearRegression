import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from numpy.ma.core import remainder

#loading and defining the data
companies = pd.read_csv('1000_Companies.csv')
X = companies.iloc[:, :-1]
y = companies.iloc[:, 4]
# print(companies.head())

#data visualization
sns.heatmap(companies.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title('correlation heatmap')
plt.show()

#encoding categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
column_transformer = ColumnTransformer(
                    transformers = [('encoder', OneHotEncoder(drop='first', sparse_output=False), ['State'])],
                    remainder = 'passthrough')
X = column_transformer.fit_transform(X)
print(X)

# splitting the dataset into the training set and test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)


