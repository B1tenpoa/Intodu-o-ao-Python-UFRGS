# Módulo __main__
# Descrição: .
# Autor: Anderson Bitencourt
# Versão: 0.0.1
# Data: 07/09/2022

# Importação de pacotes
import random

## Primeiro importo o que vier da biblioteca padrão

## Depois importe o que vier de pacotes de terceiros
from openpyxl import Workbook

## Por fim, importe os pacotes que você desenvolveu
import manipula_xls


def main():
    lista_planilhas = ['receitas', 'despesas', 'resultado']
    pasta = manipula_xls.cria_xls('orcamento.xls')
    pasta.active
    for planilha in lista_planilhas:
        manipula_xls.cria_planilha(planilha, pasta)
    pasta.save("orcamento.xls")

if __name__ == "__main__":
    main()