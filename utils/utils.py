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
    

    def read_log_csv(self):
        self.logs = pd.read_csv(self.__configurations.log_output)
        return self.logs
    

    def write_file_csv(self):
        columns = ['id', 'codigo', 'descricao', 'quantidade', 'minimo']
        transactions = pd.DataFrame(columns=columns)

        transactions.to_csv(self.__configurations.file_output, index=False)


    def write_log_csv(self):
        columns = ['Data', 'Ação', 'Item Alterado']
        logs = pd.DataFrame(columns=columns)

        logs.to_csv(self.__configurations.log_output, index=False)


    def update_transaction(self, id, codigo, descricao, quantidade, minimo):
        transactions = self.read_file_csv()
        logs = self.read_log_csv()

        data = {
            'id': [id],
            'codigo': [codigo],
            'descricao': [descricao],
            'quantidade': [quantidade],
            'minimo': [minimo]
        }

        new_line = pd.DataFrame(data)

        if int(id) not in transactions['id'].values:
            print("ID inválido. Não foi possível encontrar a transação com o ID fornecido.")

        else:
            transactions.loc[transactions['id'] == id, 'codigo'] = codigo
            transactions.loc[transactions['id'] == id, 'descricao'] = descricao
            transactions.loc[transactions['id'] == id, 'quantidade'] = quantidade
            transactions.loc[transactions['id'] == id, 'minimo'] = quantidade

            transactions.to_csv(self.__configurations.file_output, index=False)

            # Gerando o log da ação
            logs_data = {'Data': [date.today()], 
                         'Ação': ['Atualização dos dados'],
                         'Item Alterado': [id]}
            
            new_line_logs = pd.DataFrame(logs_data)
            logs = pd.concat([logs, new_line_logs], ignore_index=True)
            logs.to_csv(self.__configurations.log_output, index=False)

    def add_transaction(self, id, codigo, descricao, quantidade, minimo):
        transactions = self.read_file_csv()
        logs = self.read_log_csv()

        data = {
            'id': [id],
            'codigo': [codigo],
            'descricao': [descricao],
            'quantidade': [quantidade],
            'minimo': [minimo]
        }
    
        new_line = pd.DataFrame(data)
        
        transactions = pd.concat([transactions, new_line], ignore_index=True)

        transactions.to_csv(self.__configurations.file_output, index=False)
        
        logs_data = {
            'Data': [date.today()], 
            'Ação': ['Adição de um novo item'],
            'Item Alterado': [id]
        }
            
        new_line_logs = pd.DataFrame(logs_data)
        logs = pd.concat([logs, new_line_logs], ignore_index=True)
        logs.to_csv(self.__configurations.log_output, index=False)

    def remove_transaction(self, id):
        logs = self.read_log_csv()
        transactions = self.read_file_csv()
        
        if id not in transactions['id'].values:
            print("ID inválido. Não foi possível encontrar a transação com o ID fornecido.")

        else:
            ind = transactions[transactions['id'] == id].index
            transactions = transactions.drop(index=ind)
            transactions.to_csv(self.__configurations.file_output, index=False)

            logs_data = {'Data': [date.today()], 
                         'Ação': ['Remoção de item inteiro'],
                         'Item Alterado': [id]}
            
            new_line_logs = pd.DataFrame(logs_data)
            logs = pd.concat([logs, new_line_logs], ignore_index=True)
            logs.to_csv(self.__configurations.log_output, index=False)

    def show_critical_positions(self):
        transactions = self.read_file_csv()
        critical = transactions[transactions['quantidade'] <= transactions['minimo']]

        if critical.empty:
            print("Nenhum item abaixo do estoque mínimo.")
        else:
            print("Itens com estoque crítico:")
            print(critical)

    def add_quantity_by_id(self, id, quantidade_adicional):
        logs = self.read_log_csv()
        transactions = self.read_file_csv()
        
        if id in transactions['id'].values:
            transactions.loc[transactions['id'] == id, 'quantidade'] += quantidade_adicional
            transactions.to_csv(self.__configurations.file_output, index=False)
            print('Valor adicionado com sucesso')
            
            # Converter a quantidade adicional para string
            quantidade_adicional_str = str(quantidade_adicional)
            
            # Adicionar registro ao log
            logs_data = {
                'Data': [date.today()], 
                'Ação': ['subtraindo a quantidade ' + quantidade_adicional_str],
                'Item Alterado': [id]
            }
            
            new_line_logs = pd.DataFrame(logs_data)
            logs = pd.concat([logs, new_line_logs], ignore_index=True)
            logs.to_csv(self.__configurations.log_output, index=False)
        else:
            print(f"ID {id} não encontrado.")


    def subtract_quantity_by_id(self, id, subtrair_quantidade):
        logs = self.read_log_csv()
        transactions = self.read_file_csv()

        if id in transactions['id'].values:
            transactions.loc[transactions['id'] == id, 'quantidade'] -= subtrair_quantidade
            
            if (transactions.loc[transactions['id'] == id, 'quantidade'] < 0).any():
                print("Erro: A quantidade resultante não pode ser menor que zero. Nenhuma alteração foi feita.")
            else:
                print(f"Quantidade subtraída do item com ID {id}.")
                transactions.to_csv(self.__configurations.file_output, index=False)
                
                # Converter a quantidade subtraída para string
                subtrair_quantidade_str = str(subtrair_quantidade)
                
                # Adicionar registro ao log
                logs_data = {
                    'Data': [date.today()], 
                    'Ação': ['subtraindo a quantidade ' + subtrair_quantidade_str],
                    'Item Alterado': [id]
                }
                
                new_line_logs = pd.DataFrame(logs_data)
                logs = pd.concat([logs, new_line_logs], ignore_index=True)
                logs.to_csv(self.__configurations.log_output, index=False)
        else:
            print(f"ID {id} não encontrado.")




