import pdfplumber
from openpyxl import Workbook
from openpyxl.styles import Font

def open_pdf(file):
    with pdfplumber.open(file) as pdf:
        page = pdf.pages[3]
        table = page.extract_table()
        organize_list(table)
        return table  # just for pytest


def organize_list(data):
    for i in range(len(data)):
        data[i].pop(0)
        data[i].remove('')
    py_excel(data)

def py_excel(d):
    wb = Workbook()

    # Criando page no excel
    wb.create_sheet('fatura_nubank')
    fatura_page = wb['fatura_nubank']

    # Header da planilha
    fatura_page.append(['Nome', 'Valor'])

    # Adicionando os elementos Nome, Valor
    for i in range(len(d)):
        fatura_page.append([*d[i]])

    # Salvando o arquivo .xlsx
    wb.save('Arquivo_novo_fatura.xlsx')

def main():
    user = "fatura_test.pdf"
    open_pdf(user)

if __name__ == "__main__":
    main()


