import "bootstrap/dist/css/bootstrap.min.css";
import { useState } from "react";
import axios from "axios";
import {
  odaSayisi,
  bulunduguKat,
  district,
  isitmaTipi,
  yapiDurumu,
  tapuDurumu,
  esyaDurumu,
  siteIcerisinde,
  binaninYasi,
  binaninKatSayisi,
  kullanimDurumu,
  banyoSayisi,
  wcSayisi,
  cities,
  cityDataMap,
  ilceDataMap,
  mahalleDataMap,
  neighborhoods,
} from "./dataset";

function MainPage() {
  const [data, setData] = useState({
    Oda_Sayisi: "",
    Bulundugu_Kat: "",
    Isitma_Tipi: "",
    Yapi_Durumu: "",
    Tapu_Durumu: "",
    Esya_Durumu: "",
    Site_Icerisinde: "",
    Brut_Metrekare: "",
    Binanin_Yasi: "",
    Binanin_Kat_Sayisi: "",
    Kullanim_Durumu: "",
    Banyo_Sayisi: "",
    WC_Sayisi: "",
    Sehir: "",
    Ilce: "",
    Mahalle: "",
  });
  const [result, setResult] = useState("");
  const [districtOptions, setDistrictOptions] = useState([]);
  const [neighborhoodOptions, setNeighborhoodOptions] = useState([]);
  const [algorithm, setAlgorithm] = useState("first");

  const handleChange = (e) => {
    const { name, value } = e.target;

    if (name === "Sehir" && value !== "") {
      const districts = Object.keys(neighborhoods[value] || {});
      setDistrictOptions(districts);
      setNeighborhoodOptions([]);
      setData({ ...data, Sehir: value, Ilce: "", Mahalle: "" });
    } else if (name === "Ilce" && value !== "") {
      const neighborhoodsInDistrict =
        (neighborhoods[data.Sehir] || {})[value] || [];
      setNeighborhoodOptions(neighborhoodsInDistrict);
      setData({ ...data, Ilce: value, Mahalle: "" });
    } else {
      setData({ ...data, [name]: value });
    }
  };

  const handleAlgorithmChange = (e) => {
    setAlgorithm(e.target.value);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const transformedData = Object.fromEntries(
        Object.entries(data).map(([key, value]) => {
          const dataset = {
            WC_Sayisi: wcSayisi,
            Banyo_Sayisi: banyoSayisi,
            Kullanim_Durumu: kullanimDurumu,
            Binanin_Kat_Sayisi: binaninKatSayisi,
            Binanin_Yasi: binaninYasi,
            Site_Icerisinde: siteIcerisinde,
            Esya_Durumu: esyaDurumu,
            Tapu_Durumu: tapuDurumu,
            Yapi_Durumu: yapiDurumu,
            Isitma_Tipi: isitmaTipi,
            Bulundugu_Kat: bulunduguKat,
            Oda_Sayisi: odaSayisi,
            Sehir: cityDataMap,
            Ilce: ilceDataMap,
            Mahalle: mahalleDataMap,
          }[key];
          return [key, dataset ? dataset[value] : value];
        })
      );

      const response = await axios.post(
        `http://127.0.0.1:5000/predict/${algorithm}`,
        transformedData
      );
      setResult(response.data.result);
    } catch (error) {
      console.error("Error:", error);
    }
  };

  return (
    <div className="container mt-5">
      <h1 className="text-center mb-4">Ev Fiyat Tahmini</h1>
      <form onSubmit={handleSubmit}>
        <div className="text-center mb-4">
          <label htmlFor="algorithm">Algoritma Seçiniz</label>
          <select
            className="form-control d-inline-block w-auto ml-2"
            id="algorithm"
            value={algorithm}
            onChange={handleAlgorithmChange}
          >
            <option value="first">Seçiniz</option>
            <option value="xgboost">XGBoost</option>
            <option value="linear_regression">Linear Regression</option>
            <option value="random_forest">Random Forest</option>
            {/* <option value="svr">SVR</option> */}
            <option value="gradient_boosting">Gradient Boosting</option>
          </select>
        </div>
        <div className="form-row row">
          {Object.entries(data).map(([key, value], index) => (
            <div className="form-group col-md-4" key={key}>
              <label htmlFor={key}>{key.replace("_", " ")}</label>
              {key === "Sehir" || key === "Ilce" || key === "Mahalle" ? (
                <select
                  className="form-control"
                  id={key}
                  name={key}
                  value={value}
                  onChange={handleChange}
                >
                  <option value="">
                    {key === "Sehir"
                      ? "Şehir Seçiniz"
                      : key === "Ilce"
                      ? "İlçe Seçiniz"
                      : "Mahalle Seçiniz"}
                  </option>
                  {key === "Sehir"
                    ? cities.map((city) => (
                        <option key={city} value={city}>
                          {city}
                        </option>
                      ))
                    : key === "Ilce"
                    ? districtOptions.map((district) => (
                        <option key={district} value={district}>
                          {district}
                        </option>
                      ))
                    : neighborhoodOptions.map((neighborhood) => (
                        <option key={neighborhood} value={neighborhood}>
                          {neighborhood}
                        </option>
                      ))}
                </select>
              ) : key === "Brut_Metrekare" ? (
                <input
                  type="text"
                  className="form-control"
                  id={key}
                  name={key}
                  value={data[key]}
                  placeholder="Brüt Metrekare"
                  onChange={handleChange}
                />
              ) : (
                <select
                  className="form-control"
                  id={key}
                  name={key}
                  value={value}
                  onChange={handleChange}
                >
                  <option value="">Seçiniz</option>
                  {key === "Oda_Sayisi" &&
                    Object.keys(odaSayisi).map((oda) => (
                      <option key={oda} value={oda}>
                        {oda}
                      </option>
                    ))}
                  {key === "Bulundugu_Kat" &&
                    Object.keys(bulunduguKat).map((kat) => (
                      <option key={kat} value={kat}>
                        {kat}
                      </option>
                    ))}
                  {key === "Isitma_Tipi" &&
                    Object.keys(isitmaTipi).map((tip) => (
                      <option key={tip} value={tip}>
                        {tip}
                      </option>
                    ))}
                  {key === "Yapi_Durumu" &&
                    Object.keys(yapiDurumu).map((durum) => (
                      <option key={durum} value={durum}>
                        {durum}
                      </option>
                    ))}
                  {key === "Tapu_Durumu" &&
                    Object.keys(tapuDurumu).map((durum) => (
                      <option key={durum} value={durum}>
                        {durum}
                      </option>
                    ))}
                  {key === "Esya_Durumu" &&
                    Object.keys(esyaDurumu).map((durum) => (
                      <option key={durum} value={durum}>
                        {durum}
                      </option>
                    ))}
                  {key === "Site_Icerisinde" &&
                    Object.keys(siteIcerisinde).map((site) => (
                      <option key={site} value={site}>
                        {site}
                      </option>
                    ))}
                  {key === "Binanin_Yasi" &&
                    Object.keys(binaninYasi).map((yas) => (
                      <option key={yas} value={yas}>
                        {yas}
                      </option>
                    ))}
                  {key === "Binanin_Kat_Sayisi" &&
                    Object.keys(binaninKatSayisi).map((kat) => (
                      <option key={kat} value={kat}>
                        {kat}
                      </option>
                    ))}
                  {key === "Kullanim_Durumu" &&
                    Object.keys(kullanimDurumu).map((durum) => (
                      <option key={durum} value={durum}>
                        {durum}
                      </option>
                    ))}
                  {key === "Banyo_Sayisi" &&
                    Object.keys(banyoSayisi).map((banyo) => (
                      <option key={banyo} value={banyo}>
                        {banyo}
                      </option>
                    ))}
                  {key === "WC_Sayisi" &&
                    Object.keys(wcSayisi).map((wc) => (
                      <option key={wc} value={wc}>
                        {wc}
                      </option>
                    ))}
                </select>
              )}
            </div>
          ))}
        </div>
        <div className="text-center mt-3">
          <button type="submit" className="btn btn-primary">
            Gönder
          </button>
        </div>
      </form>
      <div className="mt-4 p-3 border rounded">
        <h2>Sonuçlar</h2>
        <p>Tahmin: {result[0]} TL</p>
        <p>Eğitim R2: {result[1]}</p>
        <p>Test R2: {result[2]}</p>
      </div>
    </div>
  );
}

export default MainPage;
