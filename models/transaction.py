from utils.utils import Utils

class Transaction():
    def __init__(self, id=None, codigo=None, descricao=None, quantidade=None, utils=None):
        self.__id = id
        self.__codigo = codigo
        self.__descricao = descricao
        self.__quantidade = quantidade
        self.__utils = utils if utils else Utils()
    
    def save(self):
        self.__utils.write_file_csv(self.__id, self.__codigo, self.__descricao, self.__quantidade)
    
    def view(self):
        transactions = self.__utils.read_file_csv()
        for ind, row in transactions.iterrows():
            print(f'id: {row[0]}, codigo: {row[1]}, descricao: {row[2]}, quantidade: {row[3]}')
        
    def update(self, id, new_codigo, new_descricao, new_quantidade):
        self.__utils.update_transaction(id, new_codigo, new_descricao, new_quantidade)

    def add(self, id, add_codigo, add_descricao, add_quantidade):
        self.__utils.add_transaction(id, add_codigo, add_descricao, add_quantidade)
    
    def remove(self, id):
        self.__utils.remove_transaction(id)