import pandas as pd
from sklearn import preprocessing

# df = pd.read_excel('dataset.xlsx')
# df.drop('Unnamed: 0', axis=1, inplace=True)
# df_2 = df.copy()
# df_3 = df.copy()

le = preprocessing.LabelEncoder()
# df_3['Sehir'] = le.fit_transform(df_2['Sehir'])
# df_3['Ilce'] = le.fit_transform(df_2['Ilce'])
# df_3['Mahalle'] = le.fit_transform(df_2['Mahalle'])
# df_3['Oda_Sayisi'] = le.fit_transform(df_2['Oda_Sayisi'])
# df_3['Bulundugu_Kat'] = le.fit_transform(df_2['Bulundugu_Kat'])
# df_3['Isitma_Tipi'] = le.fit_transform(df_2['Isitma_Tipi'])
# df_3['Krediye_Uygunluk'] = le.fit_transform(df_2['Krediye_Uygunluk'])
# df_3['Yapi_Durumu'] = le.fit_transform(df_2['Yapi_Durumu'])
# df_3['Tapu_Durumu'] = le.fit_transform(df_2['Tapu_Durumu'])
# df_3['Esya_Durumu'] = le.fit_transform(df_2['Esya_Durumu'])
# df_3['Site_Icerisinde'] = le.fit_transform(df_2['Site_Icerisinde'])
# df_3['Binanin_Yasi'] = le.fit_transform(df_2['Binanin_Yasi'])
# df_3['Binanin_Kat_Sayisi'] = le.fit_transform(df_2['Binanin_Kat_Sayisi'])
# df_3['Kullanim_Durumu'] = le.fit_transform(df_2['Kullanim_Durumu'])
# df_3['Yatirima_Uygunluk'] = le.fit_transform(df_2['Yatirima_Uygunluk'])

# df_3.to_excel('dataset_etiketlenmis.xlsx')

df = pd.read_excel('dataset_etiketlenmis.xlsx')
df.drop('Unnamed: 0', axis=1, inplace=True)

df['Banyo_Sayisi'] = df['Banyo_Sayisi'].astype(str)
df['Banyo_Sayisi'] = le.fit_transform(df.Banyo_Sayisi)

df['WC_Sayisi'] = df['WC_Sayisi'].astype(str)
df['WC_Sayisi'] = le.fit_transform(df.WC_Sayisi)

df['Balkon_Sayisi'] = df['Balkon_Sayisi'].astype(str)
df['Balkon_Sayisi'] = le.fit_transform(df.Balkon_Sayisi)

df.to_excel('dataset_etiketlenmis_son.xlsx')

