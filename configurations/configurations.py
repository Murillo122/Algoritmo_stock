
class Configurations():
    def __init__(self):
        self.__file_output = './file/estoque.csv'
        self.__file_output_txt = './file/logEstoque.csv'

    @property
    def file_output(self):
        return self.__file_output
    @property
    def file_output_txt(self):
        return self.__file_output_txt
