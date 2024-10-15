class Humano:
    
    def __init__(self,nome,pai,mae,conjuge):
        self.nome = nome
        self.pai = pai
        self.mae = mae
        self.conjuge = conjuge
        self.filhos = []
        
    def __repr__(self):
        return self.nome

class ArvoreGenealogica:
    
    def __init__(self,inicio,inicio_mae):
        self.inicio_pai = inicio
        self.inicio_mae = inicio_mae
        
    def printa_arvore(self):
        print(f"{self.inicio_pai} e {self.inicio_mae} tem {len(self.inicio_pai.filhos)} filho(as)")
        for filho in self.inicio_pai.filhos:
            self.printa_filhos(filho)

            
    def printa_filhos(self,humano):
        if len(humano.filhos) == 0:
            return None
        
        print(f"{humano} e {humano.conjuge} tem {len(humano.filhos)} filho(as)")
        
        for filho in humano.filhos:
            self.printa_filhos(filho)
            


jorge = Humano("Jorge",None,None,None)
josefina = Humano("Josefina",None,None,jorge)
jorge.conjuge = josefina

junior = Humano("Junior",jorge,josefina,None)
jussarra = Humano("Jussara",None,None,junior)
junior.conjuge = jussarra

jose = Humano("Jose",junior,jussarra,None)

joao = Humano("João",jorge,josefina,None)
joaquina = Humano("Joaquina",None,None,joao)
joao.conjuge = joaquina

jonas = Humano("Jonas",joao,joaquina,None)

jorge.filhos.append(joao)
joao.filhos.append(jonas)
jorge.filhos.append(junior)
junior.filhos.append(jose)

arvore = ArvoreGenealogica(jorge,josefina)
arvore.printa_arvore()
                
        