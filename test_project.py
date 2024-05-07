from project import open_pdf
import pytest

def main():
    test_pdf()

def test_pdf():
    with pytest.raises(FileNotFoundError):
        open_pdf('fatura.pdf')
        open_pdf('fatura_nubank.pdf')
        open_pdf('faturado.pdf')
        open_pdf('faturado.docx')
        open_pdf('faturado.xlsx')


if __name__ == "__main__":
    main()