import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_excel('new_dataset.xlsx')
df.drop('Unnamed: 0', axis=1, inplace=True)
df.drop('Tipi', axis=1, inplace=True)
df['Yapi_Durumu'] = df['Yapi_Durumu'].fillna('İkinci El')
df.loc[df['Binanin_Yasi'] == '0 (Yeni)', 'Binanin_Yasi'] = '0'
df['WC_Sayisi'] = df['WC_Sayisi'].fillna(0)
df['WC_Sayisi'] = df['WC_Sayisi'].astype(int)
df['Balkon_Sayisi'] = df['Balkon_Sayisi'].fillna(0)
df['Tapu_Durumu'] = df['Tapu_Durumu'].fillna('Bilinmiyor')
df['Balkon_Sayisi'] = df['Balkon_Sayisi'].astype(int)
df['Esya_Durumu'] = df['Esya_Durumu'].fillna('Boş')
df['Yatirima_Uygunluk'] = df['Yatirima_Uygunluk'].fillna('Bilinmiyor')
df.to_excel('dataset.xlsx')