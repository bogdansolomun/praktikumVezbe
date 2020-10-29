#%%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as se

#from pandas import DataFrame
#from scipy import stats


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

#09.10
#Histogram
#plt.hist(data_vel['tcld'])


#se.distplot(data_obr['tmps'], label='Obr')
#se.distplot(data_usc['tmps'], label='Usc')
#se.distplot(data_ovc['tmps'], label='Ovc')

#plt.legend(prop={'size':10})
#plt.title('temp')
#plt.xlabel('temp')

#16.10

data_iph['Date'] = pd.to_datetime(data_iph['Date'])
start_date = '01-01-2017'
end_date = '31-12-2019'
mask = (data_iph['Date'] > start_date) & (data_iph['Date'] <= end_date)

data_iph = data_iph.loc[mask]

#Prebacivanje u celzijuse
for frame in [data_iph,data_laz,data_nbg,data_obr,data_ovc,data_usc,data_vel,data_zem]:
    frame['tmps'] = frame['tmps']-270

data_iph.plot(x='Date', y='tmps',kind = 'line')



#ispis svih stanica
#iph = data_iph.plot(kind='line',x='Date' ,y='tmps',label='iph')
#zem = data_zem.plot(kind='line',x='Date' ,y='tmps',ax=iph,label='zem')
#vel = data_vel.plot(kind='line', x='Date', y='tmps', ax=zem,label='vel')
#laz = data_laz.plot(kind='line',x='Date', y='tmps', ax=vel,label='laz')
#usc = data_usc.plot(kind='line',x='Date', y='tmps', ax=laz,label='usc')

#plt.show()





#%%