import os

def function_pricipal(operacao:int,list_num:list):

    response = list_num[0]
    list_num = list_num[1:] 

    if operacao == 1:
        return sum(list_num,response)
    if operacao == 2:
        for item in list_num:
            response -= item
    if operacao == 3:        
        for item in list_num:
            response *= item
    if operacao == 4:
        for item in  list_num:
            response = round(float(response/item),4)
    
    return response


def capture_values():
    list_num = []
    options = 0
    while 1:
        list_num.append(int(input("Digite um número: ")))

        print("\n1 - Adicionar mais um número")
        print("0 - Finalizar\n")
        options = int(input("Digite um Valor: "))
        print("\n")

        if options == 0:
            break

    return list_num

def validate_math(expression:str):
    start_pilha = []
    char_especial_open = ['(','{','[']
    char_especial_close = [')','}',']']

    for item in expression:
        if item in char_especial_open:
            start_pilha.append(item)
        elif item in char_especial_close:
            if start_pilha:
                start_pilha.pop()
            else:
                start_pilha.append(item)
                break
    return start_pilha
