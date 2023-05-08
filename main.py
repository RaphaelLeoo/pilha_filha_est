from calculadora.functions import *
from calculadora.menu import *
import os

def main():
    fila = []
    flag = True
    option = 0

    while flag:
        layout_menu()
        option = menu_incial()
        clear_screen()

        if option == 0:
            flag = False
            break
        if option == 1:
            layout_menu()
            option_sub = menu_operacoes_sub()

            if option_sub == 1:
                clear_screen()
                layout_menu()
                option = menu_operacoes()
                values = capture_values()
                fila.append((option,values))
            if option_sub == 2:
                if not fila:
                    file_vazia()
                else:
                    show_info_function(fila[0][0],fila[0][1])
                    print("Resultado Operação: ",function_pricipal(fila[0][0],fila[0][1]))
                    fila.remove(fila[0])
            if option_sub == 3:
                if not fila:
                    file_vazia()
                else:
                    clear_screen()
                    for item in fila:
                        show_info_function(item[0],item[1])
                        print("Resultado Operação:",function_pricipal(item[0],item[1]))
                        print("\n")
                    layout_menu()
                    fila =[]
        if option == 2:
            expression = str(input("Digite a expressão: "))
            clear_screen()
            if not validate_math(expression):
                layout_menu()
                print("\n")
                print("Expressão Matemática VALIDA")
                print("\n")
                layout_menu()
            else:
                layout_menu()
                print("\n")
                print("Expressão Matemática INVALIDA")
                print("\n")
                layout_menu()
        
        
if __name__ == '__main__':
    main()
