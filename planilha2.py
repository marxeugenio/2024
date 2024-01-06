import pandas as pd

def criar_planilha_csv():
    # Dados a serem adicionados na planilha
    dados = {
        'Nome': ['Maria', 'João', 'Ana'],
        'Idade': [30, 25, 28],
        'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte']
    }

    # Criar um DataFrame do pandas com os dados
    df = pd.DataFrame(dados)

    # Salvar o DataFrame como um arquivo CSV
    df.to_csv('exemplo_planilha.csv', index=False)

criar_planilha_csv()
