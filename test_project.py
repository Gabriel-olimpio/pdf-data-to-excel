from project import open_pdf, get_file, get_directory
import pytest

def main():
    test_pdf()
    test_get_file()
    test_get_directory()

def test_pdf():
    with pytest.raises(FileNotFoundError):
        open_pdf('fatura.pdf')
        open_pdf('fatura_nubank.pdf')
        open_pdf('faturado.pdf')
        open_pdf('faturado.docx')
        open_pdf('faturado.xlsx')

def test_get_file():
    assert get_file('/Users/gabriel.andre/Downloads') == 'fatura_test.pdf'
    with pytest.raises(FileNotFoundError):
        get_file('/Users/gabriel.andre/Imagens')
        get_file('/Users/gabriel.andre/BICT')


def test_get_directory():
    assert get_directory() == '/Users/gabriel.andre/Downloads'


if __name__ == "__main__":
    main()