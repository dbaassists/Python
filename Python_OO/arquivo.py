import pandas as pd

class DataFrame:
    def __init__(self
                    , arquivo
                    , separador
                    , encoding
                    , header
                    , numeroColunas
                    , nomeColunas
                    , parametro):
        self.arquivo = arquivo
        self.sep = separador
        self.encoding = encoding
        self.header = header
        self.numeroColunas = numeroColunas
        self.nomeColunas = nomeColunas        
        self.parametro = parametro
    pass

    def carregaArquivo(self):

        if (self.parametro == 0):
        
            df = pd.read_csv(self.arquivo
                            , sep = self.sep
                            , encoding= self.encoding
                            , header=self.header
                            , names=self.nomeColunas
                            , usecols=self.numeroColunas )

        elif (self.parametro == 1):
        
            df = pd.read_csv(self.arquivo
                            , sep = self.sep
                            , encoding= self.encoding
                            , header=self.header
                            , usecols=self.numeroColunas )                            

        elif (self.parametro == 2):
        
            df = pd.read_csv(self.arquivo
                            , sep = self.sep
                            , encoding= self.encoding
                            , header=self.header
                            , names=self.nomeColunas )
                
        if (self.parametro == 3):
        
            df = pd.read_csv(self.arquivo
                            , sep = self.sep
                            , encoding= self.encoding
                            , header=self.header)


        return df
