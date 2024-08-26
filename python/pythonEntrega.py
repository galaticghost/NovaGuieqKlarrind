#!/opt/homebrew/bin/python3

class Endereco:
    def __init__(self,logradouro,tipo_logradouro,cep,ponto_referencia = None,numero = None, complemento = None):
        self.logradouro = logradouro
        self.tipo_logradouro = tipo_logradouro
        self.cep = cep
        self.ponto_referencia = ponto_referencia
        self.numero = numero
        self.complemento = complemento
    
    def __str__(self):
        return f"""Logradouro: {self.logradouro}\nTipo de logradouro: {self.tipo_logradouro}\nCep: {self.cep}
Ponto de Referênecia: {self.ponto_referencia or "Sem ponto de Referência"}\nNúmero: {self.numero or "Sem número"}\nComplemento: {self.complemento or "Sem complemento"}\n"""
    
endereco = Endereco("Soares","Rua","89220-212")
endereco2 = Endereco("Centro","Bairro","59548-129","Perto do parque")
endereco3 = Endereco("Brasil","Avenida","76539-192",None,"950")
print(endereco)
print(endereco2)