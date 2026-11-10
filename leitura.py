import pandas as pd
import os

ARQUIVO_CSV = "roupas.csv"

def listar_roupas():
    """Lê o arquivo CSV com Pandas e exibe a lista formatada de todas as roupas."""
    if not os.path.exists(ARQUIVO_CSV):
        print("\n⚠️ O arquivo 'roupas.csv' ainda não existe. Cadastre uma roupa primeiro!\n")
        return

    df = pd.read_csv(ARQUIVO_CSV, sep=";")

    if df.empty:
        print("\n⚠️ Nenhuma roupa cadastrada na base de dados.\n")
        return

    print("\n=== CATÁLOGO DE ROUPAS (PANDAS) ===")
    # Exibe o DataFrame formatado sem os índices padrão do Pandas
    print(df.to_string(index=False))
    print("------------------------------------\n")

if __name__ == "__main__":
    # Testa a leitura diretamente ao executar este arquivo
    listar_roupas()