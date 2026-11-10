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

                # Separa o nome da roupa do preço usando ';' como divisor
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