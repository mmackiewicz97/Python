import os
from geopy.geocoders import ArcGIS
import pandas
print(os.listdir())
nom = ArcGIS()
df = pandas.read_csv("../Pyton/jupyter/supermarkets.csv")
df2 = pandas.DataFrame([[2,4,6],[10,20,30]], columns=['A','B','C'], index=['1','2'])
print(df2.B.max())

#.read_json, read_excel, csv(txt, sep=';')
#pandas.read_csv?
#df.set_index("Address")
#df.loc["735 Dolores St"]
#df.loc[:, "Country"]
#df.iloc[1:3, 2:4]
#df.drop("366 21St", 0)
#df.drop(df.columns[1:2], 1) #index[1:3], 0)
#df.shape
nom.geocode(str(df.iloc[0,1])+', '+str(df.iloc[0,2])+', '+str(df.iloc[0,3]))
df_t = df.T
df_t[7]=[7, "Warszawa, Polska", "Sam", "CB", "PL", "Mat", 1]
df = df_t.T
df["Address"]=df["Address"]+', '+df["City"]+', '+df['State']
df["Coordinates"]=df["Address"].apply(nom.geocode)
df["Latitude"]=df["Coordinates"].apply(lambda x: x.latitude if x != None else None)
df["Longitude"]=df["Coordinates"].apply(lambda x: x.longitude if x != None else None)
print(df)
