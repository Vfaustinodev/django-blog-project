class Calculadora:

    def __init__(self):
        self.calc_value()

    def calc_value(self):
        

        while True: 
            first = int(input('\nDIGITE O PRIMEIRO NÚMERO: '))
            operator = str(input('\nDIGITE O OPERADOR PARA FAZER O CÁLCULO: '))
            second = int(input('\nDIGITE O SEGUNDO NÚMERO: '))

            match operator:

                case '+':
                    somar = first + second
                    print('\nRESULTADO: ', somar)
                case '*':
                    mult = first * second
                    print('\nRESULTADO: ', mult)
                case '/':
                    divi = first / second
                    print('\nRESULTADO: ', divi)
                case '-':
                    subtra = first - second
                    print('\nRESULTADO: ', subtra)
                    
            chosen = str(input('\nDESEJA SAIR DA APLICAÇÃO? S/N: ')).lower()

            if chosen[0] == 's':
                break
            elif chosen[0] == 'n':
                continue
            else:
                '\nDIGITE APENAS SIM OU NÃO!'
            
Calculadora()

    


        

        


