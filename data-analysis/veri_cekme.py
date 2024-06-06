from selenium import webdriver
import time
import pandas as pd

# Bu hazır fonksyonumuz adından da anlaşılacağı üzere listeyi string türüne çeviriyor.
def listToString(s):  
    
    # initialize an empty string 
    str1 = " " 
    
    # return string   
    return (str1.join(s)) 

# Bu aşamada selenium ile veri çekmeye başlıyoruz.

# chrome driverin yolunu veriyoruz. Selenium u kullanmak için gereklidir.
driver_path = "D:\PROGRAM SETUP\chromedriver.exe"
# browser adında bi değişken oluşturuyoruz ve driver yolumuzu veriyoruz. Bunu ortam değişkenlerine eklememiz gerekiyor öncesinde
browser = webdriver.Chrome(driver_path)
# browser get ile verdiğimiz adres de ki web sitesine gitmiş oluyoruz.
browser.get("https://www.emlakjet.com/satilik-konut/istanbul-sariyer/3/")

# şimdi bu sayfa içinde her linke tiklayarak verileri çekeceğiz sonra o sayfadan çıkıp bi altında ki evin linke girip onun 
# verilerini alarak sırayla bu işlemi devam ettireceğiz.

# Şuan da web sitesinin arayüzündeyiz. Amacımız evlerin detaylarına bakmak için linke tıklamak. Bunu da xpathlere göre yapacağız
# neden hepsini tek döngü de yapmadık. çünkü arada reklamlar olduğu için pathler karışıyor. Reklamları atlamak için
# böyle bi yol izledim.
i = 1
while i<=2:
    # tıkla adında değişkene find diyerek bu xpath de 1. olana gidiyor.
    tikla = browser.find_element_by_xpath("//*[@id='__next']/div[3]/div[1]/div/div[5]/div[1]/div[1]/div["+str(i)+"]")
    # click diyerek de bu linke tıklıyor ve evin detaylarına bakmak için sayfaya girmiş oluyoruz.
    tikla.click()
    # özelliklerin hepsini almak için bu sefer bu kod ile orda ki css bloğuna göre veriyi çekeceğiz.
    elements = browser.find_elements_by_css_selector("._2xeaw")
    # özellikleri bir önceki kodda aldık şimdi de evin fiyatını alıyoruz ve değişkene kaydediyoruz.
    fiyatlar = browser.find_elements_by_css_selector("._34630")
    
    # 2 tane boş liste oluşturuyoruz. Elimizde ki dağınık veriyi düzenleyip listeye atacağız.
    detaylar = []
    fiyat = []
    # çektiğimiz veriler text string olmadığı için verileri stringe çevirip demin oluşturduğumuz boş listeye atıyoruz.
    # unutmayalım ki verileri çektiğiniz de liste olarak gelir.
    for i in fiyatlar:
        print(i.text)
        fiyat.append(i.text)
    # özellikleri de stringe çevirerek listeye atıyoruz.
    for i in elements:
        print(i.text)
        detaylar.append(i.text)
    # elimizde string olan liste halinde veriler var. Önceden oluşturduğumuz listeden stringe çevirme fonksyonuyla stringe 
    # çeviyoruz.
    det_str = listToString(detaylar)
    # string verimizi split ile satırlara göre ayırıyoruz. Ve ayri adında değişkene atıyoruz.
    ayri = det_str.split("\n")
    # demin oluşturduğumuz ayri değişkenini DataFrame çeviriyoruz. 
    df = pd.DataFrame(ayri)
    # Verimizde ki gereksiz verilerden kurtulmak için onları ayırıyoruz.
    df_yeni = df.iloc[7:53]
    df_yeni.iloc[45] = df_yeni.iloc[45].str[0:3]
    # değişiklikler yaptığımız için indexleri resetliyoruz.
    df_yeni = df_yeni.reset_index()
    # gereksiz oluşan şndex sütununu siliyoruz.
    df_yeni.drop("index", axis = 1, inplace = True)
    # verilerimizi tekrar listeye çeviriyorum.
    df_liste = df_yeni.values.tolist()
    # içerikler adında boş liste oluşturuyprum amacım şu şuan elimizde ki veri sütun adlarını ve içeriklerini barındırıyor.
    # içerikleri sütun adlarından ayırmak için bu işlemi yapıyoruz.
    içerikler =[]
    i = 1
    while i <= 45:
        print(df_liste[i])
        içerikler.append(df_liste[i])
        i = i+2
    # Hatırlarsanız fiyatı başka bi yerde çekmiştik ve bunu da içeriklere yeni bi sütuna ekliyoruz.
    # öncesinde fiyat değişkeninde ki gereksiz verileri siliyoruz. TL yazısını ve strip ile gereksiz boşlukları
    fiyat_sade = fiyat[1].strip()
    fiyat_sade = fiyat_sade.replace("TL","")
    # içerikler kısmına fiyatı ekliyoruz.
    içerikler.append([fiyat_sade])
    # şuan liste halinde olan verimizi Df e çeviriyoruz ve transpozunu alıyoruz.
    df_içerikler = pd.DataFrame(içerikler).T
    # verimizi csv dosyasına çeviriyoruz ve modu append yapıyoruz. Çünkü diğer çektiğimiz verileri de oraya ekleyeceğiz.
    # eğer mode = a yapmassak diğer gelen veriyi üzerine yazacaktır.
    df_içerikler.to_csv(r"zingat3.csv",encoding="utf-8",index=False, mode="a")
    
    # i değişkeni sayfada ki evlerin xpath de ki sayısıydı
    i = i+1
    # bu kod ile bi önceki sayfaya geçiyoruz.
    browser.execute_script("window.history.go(-1)")

    
