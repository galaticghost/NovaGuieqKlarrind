import random

class Bicho():
    nome: str
    fome: bool
    feliz: bool
    cansado: bool

    def __init__(self,nome):
        self.__nome = nome
        self.__fome = False
        self.__feliz = True
        self.__cansado = False

    def status(self):
        if random.randint(0,1) == 0:
            self.__fome = True
        else:
            self.__fome = False

        if random.randint(0,1) == 0:
            self.__feliz = True
        else:
            self.__feliz = False
        
        if random.randint(0,1) == 0:
            self.__cansado = True
        else:
            self.__cansado = False

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self,nome):
        self.__nome = nome

    @property
    def fome(self):
        return self.__fome
    
    @fome.setter
    def fome(self,fome):
        self.__fome = fome

    @property
    def feliz(self):
        return self.__feliz
    
    @feliz.setter
    def feliz(self,feliz):
        self.__feliz = feliz

    @property
    def cansado(self):
        return self.__cansado
    
    @cansado.setter
    def cansado(self,cansado):
        self.__cansado = cansado