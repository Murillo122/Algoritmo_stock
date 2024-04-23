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
        for transaction in self.__utils.read_file_csv():
            print(f"id: {transaction['id']}, codigo: {transaction['codigo']}, descricao: {transaction['descricao']}, quantidade: {transaction['quantidade']}")

    def update(self, id, new_codigo, new_descricao, new_quantidade):
        self.__utils.update_transaction(id, new_codigo, new_descricao, new_quantidade)
