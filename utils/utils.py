import csv
from configurations.configurations import Configurations
from datetime import date

class Utils():
    def __init__(self):
        self.__configurations = Configurations()

    def read_file_csv(self):
        transactions = []
        with open(self.__configurations.file_output, mode='r', newline='') as file:
            reader = csv.DictReader(file, delimiter=';')
            for row in reader:
                transactions.append(row)
        return transactions
    
    def write_file_csv(self, id, codigo, descricao, quantidade):
        with open(self.__configurations.file_output, mode='a', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow([id, codigo, descricao, quantidade])

    def update_transaction(self, id, new_codigo, new_descricao, new_quantidade):
        transactions = self.read_file_csv()
        found = False
        for transaction in transactions:
            if transaction['id'] == str(id):
                transaction['codigo'] = new_codigo
                transaction['descricao'] = new_descricao
                transaction['quantidade'] = new_quantidade
                found = True
                break
        
        if not found:
            print("ID inválido. Não foi possível encontrar a transação com o ID fornecido.")
            return

        with open(self.__configurations.file_output, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'codigo', 'descricao', 'quantidade'], delimiter=';')
            writer.writeheader()
            for transaction in transactions:
                writer.writerow(transaction)


