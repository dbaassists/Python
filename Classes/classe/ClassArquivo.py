import pandas as pd

class Arquivo_DataFrame:
    def __init__(self
                    , arquivo
                    , separador
                    , encoding
                    , header
                    , numeroColunas
                    , nomeColunas
                    , parametro
                    , sheet_name
                    , index):
        
        self.arquivo = arquivo
        self.sep = separador
        self.encoding = encoding
        self.header = header
        self.numeroColunas = numeroColunas
        self.nomeColunas = nomeColunas        
        self.parametro = parametro 
        self.sheet_name = sheet_name
        self.index = index

    def carregaArquivoCSV(self):

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
    
    
    def carregaArquivoEXCEL(self):

        if (self.parametro == 0):
            
            df = pd.read_excel(self.arquivo
                    , sheet_name=self.sheet_name
                    , encoding= self.encoding
                    , header=self.header
                    , names=self.nomeColunas
                    , usecols=self.numeroColunas)
            
        elif (self.parametro == 1):

            df = pd.read_excel(self.arquivo
                    , sheet_name=self.sheet_name
                    , encoding= self.encoding
                    , header=self.header
                    , usecols=self.numeroColunas)

        elif (self.parametro == 2):

            df = pd.read_excel(self.arquivo
                    , sheet_name=self.sheet_name
                    , encoding= self.encoding
                    , header=self.header
                    , usecols=self.nomeColunas)
                
        if (self.parametro == 3):
            
            df = pd.read_excel(self.arquivo
                    , sheet_name=self.sheet_name
                    , encoding= self.encoding
                    , header=self.header)

        return df        
