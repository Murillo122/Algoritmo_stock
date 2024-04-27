from pages.menu import Menu
from utils.utils import Utils
from models.transaction import Transaction


if __name__ == '__main__':
    utils = Utils()
    menu = Menu()
    transaction = Transaction()
    
    #utils.write_log_csv()   
    
    while True:
        print('Itens com estoque crítico:')
        utils.show_critical_positions()

        menu.show_menu()
        operation = menu.get_operation()
        menu.limpar_terminal()

        if operation == 6:
            print('Saindo do sistema ...')
            break

        elif operation == 1:
            Transaction().view()

        elif operation == 2:
            log = utils.read_log_csv()
            print(log)
            
        elif operation == 3:
            id = int(input('Digite o id: '))
            codigo = input('Digite o codigo: ')
            descricao = input('Digite a descricao: ')
            quantidade = int(input('Digite o quantidade: '))

            transaction.update(id, codigo, descricao, quantidade)

        elif operation == 4:
            id = int(input('Digite o id: '))
            codigo = input('Digite o codigo: ')
            descricao = input('Digite a descricao: ')
            quantidade = int(input('Digite o quantidade: '))

            transaction.add(id, codigo, descricao, quantidade)
             
        elif operation == 5:
            id = int(input('Digite o id: '))
            #quantidade = int(input('Digite a quantidade a ser removida: '))

            transaction.remove(id)  

        print(f'operacao escolhida ${operation}')
            

