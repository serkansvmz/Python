import requests

class ParaDonusturucu:
    def __init__(self, api_key):
        self.api_key = api_key
        self.api_url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/"

    def kurlari_getir(self, ana_para_birimi):
        url = self.api_url + ana_para_birimi
        try:
            cevap = requests.get(url, timeout=10) # 10 saniye zaman aşımı ekledik
            cevap.raise_for_status() # 4xx veya 5xx hatalarında istisna fırlatır
            veri = cevap.json()
            
            if veri.get("result") == "error":
                print(f"API Hatası: {veri.get('error-type')}")
                return None
                
            return veri["conversion_rates"]
            
        except requests.exceptions.RequestException as e:
            print(f"Bağlantı hatası oluştu: {e}")
            return None

    def donustur(self, miktar, kaynak_birim, hedef_birim):
        kurlar = self.kurlari_getir(kaynak_birim)
        
        if kurlar and hedef_birim in kurlar:
            oran = kurlar[hedef_birim]
            return miktar * oran
        else:
            print(f"Hata: '{hedef_birim}' birimi için kur verisi alınamadı.")
            return None

if __name__ == "__main__":
    # Kendi API anahtarını buraya gir
    API_KEY = "a9f4872c2d2f6ff83f2aa127"
    
    converter = ParaDonusturucu(API_KEY)

    try:
        birim_den = input("Hangi birimden? (Örn: USD): ").upper().strip()
        birim_e = input("Hangi birime? (Örn: TRY): ").upper().strip()
        miktar = float(input("Miktar: "))

        sonuc = converter.donustur(miktar, birim_den, birim_e)

        if sonuc is not None:
            # {:,2f} kullanımı binlik ayırıcı ekler
            print(f"\nSonuç: {miktar:,.2f} {birim_den} = {sonuc:,.2f} {birim_e}")
            
    except ValueError:
        print("Lütfen geçerli bir sayı giriniz.")