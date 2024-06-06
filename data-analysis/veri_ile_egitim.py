# import pandas as pd
# import xgboost as xgb
# from xgboost import XGBRegressor 
# from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
# from sklearn.metrics import mean_squared_error, r2_score
# import numpy as np
# from sklearn import model_selection

# df_2 = pd.read_excel('dataset_etiketlenmis_son.xlsx')
# df_2.drop('Unnamed: 0', axis=1, inplace=True)
# df = df_2.copy()

# df= df[['Fiyat', 'Oda_Sayisi', 'Bulundugu_Kat', 'Isitma_Tipi',
#        'Yapi_Durumu', 'Tapu_Durumu', 'Esya_Durumu',
#        'Site_Icerisinde', 'Brut_Metrekare', 'Binanin_Yasi',
#        'Binanin_Kat_Sayisi', 'Kullanim_Durumu',
#        'Banyo_Sayisi', 'WC_Sayisi', 'Sehir', 'Ilce', 'Mahalle']]

# #bağımsız değişkenler
# X = df.drop(['Fiyat'], axis=1)
# #bağımlı değişken
# y = df['Fiyat']

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=144)

# params = {
#   'colsample_bytree': [0.4, 0.5, 0.6],
#   'learning_rate': [0.01, 0.2, 0.09],
#   'max_depth': [2, 3, 4, 5, 6],
#   'n_estimators': [100, 200, 500, 2000]
# }
# # sonuclar
# {'colsample_bytree': 0.6, 'learning_rate': 0.09, 'max_depth': 6, 'n_estimators': 2000}
# xgb = XGBRegressor()

# grid = GridSearchCV(xgb, params, cv=10, n_jobs=-1, verbose=2)
# grid.fit(X_train, y_train)
# print(grid.best_params_)

# xgb = XGBRegressor(colsample_bytree = 0.6, learning_rate = 0.09, max_depth = 6, n_estimators = 2000)

# model = xgb.fit(X_train, y_train)
# # tahminleri inceleme
# print(model.predict(X_test)[15:20])
# print(y_test[15:20])
# # sonuclar gözlemlendi
# print(model.score(X_test, y_test))
# print(model.score(X_train, y_train))
# print(np.sqrt(-1*cross_val_score(model, X_test, y_test, cv=10, scoring='neg_mean_squared_error')).mean())
# # Önemli parametreler gözlemlendi
# importance = pd.DataFrame({'Importance': model.feature_importances_*100}, index=X_train.columns)
# print(importance)

#----------------------------------------

#XGBoost
# import numpy as np
# import pandas as pd
# from sklearn.model_selection import train_test_split, GridSearchCV
# from xgboost import XGBRegressor
# from sklearn.metrics import mean_squared_error

# # Veri setini yükleyin
# df = pd.read_excel('dataset_etiketlenmis_son.xlsx').drop('Unnamed: 0', axis=1, inplace=True)

# # Bağımsız ve bağımlı değişkenleri ayırın
# # Burada, 'target' bağımlı değişkenin ismi olarak varsayılmıştır. Kendi veri setinize göre bunu değiştirin.
# X = df.drop(columns='Fiyat')
# y = df['Fiyat']

# # Veriyi eğitim ve test setlerine ayırın
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # XGBRegressor modelini tanımlayın
# xgb = XGBRegressor()

# # Hiperparametre ızgarasını tanımlayın
# param_grid = {
#     'n_estimators': [50, 100, 200, 500],
#     'learning_rate': [0.1, 0.2, 0.3],
#     'max_depth': [3, 4, 5],
#     'subsample': [0.8, 1],
#     'colsample_bytree': [0.8, 1],
#     'gamma': [0,1,5]
# }

# # GridSearchCV'yi tanımlayın
# grid_search = GridSearchCV(estimator=xgb, param_grid=param_grid, scoring='neg_mean_squared_error', cv=3, verbose=2, n_jobs=-1)

# # Grid search'i eğitin
# grid_search.fit(X_train, y_train)

# # En iyi parametreleri yazdırın
# print("En iyi parametreler:", grid_search.best_params_)

# # En iyi model ile tahmin yapın
# best_model = grid_search.best_estimator_
# y_pred = best_model.predict(X_test)

# # Performans değerlendirmesi
# mse = mean_squared_error(y_test, y_pred)
# print(f"Mean Squared Error: {mse}")

# En iyi parametreler: {'colsample_bytree': 0.8, 'gamma': 0, 'learning_rate': 0.2, 'max_depth': 5, 'n_estimators': 2000, 'subsample': 1}
# Mean Squared Error: 935994282628.4408