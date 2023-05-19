import pandas as pd
import numpy as np
import seaborn as sns
import plotly
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import warnings
import os
from inflect import engine as inf

import methods as m


pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

df = pd.read_excel('C:\\Users\\user\\.vscode\\Code_Foil_\\Nuovo.xlsx')
df.replace('-99', np.nan, inplace=True)
df.replace(-99, np.nan, inplace=True)


df['country'] = df['citizenship'].apply(lambda x: m.get_name(x))
df['alpha_3'] = df['country'].apply(lambda x: m.get_alpha3(x))
# salvo in data_map il numero di vittime per ogni stato (quindi è un dataframe con tre colonne, country, alpha_3 e Victims)
# i paesi sono ordinati in ordine alfabetico, ripetuti una volta.
data_map = pd.DataFrame(df.groupby(['country', 'alpha_3'])['alpha_3'].agg(Victims='count')).reset_index()


# creo una lista di tuple in cui il primo elemento è il nome del paese e il secondo il numero di vittime per anno dal 2002 al 2019)
cm = sns.light_palette("red", as_cmap=True)
""" table = pd.pivot_table(df, values='Datasource', index='country',
                    columns='yearOfRegistration', aggfunc='count', fill_value=0)
table.style.background_gradient(cmap=cm)
table.style.set_table_attributes("style='display:inline'")
print(table)

sns.set(rc={'figure.figsize':(15.7,12.27)})
sns.heatmap(table, cmap="YlGnBu", annot=True, fmt=".1f", linewidths=.9)

plt.show()
 """

""" df['meansOfControlConcatenated'] = df['meansOfControlConcatenated'].str.replace('Abuse', 'abuse', regex=True)
data_bar_f = df[(df.meansOfControlConcatenated.notna()) & (df.gender == 'Female')].meansOfControlConcatenated.apply(lambda x: pd.value_counts(str(x).split(";"))).sum(axis = 0)
data_bar_m = df[(df.meansOfControlConcatenated.notna()) & (df.gender == 'Male')].meansOfControlConcatenated.apply(lambda x: pd.value_counts(str(x).split(";"))).sum(axis = 0)

fig = go.Figure(data=[
    go.Bar(name='Female', x=data_bar_f.index, y=data_bar_f),
    go.Bar(name='Male', x=data_bar_m.index, y=data_bar_m)
])
fig.update_traces(texttemplate='%{value}', textposition='outside')
fig.update_layout(hovermode='x', title_text='Means of Control')
fig.show() """


# creo una tabella in cui salvo, per ogni tipo di abuso, il numero di vittime
# per 9 fasce d'età da 0 a 48+
table2 = pd.DataFrame()
for i in df[df.ageBroad.notna()].ageBroad.unique():
    age_col = pd.DataFrame(df[(df.meansOfControlConcatenated.notna()) & (df.ageBroad == i)].meansOfControlConcatenated.apply(lambda x: pd.value_counts(str(x).split(";"))).sum(axis = 0))
    age_col.rename(columns={0: i}, inplace=True)
    table2 = pd.concat([table2,age_col],axis=1)

age_list = ['0--8', '9--17', '18--20', '21--23', '24--26', '27--29', '30--38', '39--47', '48+']
table2 = table2.reindex(columns=age_list)

table2.fillna(0).style.background_gradient(cmap=cm).format('{:,.0f}')
print(table2)

indice = table2.iloc[:, 0]
print(indice)


for i in range(5):
    posizione = str(inf.number_to_words(inf.ordinal(i + 1)))
    traduct = tran.translate(posizione, dest='it').text
    id_colonna = input(f"Inserisci l'ID per valutare la {traduct} colonna: ")
    ids.append(id_colonna)
    """ posizione = num_ord_fem(i + 1)
    id_colonna = input(f"Inserisci l'ID per valutare la {posizione} colonna: ")
    ids.append(id_colonna) """



# ds['COUNTRY'] = ds['COUNTRY'].str.upper()


