import os
from random import choice

class MP3Calar():
    def __init__(self, sarkiListesi=None):
        self.sarkiListesi = sarkiListesi if sarkiListesi else []
        self.suanCalanSarki = "Çalan şarkı yok"
        self.ses = 50
        self.durum = True
        
    def sarkiSec(self):
        if not self.sarkiListesi:
            print("\nListede şarkı yok! Önce şarkı ekleyin.")
            return

        for i, sarki in enumerate(self.sarkiListesi, 1):
            print(f"{i}) {sarki}")
        
        try:
            secilen = int(input("\nSeçilen şarkı no: "))
            if 1 <= secilen <= len(self.sarkiListesi):
                self.suanCalanSarki = self.sarkiListesi[secilen - 1]
            else:
                print("Geçersiz numara!")
        except ValueError:
            print("Lütfen sadece sayı giriniz!")

    def sesArttir(self):
        if self.ses < 100:
            self.ses = min(100, self.ses + 10) # 100'ü geçmesin

    def sesAzalt(self):
        if self.ses > 0:
            self.ses = max(0, self.ses - 10) # 0'ın altına düşmesin

    def rastgeleSarkiSec(self):
        if self.sarkiListesi:
            self.suanCalanSarki = choice(self.sarkiListesi)
        else:
            print("Liste boş!")

    def sarkiEkle(self):
        sanatci = input("Sanatçı: ")
        sarki = input("Şarkı: ")
        self.sarkiListesi.append(f"{sanatci} - {sarki}")

    def sarkiSil(self):
        if not self.sarkiListesi:
            print("Silinecek şarkı yok!")
            return
            
        for i, sarki in enumerate(self.sarkiListesi, 1):
            print(f"{i}) {sarki}")
            
        try:
            silinecek = int(input("\nSilinecek şarkı no: "))
            self.sarkiListesi.pop(silinecek - 1)
        except (ValueError, IndexError):
            print("Hatalı seçim yaptınız!")

    def menuGoster(self):
        # Ekranı temizler (Windows için 'cls', Mac/Linux için 'clear')
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"""
*********** MP3 ÇALAR ***********
Çalan Şarkı : {self.suanCalanSarki}
Ses Düzeyi  : %{self.ses}
Şarkı Sayısı: {len(self.sarkiListesi)}
---------------------------------
1) Şarkı Seç
2) Ses Arttır (+)
3) Ses Azalt (-)
4) Rastgele Şarkı Çal
5) Şarkı Ekle
6) Şarkı Sil
7) Programı Kapat
*********************************
""")

    def calistir(self):
        self.menuGoster()
        secim = input("Seçiminizi Giriniz (1-7): ")

        if secim == '1': self.sarkiSec()
        elif secim == '2': self.sesArttir()
        elif secim == '3': self.sesAzalt()
        elif secim == '4': self.rastgeleSarkiSec()
        elif secim == '5': self.sarkiEkle()
        elif secim == '6': self.sarkiSil()
        elif secim == '7': self.durum = False
        else: print("Hatalı giriş, devam etmek için Enter'a basın..."); input()

# Programı başlat
mp3 = MP3Calar(["Daft Punk - Instant Crush", "Tarkan - Kuzu Kuzu"])
while mp3.durum:
    mp3.calistir()

print("Müzik çalar kapatıldı.")