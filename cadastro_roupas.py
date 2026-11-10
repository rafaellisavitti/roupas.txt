# === SISTEMA DE GERENCIAMENTO DE ROUPAS ===

def salvar_roupa(nome, preco):
    """Salva a peça de roupa e seu preço no arquivo roupas.txt."""
    with open("roupas.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{nome};{preco}\n")
    print(f"\n✅ Roupa '{nome}' cadastrada com sucesso!\n")


def exibir_roupa_mais_cara():
    """Lê o arquivo e exibe a roupa com o maior preço."""
    maior_preco = None
    roupa_mais_cara = ""

    try:
        with open("roupas.txt", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                if not linha:
                    continue

                # Separa o nome da roupa do preço usando o ';' como divisor
                nome, prc = linha.rsplit(";", 1)
                preco = float(prc)

                if maior_preco is None or preco > maior_preco:
                    maior_preco = preco
                    roupa_mais_cara = nome

        if roupa_mais_cara:
            print(f"\n🏆 ROUPA MAIS CARA: {roupa_mais_cara} com R$ {maior_preco:.2f}!\n")
        else:
            print("\n⚠️ Nenhuma roupa encontrada no arquivo.\n")

    except FileNotFoundError:
        print("\n⚠️ O arquivo 'roupas.txt' ainda não existe. Cadastre uma roupa primeiro!\n")


def listar_roupas():
    """Lê e exibe todas as roupas cadastradas."""
    try:
        with open("roupas.txt", "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()
            if not linhas:
                print("\n⚠️ Nenhuma roupa cadastrada no momento.\n")
                return

            print("\n--- LISTA DE ROUPAS ---")
            for i, linha in enumerate(linhas, 1):
                linha = linha.strip()
                if linha:
                    nome, preco = linha.rsplit(";", 1)
                    print(f"{i}. {nome} - R$ {float(preco):.2f}")
            print("----------------------\n")
    except FileNotFoundError:
        print("\n⚠️ O arquivo 'roupas.txt' ainda não existe. Cadastre uma roupa primeiro!\n")


def menu():
    """Menu interativo do terminal."""
    while True:
        print("=== SISTEMA DE CATÁLOGO DE ROUPAS ===")
        print("1 - Cadastrar Nova Roupa")
        print("2 - Exibir Roupa Mais Cara")
        print("3 - Listar Todas as Roupas")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome/modelo da roupa: ")
            try:
                preco = float(input("Digite o preço (R$): "))
                salvar_roupa(nome, preco)
            except ValueError:
                print("\n❌ Preço inválido! Digite apenas números.\n")
        elif opcao == "2":
            exibir_roupa_mais_cara()
        elif opcao == "3":
            listar_roupas()
        elif opcao == "4":
            print("\nSaindo do sistema...")
            break
        else:
            print("\n❌ Opção inválida! Tente novamente.\n")

if __name__ == "__main__":
    menu()