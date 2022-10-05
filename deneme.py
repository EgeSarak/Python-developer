class Araba:
    def __init__(self,model,yas,renk,beygir,kapi):
        self.model = model
        self.yas = yas
        self.renk = renk
        self.beygir = beygir
        self.kapi = kapi
    
    def run(self):
        print(f"araba özellikleri: {self.model},{self.yas},{self.renk},{self.beygir},{self.kapi}")
          


araba1=Araba("BMW",7,"kırmızı",150,2)
araba2=Araba("mercedes",5,"mor",110,3)


print(araba1.run())