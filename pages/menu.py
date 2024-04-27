import os

class Menu:
    def __init__(self, operation = None):
        self.__operation = operation
    
    def show_menu(self):
        print('\n\n=== Menu ===')
        print('1. Visualizar o estoque')
        print('2. Visualizar o log de movimentação no estoque')
        print('3. Alterar o valor de um dos produtos no estoque') 
        print('4. Adicionar um produto no estoque')
        print('5. Remover um produto do estoque')
        print('6. Adicionar uma quantidade para um produto no estoque')
        print('7. Remover uma quantidade de um produto no estoque')
        print('8. Sair')

    def get_operation(self):
        self.__operation = int(input('selecione uma operação: '))
        return self.__operation
    
    def limpar_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')