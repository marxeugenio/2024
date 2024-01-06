from openpyxl import Workbook

def criar_planilha():
    # Criar um novo arquivo de planilha
    planilha = Workbook()

    # Criar uma aba na planilha
    aba = planilha.active
    aba.title = "Exemplo"

    # Adicionar dados a algumas células
    aba['A1'] = "Nome"
    aba['B1'] = "Idade"
    aba['A2'] = "Maria"
    aba['B2'] = 30
    aba['A3'] = "João"
    aba['B3'] = 25

    # Salvar a planilha
    planilha.save("exemplo_planilha.xlsx")

criar_planilha()
