#%%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as se




atributi = ['Date','tmps']

#Stanica IPH
data_iph = pd.read_csv("C:\\Users\\Bogdan\\Desktop\\vezbe2praktikum\\Za slanje\\Stanica IPH\\GDAS_2017_2019_IPH.csv", usecols=atributi)
data_iph.dropna(inplace=True)
#print (data_iph.head())

#Stanica LAZ
data_laz = pd.read_csv("C:\\Users\\Bogdan\\Desktop\\vezbe2praktikum\\Za slanje\\Stanica LAZ\\GDAS_2018_2019_LAZ.csv", usecols=atributi)
data_laz.dropna(inplace=True)

#Stanica NBG
data_nbg = pd.read_csv("C:\\Users\\Bogdan\\Desktop\\vezbe2praktikum\\Za slanje\\Stanica NBG\\GDAS_2017_2019_NBG.csv", usecols=atributi)
data_nbg.dropna(inplace=True)

#Stanica OBR
data_obr = pd.read_csv("C:\\Users\\Bogdan\Desktop\\vezbe2praktikum\\Za slanje\\Stanica OBR\\GDAS_2017_2019_OBR.csv", usecols=atributi)
data_obr.dropna(inplace=True)

#Stanica OVC
data_ovc = pd.read_csv("C:\\Users\\Bogdan\\Desktop\\vezbe2praktikum\\Za slanje\\Stanica OVC\\GDAS_2018_2019_OVC.csv", usecols=atributi)
data_ovc.dropna(inplace=True)

#Stanica USC
data_usc = pd.read_csv("C:\\Users\\Bogdan\\Desktop\\vezbe2praktikum\\Za slanje\\Stanica USC\\GDAS_2018_2019_USC.csv", usecols=atributi)
data_usc.dropna(inplace=True)

#Stanica VEL
data_vel = pd.read_csv("C:\\Users\\Bogdan\\Desktop\\vezbe2praktikum\\Za slanje\\Stanica VEL\\GDAS_2018_2019_VEL.csv", usecols=atributi)
data_vel.dropna(inplace=True)

#Stanica ZEM
data_zem = pd.read_csv("C:\\Users\\Bogdan\Desktop\\vezbe2praktikum\\Za slanje\\Stanica ZEM\\GDAS_2018_2019_ZEM.csv", usecols=atributi)
data_zem.dropna(inplace=True)



for frame in [data_iph,data_laz,data_nbg,data_obr,data_ovc,data_usc,data_vel,data_zem]:
    frame['tmps'] = frame['tmps']-270

data_iph['Date'] = pd.to_datetime(data_iph['Date'])
data_iph['tmps'] = data_iph['tmps'].astype(float)

datum=None

temp=0
zaProsek = 0
listaZaTemp=[]
lista=[]
std = 0

ispis={}
for index, row in data_iph.iterrows():
    if(row[0].date() != datum or datum==None):
        if len(listaZaTemp) > 0:
            zaProsek = sum(listaZaTemp)/len(listaZaTemp)
            std = np.std(listaZaTemp)        
            ispis ={'datum': str(datum), 'Avg temp':zaProsek,'Std':std}
            lista.append(ispis)

        datum = row['Date'].date()
        listaZaTemp=[]
        zaProsek=0
        std=0       

    listaZaTemp.append(row['tmps'])


lista[:5]











#%%
# %%
