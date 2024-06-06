import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from xgboost import XGBRegressor

# Veri Setini Okuma ve Ön İşleme
df = pd.read_excel('dataset_etiketlenmis_son.xlsx').drop('Unnamed: 0', axis=1)
features = ['Oda_Sayisi', 'Bulundugu_Kat', 'Isitma_Tipi', 'Yapi_Durumu',
            'Tapu_Durumu', 'Esya_Durumu', 'Site_Icerisinde', 'Brut_Metrekare',
            'Binanin_Yasi', 'Binanin_Kat_Sayisi', 'Kullanim_Durumu',
            'Banyo_Sayisi', 'WC_Sayisi', 'Sehir', 'Ilce']

X = df[features]
y = df['Fiyat']

# Veriyi Eğitim ve Test Kümelerine Ayırma
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=144)

# Model Oluşturma ve Eğitme
model = XGBRegressor(colsample_bytree=0.6, learning_rate=0.09, max_depth=6, n_estimators=2000)
model.fit(X_train, y_train)

# Modelin Performansını Değerlendirme
y_pred_train = model.predict(X_train)
y_pred_test = model.predict(X_test)

train_r2 = r2_score(y_train, y_pred_train)
test_r2 = r2_score(y_test, y_pred_test)

print("Eğitim R2 Skoru:", train_r2)
print("Test R2 Skoru:", test_r2)

# Yeni Veri Noktaları için Tahmin Yapma 3008552
veri_list = [2, 5, 9, 2, 3, 1, 0, 150, 2, 0, 2, 0, 2, 0, 84]
new_data = [veri_list]
new_df = pd.DataFrame(new_data, columns=features)
pred = int(model.predict(new_df)[0])
print("Tahmin Edilen Fiyat:", pred)
