import pandas as pd

def imprimir_tabela_csv(caminho_arquivo):
    try:
        #Lendo o arquivo CSV
        dados = pd.read_csv(caminho_arquivo)

        #Imprimindo as informações em forma de tabela
        print(dados)
    except FileNotFoundError:
        print("Arquivo não encontrado.")
    except Exception as e:
        print("Ocorreu um erro:", e)

if __name__ == "__main__":
    caminho_arquivo = input(" Digite o caminho completo do arquivo CSV: ")
    imprimir_tabela_csv(caminho_arquivo)
