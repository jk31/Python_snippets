# Data Science Collection

#### Import template

import numpy as np
import pandas as pd
# https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf
pd.options.display.max_colwidth = 100

from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

import pandas_profiling

import re

import requests

import matplotlib as mpl
import matplotlib.pyplot as plt
%matplotlib inline
https://github.com/matplotlib/cheatsheets

## Wrangling

### Basic imports

import numpy as np
import pandas as pd

import pandas_profiling as pp

### Create/Load/Save DataFrames

#### Manual

df = pd.DataFrame(
    np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
    columns=['a', 'b', 'c'])

data = [['tom', 10], ['nick', 15], ['juli', 14]] 

df = pd.DataFrame(
    data, 
    columns = ['Name', 'Age']) 

df = pd.DataFrame({
    'ColumnA': np.repeat(-1, 6).tolist(),
    'ColumnB':["A", "Bird", "C", "E", "E", "F"],
    'ColumnC':[0.7, 0.9, 0.3, 3.6, 2.7, 3],
    'y':[1, 1, 1, 0, 0, 0]})

data = [
    ['2015-06-01', 41],
    ['2015-06-02', 43],
    ['2015-06-03', 47],
    ['2015-06-04', 42],
    ['2015-06-05', 45],
    ['2015-06-08', 39],
    ['2015-06-09', 38],
    ['2015-06-10', 41]
]

data = pd.concat([a, b, c, d, e, f], axis=1)
data.columns = ["All", "Choice", "Random-Videos", "Random-Comments", "Previous-Videos", "Previous-Comments"]
 
df = pd.DataFrame(data, columns=['date', 'price'])

### List comprehension lambda

