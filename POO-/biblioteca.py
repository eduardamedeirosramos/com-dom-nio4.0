class Pessoa:
    def __init__(self,nome, idade,peso ):
        self.nome=nome
        self.idade=idade
        self.peso=peso
        self.comendo=False
        self.falando=False
        self.dormindo=False
    def falar(self):
     if self.falando == False:
         if self.comendo == False:
             if self.dormindo== False:
                 self.falando = True
                 print(f"{self.nome} está falando")

             else:
                print(f"{self.nome} não pode falar pois está dormindo")
         else:
             print(f"{self.nome} não pode falar pois está comendo")
     else:
         print(f"{self.nome} não pode falar pois já está falando")

    def comer(self):
        if self.falando == False:
            if self.comendo == False:
                if self.dormindo == False:
                    self.comendo = True
                    print(f"{self.nome} está comendo")
                else:
                 print(f"{self.nome} não pode dormir pois já está dormindo")
            else:
                print(f"{self.nome} não pode dormir pois está comendo")
        else:
            print(f"{self.nome} não pode dormir pois já está falando")


    def dormir(self):
        if self.falando == False:
            if self.comendo == False:
                if self.dormindo == False:
                    self.dormindo = True
                    print(f"{self.nome} está dormindo")
                else:
                 print(f"{self.nome} não pode dormir pois já está dormindo")
            else:
                print(f"{self.nome} não pode dormir pois está comendo")
        else:
            print(f"{self.nome} não pode dormir pois já está falando")

    def PararComer(self):
        self.Comendo= False
        print(f"{self.nome} parou de comer")

    def PararFalar(self):
        self.Falando = False
        print(f"{self.nome} parou de falar")

    def PararDormir(self):
        self.Dormindo = False
        print(f"{self.nome} parou de dormir")

