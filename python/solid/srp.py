class RelatorioVendas():
    def __init__(self,vendas):
        self.vendas = vendas
    
    def gerar_relatorio(self):
        return f'Relatório de vendas: {len(self.vendas)} vendas'
    
class CaluladoraImpostos():
    def calcular_impostos(self,vendas):
        return sum(venda['valor'] * 0.1 for venda in vendas)