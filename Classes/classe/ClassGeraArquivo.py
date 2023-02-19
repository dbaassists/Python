import pandas as pd
import json
import pyodbc

class GeraArquivo:
    
    def __init__(self
                    , arquivo
                    , separador
                    , encoding
                    , header
                    , index
                    , sheet_name
                    , arquivoConfig
                    , schemaDB
                    , tabelaDB
                    , diretorioDestinoArquivo
                    , nomeArquivoGerado
                    , data):
        
        self.arquivo = arquivo
        self.sep = separador
        self.encoding = encoding
        self.header = header
        self.index = index
        self.sheet_name = sheet_name
        self.arquivoConfig = arquivoConfig
        self.schemaDB = schemaDB
        self.tabelaDB = tabelaDB
        self.diretorioDestinoArquivo = diretorioDestinoArquivo
        self.nomeArquivoGerado = nomeArquivoGerado
        self.df = pd.DataFrame(data)
    
    # Documentação: https://datagy.io/pandas-dataframe-to-csv/
    def geraArquivoCSV(self):
        self.df.to_csv(self.arquivo
                     , sep = self.sep
                     , index=self.index
                     , encoding=self.encoding)
        
    # Documentação: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_excel.html    
    def geraArquivoEXCEL(self):
        self.df.to_excel(self.arquivo
                     , index=self.index
                     , sheet_name = self.sheet_name
                     , encoding=self.encoding) 
        
    def exportaDadosSQLServer(self):
        
        paramJson 	= "../Config/{0}.json".format(self.arquivoConfig)
        file 		= open(paramJson)
        dfJson 		= json.load(file)

        for tag in dfJson:
            server 		= dfJson[tag]['server']
            database 	= dfJson[tag]['database']
            username 	= dfJson[tag]['username']
            password 	= dfJson[tag]['password']
            
            
        cnxn 	= pyodbc.connect('DRIVER={SQL Server};SERVER='+server+\
                              ';DATABASE='+database+\
                              ';UID='+username+\
                              ';PWD='+ password)

        cursor 	= cnxn.cursor()
        
        query = "SELECT * FROM {0}.{1};".format(self.schemaDB, self.tabelaDB)
        df = pd.read_sql(query, cnxn)
        
        df.to_csv('../{0}/{1}.csv'.format(self.diretorioDestinoArquivo, self.nomeArquivoGerado)
                  , sep=self.sep
                  , index=self.index
                  , encoding=self.encoding)