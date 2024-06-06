from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from xgboost import XGBRegressor
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
CORS(app)

# Veri Setini Okuma ve Ön İşleme
df = pd.read_excel('dataset_etiketlenmis_son.xlsx').drop('Unnamed: 0', axis=1)
features = ['Oda_Sayisi', 'Bulundugu_Kat', 'Isitma_Tipi', 'Yapi_Durumu',
            'Tapu_Durumu', 'Esya_Durumu', 'Site_Icerisinde', 'Brut_Metrekare',
            'Binanin_Yasi', 'Binanin_Kat_Sayisi', 'Kullanim_Durumu',
            'Banyo_Sayisi', 'WC_Sayisi', 'Sehir', 'Ilce','Mahalle']

X = df[features]
y = df['Fiyat']

# Veriyi Eğitim ve Test Kümelerine Ayırma
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=144)

# Özellik Ölçekleme
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Modelleri Oluşturma
models = {
    'xgboost': XGBRegressor(colsample_bytree=0.6, learning_rate=0.09, max_depth=6, n_estimators=2000),
    'linear_regression': LinearRegression(),
    'random_forest': RandomForestRegressor(),
    # 'svr': SVR(C=100, kernel='rbf'),
    'gradient_boosting': GradientBoostingRegressor(max_depth=16, n_estimators=3, learning_rate=0.5)
}

# Dictionary to track whether a model is fitted
is_fitted = {model_name: False for model_name in models}

def trained_models(model_name):
    return models.get(model_name, "Model not found")

def predict(model_name, values):
    model = trained_models(model_name)
    if not is_fitted[model_name]:
        model.fit(X_train, y_train)
        is_fitted[model_name] = True
        
    new_data = [values]
    new_df = pd.DataFrame(new_data, columns=features)
    pred = int(model.predict(new_df)[0])
    
    y_pred_train = model.predict(X_train)
    y_pred_test = model.predict(X_test)
    
    train_r2 = r2_score(y_train, y_pred_train)
    test_r2 = r2_score(y_test, y_pred_test)
    
    return pred, train_r2, test_r2

@app.route('/predict/<model_name>', methods=['POST'])
def predict_model(model_name):
    if model_name not in models:
        return jsonify({'error': 'Model not found'}), 404
    
    data = request.get_json()
    values = [int(value) if value else 0 for key, value in data.items()]
    pred, train_r2, test_r2 = predict(model_name, values)
    return jsonify({'result': [pred, train_r2, test_r2]})

if __name__ == '__main__':
    app.run(debug=True)