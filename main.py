from pages.menu import Menu
from models.transaction import Transaction

if __name__ == '__main__':
    menu = Menu()
    transaction = Transaction()
    transaction.show_critical()
    
    while True:
        menu.show_menu()
        operation = menu.get_operation()
        menu.limpar_terminal()

        if operation == 8:
            print('Saindo do sistema ...')
            break

        elif operation == 1: # ver o estoque
            transaction.view()

        elif operation == 2: # log de Movimentação
            transaction.show_log()
   
        elif operation == 3: # alterar valor
            id = int(input('Digite o id: '))
            codigo = input('Digite o codigo: ')
            descricao = input('Digite a descricao: ')
            quantidade = int(input('Digite o quantidade: '))
            minimo = int(input('Digite o minimo: '))

            transaction.update(id, codigo, descricao, quantidade, minimo)

        elif operation == 4: # adicionar produto
            id = int(input('Digite o id: '))
            codigo = input('Digite o codigo: ')
            descricao = input('Digite a descricao: ')
            quantidade = int(input('Digite o quantidade: '))
            minimo = int(input('Digite o minimo: '))

            transaction.add(id, codigo, descricao, quantidade, minimo)
             
        elif operation == 5: #remover produto
            id = int(input('Digite o id: '))

            transaction.remove(id)
        
        elif operation == 6: #adicionar quantidade
            id = int(input('Digite o id: '))
            quantidade = int(input('Digite a quantidade: '))

            transaction.adicionar_quantidade(id, quantidade)
        
        elif operation == 7: #retirar quantidade
            id = int(input('Digite o id: '))
            quantidade = int(input('Digite a quantidade: '))

            transaction.remove_quantidade(id, quantidade)

        print(f'operacao escolhida ${operation}')
            

