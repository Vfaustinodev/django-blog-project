from random import choice
from string import digits, ascii_uppercase

def sortear_num_letters(valor):

    gen_cod = ''
    for num_letters in range(valor):
        gen_cod += choice(digits) + choice(ascii_uppercase)
    
    return gen_cod

def gen_list():
    list_create = []
    quant = int(input("\n\nQUANTOS SORTEIOS? "))

    while quant > 0:
        if len(list_create) >= 0:
            list_create.append(sortear_num_letters(3))
            quant -= 1
    
    return print(list_create)

gen_list()

        

        


