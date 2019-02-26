import os
os.listdir()

import pandas
from geopy.geocoders import ArcGIS
nom = ArcGIS()


df1=pandas.read_csv("../jupyter/supermarkets.csv")
df1.set_index("ID")
nom.geocode(str(df1.iloc[0,1])+', '+str(df1.iloc[0,2])+', '+str(df1.iloc[0,3]))
warsaw = nom.geocode("Warszawa, Polska")
df1_t = df1.T
df1_t[7] = [7, "Warszawa, Polska","Warsaw","Mazowieckie", "PL","Mat", 90]
df1 = df1_t.T

df1["Address"]=df1["Address"]+', '+df1["City"]+', '+df1['State']
df1["Coordinates"]=df1["Address"].apply(nom.geocode)
df1["Latitude"]=df1["Coordinates"].apply(lambda x: x.latitude if x != None else None)
df1["Longitude"]=df1["Coordinates"].apply(lambda x: x.longitude if x != None else None)
print(df1)
df2=pandas.read_json("../jupyter/supermarkets.json")
df2.set_index("ID")

df3=pandas.read_excel("../jupyter/supermarkets.xlsx", sheet_name=0)

df4=pandas.read_csv("../jupyter/supermarkets-commas.txt")

df5=pandas.read_csv("../jupyter/supermarkets-semi-colons.txt", sep=';')

#get_ipython().run_line_magic('pinfo', 'pandas.read_csv')

df22=df2.set_index("Address")
df22.loc["735 Dolores St"]

list(df22.loc[:, "Country"])

df22.iloc[1:3,1:3]

df22.drop("3666 21st St",0)

df22.drop(df22.columns[1:2],1)

df22.drop(df22.index[0:4],0)

df22["Nowy"]=df22.shape[0]*["tekst"]
df22["nowszy"]=df22["Country"]+", "+['kek']

df22_t=df22.T
df22_t["Mój adres"]=["miasto","kraj",1,7,"nazwa","stacja xd", "a","b"]
df22 = df22_t.T
