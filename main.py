from pages.menu import Menu
from models.transaction import Transaction

if __name__ == '__main__':
    menu = Menu()

    while True:
        
        menu.show_menu()
        operation = menu.get_operation()

        if operation == 6:
            print('Saindo do sistema ...')
            break
        else :
            if operation == 1:
                Transaction().view()
            elif operation == 3:
                id = int(input('Digite o id: '))
                codigo = input('Digite o codigo: ')
                descricao = input('Digite a descricao: ')
                quantidade = int(input('Digite o quantidade: '))

                transaction = Transaction()
                transaction.update(id, codigo, descricao, quantidade)
            elif operation == 4:
                id = int(input('Digite o id: '))
                codigo = input('Digite o codigo: ')
                descricao = input('Digite a descricao: ')
                quantidade = int(input('Digite o quantidade: '))

                transaction = Transaction()
                transaction.add(id, codigo, descricao, quantidade)  
            print(f'operacao escolhida ${operation}')
            

