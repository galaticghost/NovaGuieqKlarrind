from parser import parse
from token import tokenizer

def validate(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            conteudo = f.read()

        print(f"Validando o arquivo: {file_name}")
        tokens = tokenizer(conteudo)
        print("Tokens gerados:", tokens)
        
        if parse(tokens):
            print("Resultado: A sintaxe do arquivo é VÁLIDA.")
        else:
            print("Resultado: A sintaxe do arquivo é INVÁLIDA.")
            
    except FileNotFoundError:
        print(f"Erro: Arquivo '{file_name}' não encontrado.")

if __name__ == "__main__":
    validate("texto.sm")
    validate("textoinvalido.sm")