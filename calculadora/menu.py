import os

def menu_incial():
    print("\n1 - Operações")
    print("2 - Expressão")
    print("0 - Finalizar Programa\n")
    return int(input("Digite uma Opção: "))

def menu_operacoes():
    
    print("\n1 - Adição (+)")
    print("2 - Subtração (-)")
    print("3 - Multiplicação (*)")
    print("4 - Divisão (/)\n")
    return int(input("Digite uma Opção: "))

def menu_operacoes_sub():
    
    print("\n1 - Adicionar Operação na Fila")
    print("2 - Executar Próxima Operação da Fila")
    print("3 - Executar Todas as Operações da Fila")
    print("0 - Voltar para o menu principal\n")
    return int(input("Digite uma Opção: "))

def file_vazia():
    print("\n")
    print("A fila de operações está vazia !!!")
    print("\n")

def show_info_function(operacao:int,list_num:list):

    layout_menu()
    operacoes = ["Adição","Subtração","Multiplicação","Divisão"]
    print(f"Operação Atual da Fila: {operacoes[operacao-1]}")
    print("Valores da operação:",list_num)

def layout_menu():
    print("***************************")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')