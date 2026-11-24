class Carro:
    #metodo dunder: Double Underscore Method
    # Metodos especiais e restritos
    def___nit__(self, modelo ,  cor)
    self.Modelo = modelo
    self.cor = cor
    self.velocidade = 0
    
    def acelerar(self, incremento):
        self.velocidade += incremento
        print(f'O carro {self.modelo} acelerou para {self.velocidade} km/h')
        
    def parar(self):
        self.velocidade = 0
        print(f'O carro {self.modelo} parou!')
     
def desacelerar(self) :
    while self.velocidade > 0:
        self.velocidade = max(0, self.velocidade - 5)          
    
# Criando um objeto: O Carro!
carrroInstrutor = Carro("Jetta GLI", "preto")
carroLucas = Carro("T-Cross","Preto")  
carroRafael = Carro("Saveiro","branco") 

carroInstrutor.acelerar(60) 
carroInstrutor.acelerar(10) 
carroInstrutor.acelerar() 

carroLucas.acelerar(60)