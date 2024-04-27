class Configurations():
    def __init__(self):
        self.__file_output = './file/estoque.csv'
        self.__log_output = './file/logEstoque.csv'


    @property
    def file_output(self):
        return self.__file_output
    

    @property
    def log_output(self):
        return self.__log_output
