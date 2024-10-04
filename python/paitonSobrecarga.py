class Produto:
    def __init__(self, nome: str, custo: float):
        self.nome = nome
        self.custo = custo

    def __add__(self,other):
        return self.custo + other.custo


pizza = Produto('Pizza', 49)
refri = Produto('Refri', 8)
print(pizza + refri)  # 57


