class RepositorioBanco:
    def salver(self,dados):
        print(f"Salvando {dados} no banco")

class Sistema:
    def __init__(self,repositorio):
        self.repositorio = repositorio
    
    def salvar_dados(self,dados):
        self.repositorio.salvar(dados)