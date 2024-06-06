import pandas as pd

df = pd.read_excel('dataset.xlsx')
df.drop('Unnamed: 0', axis=1, inplace=True)

df_2 = pd.read_excel('dataset_etiketlenmis_son.xlsx')
df_2.drop('Unnamed: 0', axis=1, inplace=True)
print(df[df['Sehir'] == 'Istanbul'])
print(df_2.Sehir)
# ['Adana' 'Aydın' 'Balıkesir' 'İstanbul' 'Ankara' 'İzmir' 'Bursa' 'Antalya'
#  'Kayseri' 'Konya' 'Manisa' 'Mersin' 'Muğla' 'Afyonkarahisar' 'Çanakkale'
#  'Denizli' 'Diyarbakır' 'Edirne' 'Eskişehir' 'Gaziantep' 'Kahramanmaraş'
#  'Kırklareli' 'Kocaeli' 'Ordu' 'Samsun' 'Sivas' 'Şanlıurfa' 'Tekirdağ'
#  'Trabzon' 'Van' 'Yalova' 'Sakarya']
# [ 0  4  5 29  2 30  6  3 13 15 17 18 19  1 28  7  8  9 10 11 12 16 14 20
#  22 23 31 24 25 26 27 21]
# sehirler = {
#     'Adana': 0, 'Aydın': 4, 'Balıkesir': 5, 'İstanbul': 29, 'Ankara': 2,
#     'İzmir': 30, 'Bursa': 6, 'Antalya': 3, 'Kayseri': 13, 'Konya': 15,
#     'Manisa': 17, 'Mersin': 18, 'Muğla': 19, 'Afyonkarahisar': 1,
#     'Çanakkale': 28, 'Denizli': 7, 'Diyarbakır': 8, 'Edirne': 9,
#     'Eskişehir': 10, 'Gaziantep': 11, 'Kahramanmaraş': 12,
#     'Kırklareli': 16, 'Kocaeli': 14, 'Ordu': 20, 'Samsun': 22,
#     'Sivas': 23, 'Şanlıurfa': 31, 'Tekirdağ': 24, 'Trabzon': 25,
#     'Van': 26, 'Yalova': 27, 'Sakarya': 21
# }

# # Döngü oluşturma
# for sehir, numara in sehirler.items():
#     ilce_listesi = df[df['Sehir'] == sehir]['Ilce'].unique()
#     print(f"{sehir} için df: {ilce_listesi}")

array1 = [5, 1, 7, 2, 3, 6, 8, 9, 21, 10, 13, 15, 4, 11, 14, 22, 12, 23, 18, 19, 20, 27, 16, 17, 25, 40, 30, 24, 36, 26, 32, 33, 29, 28, 35, 31, 42, 99, 50, 39, 44, 34, 38, 48, 41, 60, 45, 54, 43, 46, 37, 63, 83]
array2 = [4, 0, 6, 1, 2, 5, 7, 8, 20, 9, 12, 14, 3, 10, 13, 21, 11, 22, 17, 18, 19, 26, 15, 16, 24, 39, 29, 23, 35, 25, 31, 32, 28, 27, 34, 30, 41, 52, 47, 38, 43, 33, 37, 46, 40, 49, 44, 48, 42, 45, 36, 50, 51]


result = {}

for key, value in zip(array1, array2):
    result[key] = str(value)

print(result)