print("ilk kısım çalıştı")

j = 4
while j <= 7:
    tikla = browser.find_element_by_xpath("//*[@id='__next']/div[3]/div[1]/div/div[5]/div[1]/div[1]/div["+str(j)+"]")
    tikla.click()
    
    elements = browser.find_elements_by_css_selector("._2xeaw")

    fiyatlar = browser.find_elements_by_css_selector("._34630")
    
    detaylar = []
    fiyat = []
    
    for i in fiyatlar:
        print(i.text)
        fiyat.append(i.text)
    
    for i in elements:
        print(i.text)
        detaylar.append(i.text)
    
    det_str = listToString(detaylar)
    ayri = det_str.split("\n")
    
    df = pd.DataFrame(ayri)
    df_yeni = df.iloc[7:53]
    df_yeni.iloc[45] = df_yeni.iloc[45].str[0:3]
    
    df_yeni = df_yeni.reset_index()
    df_yeni.drop("index", axis = 1, inplace = True)
    df_liste = df_yeni.values.tolist()
    
    içerikler =[]
    i = 1
    while i <= 45:
        print(df_liste[i])
        içerikler.append(df_liste[i])
        i = i+2
        
    fiyat_sade = fiyat[1].strip()
    fiyat_sade = fiyat_sade.replace("TL","")
    içerikler.append([fiyat_sade])
    df_içerikler = pd.DataFrame(içerikler).T
    
    df_içerikler.to_csv(r"zingat3.csv",encoding="utf-8",index=False, mode = "a")

    
    j = j+1
    browser.execute_script("window.history.go(-1)")

print("ikinci kısım çalıştı")


    
k = 9
while k<=10:
    tikla = browser.find_element_by_xpath("//*[@id='__next']/div[3]/div[1]/div/div[5]/div[1]/div[1]/div["+str(k)+"]")
    tikla.click()
    
    print("üçüncü ksıım 1")
    
    elements = browser.find_elements_by_css_selector("._2xeaw")

    fiyatlar = browser.find_elements_by_css_selector("._34630")
    
    detaylar = []
    fiyat = []
    
    for i in fiyatlar:
        print(i.text)
        fiyat.append(i.text)
    
    for i in elements:
        print(i.text)
        detaylar.append(i.text)
    
    det_str = listToString(detaylar)
    ayri = det_str.split("\n")
    
    df = pd.DataFrame(ayri)
    df_yeni = df.iloc[7:53]
    df_yeni.iloc[45] = df_yeni.iloc[45].str[0:3]
    
    df_yeni = df_yeni.reset_index()
    df_yeni.drop("index", axis = 1, inplace = True)
    df_liste = df_yeni.values.tolist()
    
    içerikler =[]
    i = 1
    while i <= 45:
        print(df_liste[i])
        içerikler.append(df_liste[i])
        i = i+2
        
    fiyat_sade = fiyat[1].strip()
    fiyat_sade = fiyat_sade.replace("TL","")
    içerikler.append([fiyat_sade])
    df_içerikler = pd.DataFrame(içerikler).T
    
    df_içerikler.to_csv(r"zingat3.csv",encoding="utf-8",index=False,mode="a")
    
    
    
    k = k+1
    browser.execute_script("window.history.go(-1)")
    
