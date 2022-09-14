# Importando o pacote requests

import requests

def page_reader(endereco: str) -> requests.models.Response:
    tce = requests.get(endereco)
    return tce

def grava_balancete_csv(resposta: requests.models.Response) -> None:
    arquivo = open('balancete.csv', 'wb')
    for texto in resposta.iter_content():
        arquivo.write(texto)
    arquivo.close()

    
def main():
    endereco = 'http://dados.tce.rs.gov.br/dados/municipal/balancete-despesa/2022.csv'
    balancete = page_reader(endereco)
    grava_balancete_csv(balancete)
    print(f"O balancete de despesas do TCE foram baixados com sucesso no arquivo 'balancete.csv'.")
    print(f"Obrigado Prof. Nelson pelos ensinamentos neste curso de Python.")
    
if __name__ == "__main__":
    main()