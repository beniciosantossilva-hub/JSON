import json

ARQUIVO_CADASTROS = "cadastros.json"

def exibir_menu():
    print("\n=========== MENU CADASTRO ===========")
    print("1. Cadastrar pessoa")
    print("2. Ver cadastros")
    print("3. Apagar cadastro")
    print("4. Sair")
    print("======================================")

def salvar_cadastros(cadastros):
    with open(ARQUIVO_CADASTROS, "w", encoding="utf-8") as arquivo:
        json.dump(cadastros, arquivo, indent=4, ensure_ascii=False)

def carregar_cadastros():
    try:
        with open(ARQUIVO_CADASTROS, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def cadastrar_pessoa(cadastros):
    nome = input("Nome: ")
    idade = input("Idade: ")
    turma = input("Turma: ")
    curso = input("Curso: ")

    cadastros.append({
        "Nome": nome,
        "Idade": idade,
        "Turma": turma,
        "Curso": curso
    })

    salvar_cadastros(cadastros)
    print("Cadastro realizado com sucesso!")

def ver_cadastros(cadastros):
    if not cadastros:
        print("\nNenhum cadastro realizado.")
    else:
        print("\n===== LISTA DE CADASTROS =====")
        for i, pessoa in enumerate(cadastros, 1):
            print(f"{i}. Nome: {pessoa['Nome']}, Idade: {pessoa['Idade']}, Turma: {pessoa['Turma']}, Curso: {pessoa['Curso']}")
    input("\nPressione Enter para voltar ao menu...")

def apagar_cadastro(cadastros):
    if not cadastros:
        print("\nNenhum cadastro para apagar.")
        return
    
    print("\n===== APAGAR CADASTRO =====")
    for i, pessoa in enumerate(cadastros, 1):
        print(f"{i}. Nome: {pessoa['Nome']}, Idade: {pessoa['Idade']}, Turma: {pessoa['Turma']}, Curso: {pessoa['Curso']}")
    
    try:
        indice = int(input("\nDigite o número do cadastro que deseja apagar: "))
        if 1 <= indice <= len(cadastros):
            removido = cadastros.pop(indice - 1)
            salvar_cadastros(cadastros)
            print(f"Cadastro de {removido['Nome']} apagado com sucesso!")
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida. Digite apenas números.")


# Programa principal
def main():
    cadastros = carregar_cadastros()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_pessoa(cadastros)
        elif opcao == "2":
            ver_cadastros(cadastros)
        elif opcao == "3":
            apagar_cadastro(cadastros)
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
