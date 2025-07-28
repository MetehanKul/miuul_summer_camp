###############################
# Numpy & Pandas - Ödev Soruları
###############################

import numpy as np
import pandas as pd
import seaborn as sns

###############################
# Soru 1:
# 1D ve 2D array'ler oluşturun.
# Bu array’lerin boyut, eleman sayısı ve şekil bilgilerini yazdırın.
array_1d = np.array([1, 2, 3, 4, 5])
array_2d = np.array([[1, 2, 3], [4, 5, 6]])

print("1D Array - Boyut:", array_1d.ndim)
print("1D Array - Eleman Sayısı:", array_1d.size)
print("1D Array - Şekil:", array_1d.shape)

print("2D Array - Boyut:", array_2d.ndim)
print("2D Array - Eleman Sayısı:", array_2d.size)
print("2D Array - Şekil:", array_2d.shape)

###############################
# Soru 2:
# 5 elemanlı rastgele sayılardan oluşan bir array oluşturun.
# Elemanların ortalamasını, standart sapmasını ve medyanını bulun.

a = np.random.rand(5)
print("Array:", a)
print("Ortalama:", a.mean())
print("Standart Sapma:", a.std())
print("Medyan:", np.median(a))

###############################
# Soru 3:
# 0 ile 1 arasında 10 eşit aralıklı sayı üretin.
# Bu sayılardan 0.5'ten büyük olanları filtreleyip yazdırın.

np.random.seed(0)  # Tekrarlanabilirlik için
sayilar = np.linspace(0, 1, 10)

sayilar[sayilar > 0.5]
print("0.5'ten büyük sayılar:", filtrelenmis)


###############################
# Soru 4:
# Pandas Series kullanarak öğrencilerin yaşlarını tutan bir seri oluşturun.
# Yaş ortalamasını ve en küçük yaşı bulun.
ogrenci_yaslari = pd.Series([18, 21, 19, 22], name="Yaşlar")
print("Öğrenci Yaşları:\n", ogrenci_yaslari)
print("Yaş Ortalaması:", ogrenci_yaslari.mean())
print("En Küçük Yaş:", ogrenci_yaslari.min())


###############################
# Soru 5:
# seaborn içerisinden "diamonds" veri setini alın.
# Sadece "carat" ve "price" sütunlarını içeren ilk 5 satırı yazdırın.
df = sns.load_dataset("diamonds")
print("Carat ve Price İlk 5 Satır:\n", df[["carat", "price"]].head())

###############################
# Soru 6:
# Fiyatı 15.000’den fazla olan kaç elmas var?
filt = df["price"] > 15000
count = df[filt].count()[0]
print("Fiyatı 15.000'den fazla olan elmas sayısı:", count)

###############################
# Soru 7:
# “cut” sütunundaki her bir kesim tipi için ortalama fiyatı(price) hesaplayın.
ortalama_fiyat = df.groupby("cut")["price"].mean()
print("Kesim Tipine Göre Ortalama Fiyatlar:\n", ortalama_fiyat)

###############################
# Soru 8:
# pivot_table kullanarak her “cut” tipi için hem ortalama “carat” hem de “price” değerlerini gösterin.
pivot_table = df.pivot_table(values=["carat", "price"], index="cut", aggfunc="mean")
print("Kesim Tipine Göre Ortalama Carat ve Price:\n", pivot_table)

###############################
# Soru 9:
# “color” sütununda kaç farklı renk olduğunu bulun. Her bir rengin kaç kez geçtiğini de yazdırın.
color = df["color"].unique()
color_count = df["color"].value_counts()
print("Farklı Renkler:", color)
print("Renklerin Sayısı:\n", color_count)


###############################
# Soru 10:
# “cut” ve “clarity” kombinasyonlarına göre ortalama fiyatları hesaplayın.

df.groupby(["cut" , "clarity"])["price"].mean()

df.head()
df["clarity"].value_counts()