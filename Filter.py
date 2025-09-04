# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import dateandtime

df=pd.read_csv(r'F:\GIThUB\GitDemo\My-First-GitHub-Repo\LocalRepo\RAW\U_Full_Link_Report_05_10_2024.csv',skiprows=5,encoding='latin1')
print(df)

df=df[['Site A Name','Site Z Name']]
df=df.dropna(subset=['Site Z Name'])
Test=df[df['Site A Name']=='IDJK100156_JMMU_H_C_I211']
print(Test)
Test1=df[df['Site A Name'].isin(['IDJK100156_JMMU_H_C_I211','INUE170101_PARA_I_C_I2C1'])]
print(Test1)