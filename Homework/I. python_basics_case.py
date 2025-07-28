#####################################
# Python Temelleri - Ödev Scripti
#####################################

# Soru 1:
# Bir integer, bir float ve bir complex sayı tanımlayın.
# Bu sayıların türlerini yazdırın ve aralarında 1-2 işlem yapın.
a = 10  # integer
b = 3.5  # float
c = 2 + 3j  # complex

print(type(a), type(b), type(c))
print(a + b, b * c)


# Soru 2:
# İsminizi içeren bir string değişkeni oluşturun.
# Bu stringin ilk ve son karakterini yazdırın. Ayrıca tüm harfleri büyük yaparak ekrana yazdırın.
name = "Metehan"
print(name[0], name[-1])
print(name.upper())




# Soru 3:
# Aşağıdaki string içinde "veri" kelimesi geçiyor mu kontrol edin.
# Ardından bu stringi boşluklardan bölerek liste haline getirin.

sentence = "Veri bilimi yapay zeka ile birleştiğinde güçlü sonuçlar doğurabilir."

print("veri" in sentence.lower())
words = sentence.split()
print(words)



# Soru 4:
# İçerisinde 3 farklı türde veri bulunan bir liste oluşturun.
# Listenin uzunluğunu, ilk ve son elemanını yazdırın.
# Ardından bu listeye yeni bir eleman ekleyin ve ikinci elemanı silin.

liste = [42, "Python", 3.14]
print(len(lisrte) , liste[0], liste[-1])
liste.append("Metehan")
print(liste)
liste.pop(1)




# Soru 5:
# 2 parametre alan bir fonksiyon yazın. Bu fonksiyon, aldığı iki sayının ortalamasını dönsün.
def ortalama(sayi1, sayi2):
    return (sayi1 + sayi2) / 2

print(ortalama(10, 20))

# Soru 6:
# Kullanıcının yaşına göre mesaj yazdıran bir fonksiyon yazın:
# 18'den küçükse "Çok gençsin!", 18-40 arasıysa "Harika bir yaştasın!", 40'tan büyükse "Deneyim önemli!" mesajını yazdırsın.
def yas_mesajı(yas):
    if yas < 18:
        return "Çok gençsin!"
    elif 18 <= yas <= 40:
        return "Harika bir yaştasın!"
    else:
        return "Deneyim önemli!"

print(yas_mesajı(25))



# Soru 7:
# İçerisinde sayılar olan bir liste içindeki sayıları dolaşarak 2 katını ekrana yazdırın (for döngüsü ile).
sayilar = [1, 2, 3, 4, 5]
for i in sayilar:
    print(i*2)
    print(i**2) # Karekökünü de yazdırabilirsiniz. 


# Soru 8:
# 1'den başlayarak 20 dahil olacak şekilde çift sayıları yazdırın (while döngüsü ile).
a = 1
while a <= 20:
    if a % 2 == 0:
        print(a)
    a += 1

# Soru 9:
# Bir çalışanın haftalık maaşını hesaplayan bir fonksiyon yazın.
# Saatlik ücreti ve haftalık toplam çalışma saati parametre olarak alınsın.
# Haftada 40 saatten fazla çalıştıysa, fazla saatler için %50 zamlı ücret ödensin (mesai).
# Örnek: 45 saat çalışan biri için 5 saatlik mesai uygulanmalı.
def maas_hesapla(saatlik_ucret, toplam_saat):
    if toplam_saat > 40:
        mesai_saat = toplam_saat - 40
        toplam_ucret = (40 * saatlik_ucret) + (mesai_saat * saatlik_ucret * 1.5)
    else:
        toplam_ucret = toplam_saat * saatlik_ucret
    return toplam_ucret
        
print(maas_hesapla(20, 45) ) # Örnek kullanım
