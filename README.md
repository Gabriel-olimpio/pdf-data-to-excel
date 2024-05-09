# Credit Card Monthly Expenses Automation
This project automates the process of extracting credit card monthly expenses from a PDF document and populating them into an Excel file.

**Features**

 - Extracts expense details (e.g., merchant name, amount) from a credit card statement PDF.
 - Organizes extracted data into a structured format.
 - Populates the data into a new or existing Excel file.

# Requirements
- Python 3 (tested with version X.X - replace with your tested version) How to install Python.

**Libraries:**

- **pdfplumber** (PDF parsing) 

- **openpyxl** (Excel file manipulation) 

- **os** (file manipulation) - python's standard libray

- **pathlib** (getting file's path) - python's standard libray

# Usage
    Bash
    1. Install required libraries:

    # Open a terminal or command prompt and run the following commands:

    pip install pdfplumber
    pip install openpyxl

    # or just run:
    pip install -r requirements.txt

**Modify the script:**


The script will automatically get the `.pdf` file in the downloads folder of your computer.

```python
# Get downloads path
def get_directory():
    path = Path()
    download_path = str(path.home() / 'Downloads')
    return download_path + '/'
``` 


Change file's name `if 'file_name' in f`

```python
def get_file(directory):
    files = os.listdir(directory)
    for f in files:
        try:
            if 'Nubank_' in f:  # Search file's name
                return f
        except FileNotFoundError:
            print(FileNotFoundError)
```


Insert page number where the data is `pdf.pages[insert_page_number]`
```python
# The data is located at the end of pdf (page 4 -> index 3)
def open_pdf(file):
    with pdfplumber.open(file) as pdf:
        page = pdf.pages[3]  # data location
        table = page.extract_table()
        organize_list(table)
        return table  # just for pytest
```

You can choose if you want to create a new sheet or insert the data in other sheet that already exist.
```python
def py_excel(d):
    # loading file
    book = load_workbook('Planilha modif nova.xlsx')  # worksheet wanted

    # creating page
    book.create_sheet('Nubank Fatura')  # create sheet page or
    fatura_page = book['Nubank Fatura']  # access sheet page
```

The file will be saved

```python
 # save modifications
    book.save('Planilha modif nova.xlsx')
```

Open a terminal or command prompt, navigate to the directory containing the script, and run:
    
    Bash
    python3 project.py