import pandas as pd
from datetime import date
from configurations.configurations import Configurations

class Utils():
    def __init__(self):
        self.__configurations = Configurations()


    def read_file_csv(self):
        self.transactions = pd.read_csv(self.__configurations.file_output)
        self.transactions = self.transactions.sort_values('id')
        return self.transactions
    

    def write_file_csv(self, id, codigo, descricao, quantidade):
        columns = ['id', 'codigo', 'descricao', 'quantidade']
        transactions = pd.DataFrame(columns=columns)

        transactions.to_csv(self.__configurations.file_output, index=False)


    def update_transaction(self, id, codigo, descricao, quantidade):
        transactions = self.read_file_csv()

        data = {'id': [id],
                'codigo': [codigo],
                'descricao': [descricao],
                'quantidade': [quantidade]
                }

        new_line = pd.DataFrame(data)

        if int(id) not in transactions['id'].values:
            print("ID inválido. Não foi possível encontrar a transação com o ID fornecido.")

        else:
            transactions.loc[transactions['id'] == id, 'codigo'] = codigo
            transactions.loc[transactions['id'] == id, 'descricao'] = descricao
            transactions.loc[transactions['id'] == id, 'quantidade'] = quantidade

            transactions.to_csv(self.__configurations.file_output, index=False)
        

    def add_transaction(self, id, codigo, descricao, quantidade):
        transactions = self.read_file_csv()

        data = {'id': [id],
        'codigo': [codigo],
        'descricao': [descricao],
        'quantidade': [quantidade]}
    
        new_line = pd.DataFrame(data)
        
        transactions = pd.concat([transactions, new_line], ignore_index=True)

        transactions.to_csv(self.__configurations.file_output, index=False)


    def remove_transaction(self, id, quantidade):
        transactions = self.read_file_csv()
        
        if id not in transactions['id'].values:
            print("ID inválido. Não foi possível encontrar a transação com o ID fornecido.")

        else:
            transactions.loc[transactions['id'] == id, 'quantidade'] -= quantidade

            transactions.to_csv(self.__configurations.file_output, index=False)

    def show_critical_positions(self):
        transactions = self.read_file_csv()
        critical = transactions[transactions['quantidade'] <= 7]

        print(critical)



