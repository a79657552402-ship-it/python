import pandas
import pandas as pd

# a = pandas.read_csv('date.csv')
# print(a)
#
# df = pd.read_csv('https://drive.google.com/uc?export=download&id=1dLwh-PaDERYQJ32IQHUCCMyaCVdFq4ot', sep=',')
#
# print(df.shape)
#
# print(df.head())
# print(df.tail())
# print(df.sample(frac=0.3, replace=True))
# print(df.shape)
# print(df.columns)
# print(df.dtypes)
# print(df.notnull().sum())
# print(df.isnull().sum())
# print(df.info())

# a = pandas.read_excel('C:/Users/Mustafa/Desktop/Меню.xlsx')
# print(a)
# df2 = pd.read_excel('https://drive.google.com/uc?export=download&id=1yzKCpvNk3r5p0ZrBzxkqyiB6sxtZqpbX', sheet_name=0)
# print(df2)

# df = pandas.read_csv('C:/Users/Mustafa/Downloads/3.3.2.csv')
# data = {'Name': ['Anna', 'Boris', 'Polina'], 'Age': [28, 34, 27], 'Salary' : [1000, 1500, 1800], 'Occupation' : ['Data Scientist', 'Data Analyst', 'Data Engineer']}
# df2 = pd.DataFrame(data, index=['a', 'b', 'c'])
# print(df2)
# print('===================')
# print('===================')
# print(df2.loc['b', 'Name'])
# print('===================')
# print('===================')
# print(df2.loc['b':'c', 'Name':'Salary'])
# print('===================')
# print('===================')
# print(df2.loc[:, 'Salary'])
# print('===================')
# print('===================')
# print(df2.loc[['a', 'c'], ['Name', 'Occupation']])

df = pd.read_csv('https://drive.google.com/uc?export=download&id=1GztFVF32hUQkzDD-kHfH37vstbvwKJwp')
print('===================')
print('===================')
print(df.iloc[0:20])
print('===================')
print('===================')
print(df.iloc[:,2:7])