name_list = [fake.name() for _ in range(100)

[x for x in df_group.columns if df_group[x].var() > 1 ]
[x+1 if x >= 45 else x+5 for x in l]
             
a = [1, 2, 3]
def mul(arg):
    return arg*2
list(map(mul, a))            
list(map(square, range(100)))
list(map(lambda x: x**2, range(10)))

# gives true and false
list(map(lambda x: x>2, range(10)))
# gives the numbers
list(filter(lambda x: x>2, range(10)))

sum(list(filter(lambda x: (x%3==0 or x%5==0), range(1000))))

sum(x for x in range(1000) if (x % 3 == 0 or x % 5 == 0))

lambda x: True if x % 2 == 0 else False

for i, j in zip(range(-10, 11), range(1939, 1960)):
  print(i, j )

from itertools import product
sum(max(x, y) for x, y in product(range(1, 7), range(1, 7))) / 36
             
#### Load/Save

df = pd.read_csv("file.csv")
pd.to_csv("file.csv", index=False)

df = pd.read_stata("file.dta")
labels = pd.io.stata.StataReader(r"C:\Users\XXX.dta").variable_labels()
df.to_stata(r"C:\Users\XXX.dta", variable_labels = labels)

df = pd.read_excel('file.xlsx', index_col=None, header=0) 
pd.to_excel("file.xlsx")

df = pd.read_pickle("file.pkl")
pd.to_pickle("file.pkl")
             
def timestamp():
    time = f"{datetime.datetime.now().date()}--{datetime.datetime.now().time().replace(microsecond=0)}"
    return time.replace(":", "-")
             
with open("all_players.txt", "w") as f:
    for player in all_players:
             f.write(player +"\n")
             
all_teams = []
with open("all_teams.txt", "r") as f:
    for line in f:
        all_teams.append((line.strip()))

#### Merging and Appending

pd.merge(df1, df2, on='Customer_id', how='inner')
             
# will remove observations that are not in intersection
df = df.merge(df2, left_on='HomeTeam', right_on='Team')

result = pd.merge(a, b[["Team", "Season", "Rank", "GD"]], how="left", on=["Team", "Season"])

### Overview

df.shape

df.head(5)

df.tail(2)

df.info()
df.info(verbose=True)

df.dtypes
df.astype({'col1': 'int32'}).dtypes

df.columns

df["y"].value_counts()
df["y"].value_counts().sort_index()

df["ColumnC"].unique().tolist()

df_full.columns.difference(df.columns)

df.describe()
pd.crosstab(df["Subtype"], df["Type"])

profile = df.profile_report(
        
    check_correlation_pearson= False, 
    correlations={
        'pearson': True,
        'spearman': False,
        'kendall': False,
        'phi_k': False,
        'cramers': False,
        'recoded':False},
    plot ={'histogram':{'bayesian_blocks_bins': False}}
    )

profile.to_file(output_file="df_profile_output.html")

!start df_profile_output.html

### Select rows and columns
<a href="https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html">Documentation for Indexing</a>

df[(df["y"] == 1) & (df["ColumnB"] == "A")]

df.iloc[0:2, 2:3]

df.loc[0:3, "ColumnC"]

df.loc[df["ColumnC"] > 1, ["y"]]

df.query("y == 1 & ColumnB == 'A'")
             
df.loc[df['column_name'].isin(some_values)]


### Edit DataFrame

#### 
             or keep column

df = df.drop(["ColumnA", "ColumnB"], axis=1)

df = df[["ColumnsToKeep", "ThisOneToo"]]
 
# remove dublicated, only keep one of them             
all_tables = all_tables.loc[:,~all_tables.columns.duplicated()]

#### Drop row

df[df["y"] == 0]

#### Drop empty

df.isna().any()
df.isna().sum()
df = df.dropna()
# removes columns             
df.dropna(axis="columns")
 
# show NaN rows
df[df.isnull().any(axis=1)]

#### Drop if not enough

drop_cols = df.columns[(df == 0).sum() > 0.25*dataframe.shape[1]]
df.drop(drop_cols, axis = 1, inplace = True) 

#### Rename Columns

df.rename(columns={'ColumnA': 'SomeOtherName'}, inplace=True)

df.sort_values(["ColumnC", "y"], ascending=False)

#### Create ID column

df["ID"] = np.arange(0, len(df))

df["ID"] = df.index.values

#### Simple feature creation

df["New"] = df["y"] + 1

#### if else then

df.loc[(df["y"] == 1) | (df["ColumnA"] == -1), ["ExistingColumnA", "AnotherExistingColumn"]] == "Oki Doki"

df["SomeNewColumn"] = np.where((df["y"] == 1) & (df["ColumnB"] == "A"), "Ok", "Not ok")

df["SomeNewColumn"] = df.["y"].apply(lambda x: "Oki" if x == 1 else "Not")

df["SomeColumn"] = df.apply(lambda x: 1 if x["y"] == 1 else 0, axis=1)

df = df["y"].replace(1, 2)

.maps(dict)
             
            
df["tokeep"] = df.apply(lambda x: 1 if x["HomeTeam"] in df2["Team"].tolist() else 0, axis=1)
# df["tokeep"] = np.where(df["HomeTeam"].isin(["Leverkusen"]), 1, 0)

Encoding

def back_from_dummies(df):
    result_series = {}

    # Find dummy columns and build pairs (category, category_value)
    dummmy_tuples = [(col.split("_")[0],col) for col in df.columns if "_" in col]

    # Find non-dummy columns that do not have a _
    non_dummy_cols = [col for col in df.columns if "_" not in col]

    # For each category column group use idxmax to find the value.
    for dummy, cols in groupby(dummmy_tuples, lambda item: item[0]):

        #Select columns for each category
        dummy_df = df[[col[1] for col in cols]]

        # Find max value among columns
        max_columns = dummy_df.idxmax(axis=1)

        # Remove category_ prefix
        result_series[dummy] = max_columns.apply(lambda item: item.split("_")[1])

    # Copy non-dummy columns over.
    for col in non_dummy_cols:
        result_series[col] = df[col]

    # Return dataframe of the resulting series
    return pd.DataFrame(result_series)

#### Count if

len(df.query(" y == 1 "))

len(df[(df["y"] == 1) & (df["ColumnB"] == "A")])

#### Loop over rows

for index, row in df.iterrows():
    print(row['ColumnA'], row['y'])

#### Remove if too often appearing in a column

df = df[df.desc.isin(df.desc.value_counts()[df.desc.value_counts() == 1].index)]

### Grouping

df_group = df.groupby("ColumnB").mean()

## Visualization

import matplotlib as mpl
import matplotlib.pyplot as plt
%matplotlib inline
plt.style.use('seaborn-whitegrid')
# https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Python_Seaborn_Cheat_Sheet.pdf
             
import seaborn as sns

### General Plotting

x = np.linspace(0, 5, 100)
g = x*2
s = s+3

fig = plt.figure(figsize=(8, 8))
ax = plt.axes()

ax.plot(x, g, color="black", label="G")
ax.plot(x, s, color="brown", label="S")
ax.plot(x, g+s, color="blue", label="G+S")

ax.set_xlim([0, 2])
ax.set_ylim([0, 0.2])
    
plt.xlabel("X", fontsize=16)
plt.ylabel("Y", fontsize=16)
ax.set_yticklabels([])
ax.set_xticklabels([])
    
ax.grid(False)
ax.legend(prop={'size': 16})

### 1 Variable

df["y"].plot.hist()

sns.distplot(df[(df.price <= 80000) & (df.price >= 100)].price)

#CDF
plt.hist(data, density=True, cumulative=True, label='CDF',
         histtype='step', alpha=0.8, color='k')

### 2-3 Variables

#### Continuous - Continuous

df.plot.scatter(x, y)

sns.regplot(x="odometer", y="price", data=df)

sns.scatterplot(x="odometer", y="price", data=df)

#### Categorical (sorted) - Continuous

sns.set(rc={'figure.figsize':(16,9)})
plt.xticks(rotation=90)
sns.boxplot(x="manufacturer", y="price", data=df)

#### Categorical (unsorted) - Continuous

manufacturer_year_price = sns.FacetGrid(df, col="manufacturer", col_wrap=5)
manufacturer_year_price.map(plt.scatter, "year", "price")

### Many Variables

#  Scatterplot arguments
sns.lmplot(x='Attack', y='Defense', data=df,
           fit_reg=False, # No regression line
           hue='Stage')

df.variable.value_counts().plot(kind="bar")

sns.pairplot(df)

sns.pairplot(data=data,
                  y_vars=['age'],
                  x_vars=['weight', 'height', 'happiness'])

fig, (ax) = plt.subplots(1, 1, figsize=(10,6))

hm = sns.heatmap(corr, 
                 ax=ax,           # Axes in which to draw the plot, otherwise use the currently-active Axes.
                 cmap="coolwarm", # Color Map.
                 #square=True,    # If True, set the Axes aspect to “equal” so each cell will be square-shaped.
                 annot=True, 
                 fmt='.2f',       # String formatting code to use when adding annotations.
                 #annot_kws={"size": 14},
                 linewidths=.05)

fig.subplots_adjust(top=0.93)
fig.suptitle('Wine Attributes Correlation Heatmap', 
              fontsize=14, 
              fontweight='bold')

## Regular experssions / String Manipulation

import re

text = '1 flock of 120 quick brown foxes jumped over 30 lazy brown, bears.'

re.findall(r"[\d]+", text)

df["ColumnB"].str.contains("(ird)", regex=True)

df = df[df.desc.str.len() < 1000]
             
# split column             
df1["A"], df1["B"] = df1["Apps"].str.split("XXX").str
             
# string replace
df1["B"] = df1["B"].str.replace(")", "")

             
df["Nationality"] = df["Nationality"].apply(lambda x: re.search(r"(\w+)$", x).group() if re.search(r"(\w+)$", x) != None else "Unkown")
## OS

import os

os.getcwd()
os.chdir()
os.path.exists("")

import glob
glob.glob("*.pdf")

from zipfile import ZipFile

with ZipFile("data-filtered.zip", "r") as zip:
    zip.extractall()
    zip.close()
             
# usefull
import datetime            
def calculate_age(born):
    born = datetime.datetime.strptime(born, "%d-%m-%Y")
    today = datetime.date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
    
## SQL
import sqlite3
cnx = sqlite3.connect("database.sqlite")
#### Show all tables from db
pd.read_sql_query("SELECT * FROM sqlite_master", cnx)

df = pd.read_sql_query("SELECT * FROM football_data", cnx)
