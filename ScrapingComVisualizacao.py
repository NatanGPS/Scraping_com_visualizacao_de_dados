import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


class ScrapingComPygal:
    def __init__(self):

        '''Configurando o requests'''
        url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
        r = requests.get(url)
        print('Codigo: ', r.status_code)
        
        self.nomes, self.plotar_dicts = [], []
       
        # Armazena a resposta da variavel r
        self.response_ = r.json()


    def Iniciar(self):

        print('Total de repositórios: ', self.response_['total_count'])
        self.ExploraInfos()
        self.Criarvisualizacao()
    
    
    def ExploraInfos(self):
        # Explorar informações sobre os repositorios
        self.dicionarioDosRepositorios = self.response_['items']
        for rep in self.dicionarioDosRepositorios:
            self.nomes.append(rep['name'])
            
            self.plotar_dict = {
                'value': rep['stargazers_count'],
                'label': rep['description'],
                'xlink': rep['html_url']
            
        }
            self.plotar_dicts.append(self.plotar_dict)

    def Criarvisualizacao(self):
        '''Cria a visualização dos dados'''
        
        # Configura a tela
        self.tela = LS('#333366', base_style=LCS)
        self.configuracao = pygal.Config()
        self.configuracao.x_label_rotation = 45
        self.configuracao.show_legend = False
        self.configuracao.title_font_size = 24
        self.configuracao.label_font_size = 14
        self.configuracao.major_label_font_size = 18
        self.configuracao.truncate_label = 15
        self.configuracao.show_y_guides = False
        self.configuracao.width = 1000
        
        
        #Cria os graficos
        self.graficos = pygal.Bar(self.configuracao, style=self.tela)
        self.graficos.title = 'Repositorios do github com mais estrelas'
        self.graficos.x_labels = self.nomes

        self.graficos.add('', self.plotar_dicts)
        self.graficos.render_to_file('Projeto_Python.svg')





comecar = ScrapingComPygal()
comecar.Iniciar()
