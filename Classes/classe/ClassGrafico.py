import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class Grafico:
    def __init__(self
                    , baseDados
                    , eixo_x
                    , eixo_y
                    , tituloGrafico
                    , descricaoEixoX
                    , descricaoEixoY
                    , variacao
                    , descritivo
                    , quantidade):
            
        self.baseDados = baseDados
        self.eixo_x = eixo_x
        self.eixo_y = eixo_y
        self.tituloGrafico = tituloGrafico
        self.descricaoEixoX = descricaoEixoX
        self.descricaoEixoY = descricaoEixoY
        self.variacao = variacao
        self.descritivo = descritivo
        self.quantidade = quantidade
    pass
    
    def geraGraficoBarra(self):        
        #criando a fig e o ax no matplotlib
        fig, ax = plt.subplots(figsize=(13,6))

        #criando novamente o gráfico
        sns.barplot(x=self.eixo_x, # colocando as categorias no eixo x
                    y=self.eixo_y, # colocando os valores no eixo y
                    data = self.baseDados, # selecionando a base de dados
                    ax=ax,palette=['red','green','brown','grey','blue']) # definindo o Axes criado

        #modificação do fundo
        ax.set_frame_on(False) # retirando o Frame (retângulo que encobre os gráficos)

        #adicionando um título
        ax.set_title(self.tituloGrafico, # texto do título
                     loc='center', # posicionamento do título no Axes
                     pad=30, # Distanciamento do título com outros objetos
                     fontdict={'fontsize':20}, # Tamanho da fonte utilizado
                     color='#3f3f4e') # cor da fonte em hexadecimal

        #retirando o eixo y
        ax.get_yaxis().set_visible(True) # retirando o eixo Y

        #retirando os ticks do eixo x
        ax.tick_params(axis='x', # escolhendo os ticks do eixo x
                       length=0, # colocamos os ticks de tamanho zero, compare com os desenhos de cima
                       labelsize=12, # tamanho da fonte para os eixos
                       colors='dimgrey') # cor da fonte para o eixo x

        #ajustando o título Frutas do eixo
        ax.set_xlabel(self.descricaoEixoX, # título que queremos colocar na parte horizontal (em baixo)
                      labelpad=10, # distanciamento deste título com outros objetos
                      fontdict={'fontsize':14}, # tamanho da fonte utilizado
                      color='#4c4c4c') # cor da fonte em hexadecimal

        #ajustando o título Frutas do eixo
        ax.set_ylabel(self.descricaoEixoY, # título que queremos colocar na parte horizontal (em baixo)
                      labelpad=10, # distanciamento deste título com outros objetos
                      fontdict={'fontsize':14}, # tamanho da fonte utilizado
                      color='#4c4c4c') # cor da fonte em hexadecimal


        #colocando os rótulos
        for retangulo in ax.patches:
            ax.text(retangulo.get_x() + retangulo.get_width() / 2,
                  retangulo.get_height() + self.variacao,
                  '{:,.2f}'.format(float(retangulo.get_height())).replace(',','.'), # adicionando o texto da altura
                  ha = 'center')

        #plotando o gráfico
        return plt.tight_layout();

    
    
    def geraGraficoPizza(self):
        
        fig, ax = plt.subplots(figsize=(15,5))

        # Data to be represented
        descritivo = self.descritivo
        quantidade = self.quantidade

        # Plotting the pie chart
        plt.title(self.tituloGrafico,
        fontsize = 20)
        plt.pie(quantidade, labels=descritivo, autopct=lambda x: '{:.0f}'.format(x*quantidade.sum()/100))
        plt.axis('equal')
        plt.show()