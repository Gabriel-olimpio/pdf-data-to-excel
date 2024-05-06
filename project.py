import pdfplumber
from openpyxl import Workbook
from openpyxl.styles import Font

def open_pdf(file):
    with pdfplumber.open(file) as pdf:
        page = pdf.pages[3]
        table = page.extract_table()
        # dict = {"nome": table[0][2], "valor": table[0][3]}
        return table


def organize_list(data):
    for i in range(len(data)):
        data[i].pop(0)
        data[i].remove('')
    return data

def py_excel(d):
    wb = Workbook()

    # Criando page no excel
    wb.create_sheet('fatura_nubank')
    fatura_page = wb['fatura_nubank']

    # header da planilha
    fatura_page.append(['Nome', 'Valor'])

    # Adicionando os elementos Nome, Valor
    for i in range(len(d)):
        fatura_page.append([*d[i]])

    # Salvando o arquivo .xlsx
    wb.save('Fatura_Nubank.xlsx')

def main():
    user = "fatura_test.pdf"
    txt = open_pdf(user)
    dados = organize_list(txt)
    py_excel(dados)

if __name__ == "__main__":
    main()


