class Single():
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    @property
    def usuario(self):
        return self.__usuario
    
    @usuario.setter
    def usuario(self,usuario):
        self.__usuario = usuario
        
    @property
    def idioma(self):
        return self.__idioma
    
    @idioma.setter
    def idioma(self,idioma):
        self.__idioma = idioma
    
    @property
    def fuso_horario(self):
        return self.__fuso_horario
    
    @fuso_horario.setter
    def fuso_horario(self,fuso_horario):
        self.__fuso_horario = fuso_horario
    
    @property
    def moeda(self):
        return self.__moeda
    
    @moeda.setter
    def moeda(self,moeda):
        self.__moeda = moeda
    
    @property
    def unidade_metrica(self):
        return self.__unidade_metrica
    
    @unidade_metrica.setter
    def unidade_metrica(self,unidade_metrica):
        self.__unidade_metrica = unidade_metrica
    
class Utils:
    
    @staticmethod
    def converter_para_km(single,valor):
        if single.unidade_metrica == "mi":
            return valor
        else:
            km = 1.60934
            return valor * km
        
single = Single()
single.unidade_metrica = "km"
print(Utils.converter_para_km(single,40))