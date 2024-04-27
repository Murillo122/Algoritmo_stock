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
        print("ID | Código    | Descrição          | Quantidade | Mínimo")
        print("-" * 55)
        for ind, row in transactions.iterrows():
            print(f"{row['id']:<3}| {row['codigo']:<10}| {row['descricao']:<20}| {row['quantidade']:<11}| {row['minimo']}")

        
    def update(self, id, new_codigo, new_descricao, new_quantidade, new_minimo):
        self.__utils.update_transaction(id, new_codigo, new_descricao, new_quantidade, new_minimo)

    def add(self, id, add_codigo, add_descricao, add_quantidade, new_minimo):
        self.__utils.add_transaction(id, add_codigo, add_descricao, add_quantidade, new_minimo)
    
    def remove(self, id):
        self.__utils.remove_transaction(id)
    
    def show_critical(self):
        self.__utils.show_critical_positions()
    
    def show_log(self):
        log = self.__utils.read_log_csv()
        print("Data       | Ação        | Item Alterado")
        print("-" * 45)
        for ind, row in log.iterrows():
            print(f"{row['Data']:<10}| {row['Ação']:<12}| {row['Item Alterado']}")


    def adicionar_quantidade(self, id, quantidade):
        self.__utils.add_quantity_by_id(id, quantidade)
    
    def remove_quantidade(self, id, quantidade):
        self.__utils.subtract_quantity_by_id(id, quantidade)

