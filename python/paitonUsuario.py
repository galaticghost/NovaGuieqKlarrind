from pythonEntrega import Endereco

class Usuario:
    
    def __init__(self,nome,sobrenome,email,endereco):
        self.__nome = nome.capitalize()
        self.__sobrenome = sobrenome.capitalize()
        self.__email = email
        self.__endereco = endereco
        
    def __str__(self):
        return f"{self.nome},{self.sobrenome} \n {self.endereco}"

    @property
    def nome(self):
        return self.__nome.capitalize()

    @nome.setter
    def nome(self,dado):
        self.__nome = dado
        
    @property
    def sobrenome(self):
        return self.__sobrenome.capitalize()

    @sobrenome.setter
    def sobrenome(self,dado):
        self.__sobrenome = dado
        
    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self,dado):
        self.__email = dado
        
    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self,dado):
        self.__endereco = dado

endereco2 = Endereco("Centro","Bairro","59548-129","Perto do parque") 
user = Usuario("Bola","Cunha","bola@bola.com",endereco2)

print(user)