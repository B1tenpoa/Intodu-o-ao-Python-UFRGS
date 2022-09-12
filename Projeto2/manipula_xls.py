# Módulo manipula_xls
# Descrição: Este módulo oferece funções para manipular arquivos no
# formato xls.
# Autor: Anderson Bitencourt
# Versão: 0.0.1
# Data: 07/09/2022

# para criar os arquivos no terminal powershell windows
# type > __main__.py

# type > manipula_xls.py

# pip install openpyxl -> para instalar o openpyxl

# importação de pacotes
from openpyxl import Workbook


def cria_xls(nome_arquivo: str) -> Workbook:
    """Esta função cria uma pasta de trabalho MS-Excel."""
    pasta = Workbook()
    return pasta

def cria_planilha(nome_planilha: str, pasta: Workbook) -> None:
    pasta.active
    pasta.create_sheet(nome_planilha)
