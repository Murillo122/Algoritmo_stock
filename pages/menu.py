import os

class Menu:
    def __init__(self, operation = None):
        self.__operation = operation
    
    def show_menu(self):
        print('Digite 1 para ver o estoque: ')
        print('Digite 2 para ver o log de Movimentação no estoque')
        print('Digite 3 para alterar um valor de um dos produtos no estoque') 
        print('Digite 4 para adicionar um produto no estoque')
        print('Digite 5 para remover um produto no estoque')
        print('Digite 6 para sair')

    def get_operation(self):
        self.__operation = int(input('selecione uma operação: '))
        return self.__operation
    
    def limpar_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')