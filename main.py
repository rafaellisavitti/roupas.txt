import pandas as pd
import os

ARQUIVO_CSV = "roupas.csv"

def garantir_base_dados():
    """Garante que o arquivo roupas.csv exista antes de executar operações."""
    if not os.path.exists(ARQUIVO_CSV):
        df_inicial = pd.DataFrame(columns=["Nome", "Preco"])
        df_inicial.to_csv(ARQUIVO_CSV, index=False, sep=";")

def cadastrar_roupa(nome, preco):
    """Adiciona uma nova roupa à base de dados usando Pandas."""
    garantir_base_dados()
    df = pd.read_csv(ARQUIVO_CSV, sep=";")
    nova_linha = pd.DataFrame([{"Nome": nome, "Preco": float(preco)}])
    df = pd.concat([df, nova_linha], ignore_index=True)
    df.to_csv(ARQUIVO_CSV, index=False, sep=";")
    print(f"\n✅ Roupa '{nome}' cadastrada com sucesso!\n")

def listar_roupas():
    """Lê e exibe todas as roupas cadastradas no terminal."""
    garantir_base_dados()
    df = pd.read_csv(ARQUIVO_CSV, sep=";")
    if df.empty:
        print("\n⚠️ Nenhuma roupa cadastrada na base de dados.\n")
        return
    print("\n--- CATÁLOGO DE ROUPAS (PANDAS) ---")
    print(df.to_string(index=True))
    print("------------------------------------\n")

def exibir_roupa_mais_cara():
    """Encontra a roupa com maior preço usando idxmax() do Pandas."""
    garantir_base_dados()
    df = pd.read_csv(ARQUIVO_CSV, sep=";")
    if df.empty:
        print("\n⚠️ A base de dados está vazia.\n")
        return
    idx_max = df["Preco"].idxmax()
    roupa_mais_cara = df.loc[idx_max]
    print("\n🏆 ROUPA MAIS CARA DO CATÁLOGO:")
    print(f"Nome:  {roupa_mais_cara['Nome']}")
    print(f"Preço: R$ {roupa_mais_cara['Preco']:.2f}\n")

def menu():
    """Interface do menu interativo no terminal."""
    while True:
        print("=== SISTEMA DE CATÁLOGO DE ROUPAS (PANDAS) ===")
        print("1 - Cadastrar Nova Roupa")
        print("2 - Exibir Roupa Mais Cara")
        print("3 - Listar Todas as Roupas")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome/modelo da roupa: ")
            try:
                preco = float(input("Digite o preço (R$): "))
                cadastrar_roupa(nome, preco)
            except ValueError:
                print("\n❌ Valor inválido! Digite apenas números para o preço.\n")
        elif opcao == "2":
            exibir_roupa_mais_cara()
        elif opcao == "3":
            listar_roupas()
        elif opcao == "4":
            print("\nEncerrando o programa... Até logo!")
            break
        else:
            print("\n❌ Opção inválida! Tente novamente.\n")

if __name__ == "__main__":
    menu()