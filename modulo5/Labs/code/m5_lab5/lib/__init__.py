# -*- coding: utf-8 -*-
'''
classe: DadosAbertos
descrição: classe que utiliza API dos dados abertos
autor: Clodonil Honorio Trigo
email: clodonil@nisled.org
data: 20 de Agosto de 2018
'''
import requests


class DadosAbertos:
    def __init__(self):
       self.url = 'https://dadosabertos.camara.leg.br/api/v2/'
                  

    def get(self,link):
        #parametros = {'formato': 'json', 'itens': 600}
        
        resposta = requests.get(link)      
        try: 
           return resposta.json()['dados']
        except:
           return resposta.json()

    def frentes(self):
        link = self.url + '/frentes'
        return self.get(link)
        
    def blocos(self):
        link = self.url + '/blocos'
        return self.get(link)
       
    def blocos_id(self,id):
        link = self.url + '/blocos/' + str(id)
        return self.get(link)

    def deputados(self):
        link = self.url + 'deputados/'
        return self.get(link)

    def deputado_id(self,id):
        link = self.url + 'deputados/' + str(id)
        return self.get(link)
    
    def deputado_despesas(self,id):
        link = self.url + 'deputados/' +  str(id) + '/despesas'
        return self.get(link)
       
    def deputado_discursos(self,id):
        link = self.url + 'deputados/' + str(id) + '/discursos'
        return self.get(link)

    def deputado_eventos(self,id): 
       # /deputados/{id}/eventos
       link = self.url + 'deputados/' + str(id) + '/eventos'
       return self.get(link)

    def deputado_orgaos(self,id): 
      # /deputados/{id}/orgaos
      link = self.url + 'deputados/' + str(id) + '/orgaos'
      return self.get(link)

    def deputado_mesa(self,id):
      # /legislaturas/{id}/mesa
      link = self.url + 'deputados/' + str(id) + '/orgaos'
      return self.get(link)

    def  situacoesDeputado(self):    
       # /referencias/situacoesDeputado
       link = self.url + 'referencias/situacoesDeputado'
       return self.get(link)

    def eventos(self):
      # /eventos
      link = self.url + 'eventos'
      return self.get(link)

    def evento_id(self,id):
      # /eventos/{id}
      link = self.url + 'eventos/' + str(id)
      return self.get(link)

    def evento_deputados(self,id):
      # /eventos/{id}/deputados
      link = self.url + 'eventos/' + str(id) + '/deputados'
      return self.get(link)

    def evento_pauta(self,id):
      # /eventos/{id}/pauta
      link = self.url + 'eventos/' + str(id) + '/pauta'
      return self.get(link)

    def partidos(self): 
      # /partidos
      link = self.url + 'partidos'
      return self.get(link)
      
    def partido_id(self,id):    
      # /partidos/{id}
      link = self.url + 'partidos/' + str(id)
      return self.get(link)
    def orgaos(self):
       # /orgaos
       link = self.url + 'orgaos'
       return self.get(link)

    def orgaos_id(self,id):
       # /orgaos/{id}
       link = self.url + 'orgaos/' + str(id)
       return self.get(link)

    def orgaos_eventos(self,id):
       # /orgaos/{id}/eventos
       link = self.url + 'orgaos/' + str(id) + '/eventos'
       return self.get(link)

    def orgaos_membros(self,id): 
       # /orgaos/{id}/membros
       link = self.url + 'orgaos/' + str(id) + '/membros'
       return self.get(link)

    def proposicoes(self):
       # /proposicoes
       link = self.url + 'proposicoes/'
       return self.get(link)

    def proposicoes_id(self,id):
       # /proposicoes/{id}
       link = self.url + 'proposicoes/' + str(id)
       return self.get(link)
  
    def proposicoes_autores(self,id):
       # /proposicoes/{id}/autores
       link = self.url + 'proposicoes/' + str(id) + '/autores'
       return self.get(link)

    def proposicoes_relacionadas(self,id):
       # /proposicoes/{id}/relacionadas
       link = self.url + 'proposicoes/' + str(id) + '/relacionadas'
       return self.get(link)
       
    def proposicoes_tramitacoes(self,id):     
       # /proposicoes/{id}/tramitacoes
       link = self.url + 'proposicoes/' + str(id) + '/tramitacoes'
       return self.get(link)

    def proposicoes_votacoes(self, id):
       # /proposicoes/{id}/votacoes
       link = self.url + 'proposicoes/' + str(id) + '/votacoes'
       return self.get(link)   

    def referencias_situacoesEvento(self):
       # /referencias/situacoesEvento
       link = self.url + 'referencias/situacoesEvento'
       return self.get(link)   
    def referencias_tiposEvento(self):  
      # /referencias/tiposEvento
      link = self.url + '/referencias/tiposEvento'
      return self.get(link)   
    
    def legislaturas(self):  
      # /legislaturas
      link = self.url + '/legislaturas'
      return self.get(link)   
    
    def legislaturas(self,id):  
      # /legislaturas/{id}
      link = self.url + '/legislaturas' + str(id)
      return self.get(link)   
    def legislaturas_mesa(self,id):
      # /legislaturas/{id}/mesa
      link = self.url + '/legislaturas' + str(id) + '/mesa'
      return self.get(link)   
  
    def referencias_situacoesProposicao(self):
      # /referencias/situacoesProposicao
      link = self.url + '/referencias/situacoesProposicao'
      return self.get(link)   
    
    def referencias_tiposProposicao(self):
      # /referencias/tiposProposicao
      link = self.url + '/referencias/tiposProposicao'
      return self.get(link)   
    
    def referencias_tiposTramitacao(self):
      # /referencias/tiposTramitacao
      link = self.url + '/referencias/tiposTramitacao'
      return self.get(link)   
    
    def referencias_situacoesDeputado(self):
       # /referencias/situacoesDeputado
      link = self.url + '/referencias/situacoesDeputado'
      return self.get(link)   
      
    def referencias_situacoesEvento(self):
       # /referencias/situacoesEvento
      link = self.url + '/referencias/situacoesEvento'
      return self.get(link)   
      
    def referencias_situacoesOrgao(self):
       # /referencias/situacoesOrgao
      link = self.url + '/referencias/situacoesOrgao'
      return self.get(link)   
      
    def referencias_situacoesProposicao(self):
       # /referencias/situacoesProposicao
      link = self.url + '/referencias/situacoesProposicao'
      return self.get(link)   
      
    def referencias_tiposEvento(self):
       # /referencias/tiposEvento
      link = self.url + '/referencias/tiposEvento'
      return self.get(link)   
      
    def referencias_tiposOrgao(self):
       # /referencias/tiposOrgao
      link = self.url + '/referencias/tiposOrgao'
      return self.get(link)   
      
    def referencias_tiposProposicao(self):
       # /referencias/tiposProposicao
      link = self.url + '/referencias/tiposProposicao'
      return self.get(link)   
      
    def referencias_tiposTramitacao(self):
       # /referencias/tiposTramitacao
      link = self.url + '/referencias/tiposTramitacao'
      return self.get(link)   
   
    def referencias_uf(self):
      # /referencias/uf
      link = self.url + '/referencias/uf'
      return self.get(link)   
    
    def help(self): 
        metodos = """ Métodos da class  Dados Abertos:
                   blocos()                               : Lista de dados sobre os blocos partidários
                   blocos_id(bloco_id)                    : Informações sobre um bloco partidário específico
                   deputados()                            : Listagem e busca de deputados, segundo critérios
                   deputado_id(deputado_id)               : Informações detalhadas sobre um deputado específico
                   deputado_despesas(deputado_id)         : As despesas com exercício parlamentar do deputado
                   deputado_discursos(deputado_id)        : Os discursos feitos por um deputado em vários eventos
                   deputado_eventos(deputado_id)          : Uma lista de eventos com a participação do parlamentar
                   deputado_orgaos(deputado_id)         : Os órgãos dos quais um deputado é integrante
                   deputado_mesa(deputado_id)             : Quais deputados fizeram parte da Mesa Diretora em uma legislatura
                   situacoesDeputado()                    : As possíveis situações de exercício parlamentar de um deputado
                   eventos()                              : Lista de eventos ocorridos ou previstos nos diversos órgãos da Câmara
                   evento_id(evento_id)                   : Informações detalhadas sobre um evento específico
                   evento_deputados(evento_id)            : Os deputados participantes de um evento específico
                   evento_pauta(evento_id)                : Lista de proposições que foram ou deverão ser avaliadas em um evento de caráter deliberativo
                   partidos()                             : Os partidos políticos que têm ou já tiveram parlamentares em exercício na Câmara
                   partido_id(partido_id)                 : Informações detalhadas sobre um partido
                   orgaos()                               : A lista das comissões e outros órgãos legislativos da Câmara
                   orgaos_id(orgao_id)                    : Informações detalhadas sobre um órgão legislativo
                   orgaos_eventos(orgao_id)               : Informações detalhadas sobre um órgão legislativo
                   orgaos_membros(orgao_id)               : Informações detalhadas sobre um órgão legislativo 
                   proposicoes()                          : Lista configurável de proposições na Câmara
                   proposicoes_id(proposicao_id)          : Informações detalhadas sobre uma proposição específica
                   proposicoes_autores(proposicao_id)     : Lista pessoas e/ou entidades autores de uma proposição
                   proposicoes_relacionadas(proposicao_id): Uma lista de proposições relacionadas a uma em especial
                   proposicoes_tramitacoes(proposicao_id) : O histórico de passos na tramitação de uma proposta
                   proposicoes_votacoes(proposicao_id)    : As votações por quais uma proposição já passou
                   referencias_situacoesEvento()          :  As possíveis situações para eventos
                   referencias_tiposEvento()              : Os tipos de eventos realizados na Câmara
                   legislaturas()                         : Os períodos de mandatos e atividades parlamentares da Câmara
                   legislaturas(legislatura_id)           : Informações extras sobre uma determinada legislatura da Câmara
                   legislaturas_mesa(legislatura_id)      : Quais deputados fizeram parte da Mesa Diretora em uma legislatura
                   referencias_situacoesProposicao()      : Os possíveis estados de tramitação de uma proposição
                   referencias_tiposProposicao()          : Os vários tipos de proposições existentes
                   referencias_tiposTramitacao()          : Os vários tipos de tramitação existentes
                   referencias_situacoesDeputado()        : As possíveis situações de exercício parlamentar de um deputado                   
                   referencias_situacoesOrgao()           : As situações em que órgãos podem se encontrar
                   referencias_tiposOrgao()               : Os tipos de órgãos que existem na Câmara
                   referencias_uf()                       : Identificadores dos estados e do Distrito Federal 
                  """    
        return metodos
# /proposicoes/{id}/votacoes
# /votacoes/{id}
# /votacoes/{id}/votos
# /referencias/situacoesOrgao
