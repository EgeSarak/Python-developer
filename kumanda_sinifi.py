import random
import time


class Kumanda():
    def __init__(self,tv_durum = "Kapalı",tv_ses = 0,kanal_listesi =["TRT"],kanal="Trt"):
        
        self. tv_durum = tv_durum
        self.tv_ses = tv_ses
        self.kanal_listesi = kanal_listesi
        self.kanal = kanal
        
    def tv_ac(self):
        if self.tv_durum == "Açık":
            print("Televizyon açık")
        else:
            print("Televizyon Açılıyor")
            self.tv_durum = "Açık"
            
    def tv_kapat(self):
        if self.tv_durum == "Kapalı":
            print("Televizyon kapalı")
        else:
            print("Televizyon kapanıyor")
            self.tv_durum ="Kapalı" 
            
    def ses_ayarlari(self):
        while True:
            cevap = input("sesi azalat: '<'\nsesi artır: '>'\nÇıkış: çıkış")
            
            if cevap == "<":
                if self.tv_ses != 0:
                    self.tv_ses -= 1
                    print("Ses: ",self.tv_ses)
            elif cevap ==">":
                if self.tv_ses != 31:
                    self.tv_ses += 1
                    print("Ses: ",self.tv_ses)
            else:
                print("Ses güncellendi: ",self.tv_ses)
                break  
    
    def kanal_ekle(self,kanal_ismi):
        print("Kanal ekleniyor...")
        time.sleep(1)
        
        self.kanal_listesi.append(kanal_ismi)
        
        print("Kanal eklendi...")
        
    def rastgele_kanal(self):
        rastgele = random.randint(0,len(self.kanal_listesi)-1)
        self.kanal = self.kanal_listesi[rastgele]
        
        print("Şu anki Kanal: ",self.kanal)
    
    def __len__(self):
        return len(self.kanal_listesi)
    
    def __str__(self):
        return f"TV durumu: {self.tv_durum}\nTV ses: {self.tv_ses}\nKanal listesi: {self.kanal_listesi}\nŞu anki kanal: {self.kanal}"        
    
kumanda = Kumanda()
  
print("""
      
Televizyon Uygulaması

1. Tv aç 

2. Tv kapat

3. Ses ayarları

4. kanal ekle

5. kanal sayısını öğrenme

6. Rastegele kanal seçme

7. Televizyon Bilgileri

Çıkmak için 'q' ya basın.
     
""")   


while True:
    islem =input("İşlemi seçin: ")
    if islem == "q":
        print("Program sonlandırılıyor...")
        break
    
    elif islem == "1":
        kumanda.tv_ac()
    elif islem == "2":
        kumanda.tv_kapat()
    elif islem == "3":
        kumanda.ses_ayarlari()
    elif islem == "4":
        kanal_isimleri = input("Kanal isismlerini ',' ile ayırarak girin: ")
        kanal_listesi = kanal_isimleri.split(",")
        for eklenecekler in kanal_listesi:
            kumanda.kanal_ekle(eklenecekler)
    elif islem == "5":
        print("Kanal Sayısı: ",len(kumanda))   
    elif islem == "6":
        kumanda.rastgele_kanal()
    elif islem == "7":
        print(kumanda)    
    else:
        print("Geçersiz işlem.........")            
        
        
                
            
        
        
    
            
                                               
            
                                      
                
               
        