print("üçüncü kısım çalıştı")

l = 12
while l<=13:
    tikla = browser.find_element_by_xpath("//*[@id='__next']/div[3]/div[1]/div/div[5]/div[1]/div[1]/div["+str(l)+"]")
    tikla.click()
    
    elements = browser.find_elements_by_css_selector("._2xeaw")

    fiyatlar = browser.find_elements_by_css_selector("._34630")
    
    detaylar = []
    fiyat = []
    
    for i in fiyatlar:
        print(i.text)
        fiyat.append(i.text)
    
    for i in elements:
        print(i.text)
        detaylar.append(i.text)
    
    det_str = listToString(detaylar)
    ayri = det_str.split("\n")
    
    df = pd.DataFrame(ayri)
    df_yeni = df.iloc[7:53]
    df_yeni.iloc[45] = df_yeni.iloc[45].str[0:3]
    
    df_yeni = df_yeni.reset_index()
    df_yeni.drop("index", axis = 1, inplace = True)
    df_liste = df_yeni.values.tolist()
    
    içerikler =[]
    i = 1
    while i <= 45:
        print(df_liste[i])
        içerikler.append(df_liste[i])
        i = i+2
        
    fiyat_sade = fiyat[1].strip()
    fiyat_sade = fiyat_sade.replace("TL","")
    içerikler.append([fiyat_sade])
    df_içerikler = pd.DataFrame(içerikler).T
    
    df_içerikler.to_csv(r"zingat3.csv",encoding="utf-8",index=False,mode="a")
    
    
    
    l = l+1
    browser.execute_script("window.history.go(-1)")
    
print("dördüncü kısım çalıştı")
    
m = 15
while m<=30:
    tikla = browser.find_element_by_xpath("//*[@id='__next']/div[3]/div[1]/div/div[5]/div[1]/div[1]/div["+str(m)+"]")
    tikla.click()
    
    elements = browser.find_elements_by_css_selector("._2xeaw")

    fiyatlar = browser.find_elements_by_css_selector("._34630")
    
    detaylar = []
    fiyat = []
    
    for i in fiyatlar:
        print(i.text)
        fiyat.append(i.text)
    
    for i in elements:
        print(i.text)
        detaylar.append(i.text)
    
    det_str = listToString(detaylar)
    ayri = det_str.split("\n")
    
    df = pd.DataFrame(ayri)
    df_yeni = df.iloc[7:53]
    df_yeni.iloc[45] = df_yeni.iloc[45].str[0:3]
    
    df_yeni = df_yeni.reset_index()
    df_yeni.drop("index", axis = 1, inplace = True)
    df_liste = df_yeni.values.tolist()
    
    içerikler =[]
    i = 1
    while i <= 45:
        print(df_liste[i])
        içerikler.append(df_liste[i])
        i = i+2
        
    fiyat_sade = fiyat[1].strip()
    fiyat_sade = fiyat_sade.replace("TL","")
    içerikler.append([fiyat_sade])
    df_içerikler = pd.DataFrame(içerikler).T
    
    
    df_içerikler.to_csv(r"zingat3.csv",encoding="utf-8",index=False,mode="a")
    
    print("beşinci kısım 1")
    m = m+1
    browser.execute_script("window.history.go(-1)")
    
print("beşinci kısım son 1 ")