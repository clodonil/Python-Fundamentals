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
        resposta = requests.get(link)      
        try: 
           return resposta.json()['dados']
        except:
           return resposta.json()
  
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
        link = self.url + str(id) + '/despesas'
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
                   blocos():
                   blocos_id(id):
                   deputados():
                   deputado_id(id):
                   deputado_despesas(id):
                   deputado_discursos(id):
                   deputado_eventos(id):
                   deputado_orgaos(id):
                   deputado_mesa(id):
                   situacoesDeputado():
                   eventos():
                   evento_id(id):
                   evento_deputados(id):
                   evento_pauta(id):
                   partidos():
                   partido_id(id):
                   orgaos():
                   orgaos_id(id):
                   orgaos_eventos(id):
                   orgaos_membros(id):
                   proposicoes():
                   proposicoes_id(id):
                   proposicoes_autores(id):
                   proposicoes_relacionadas(id):
                   proposicoes_tramitacoes(id):
                   proposicoes_votacoes(id):
                   referencias_situacoesEvento():
                   referencias_tiposEvento():
                   legislaturas():
                   legislaturas(id):
                   legislaturas_mesa(id):
                   referencias_situacoesProposicao():
                   referencias_tiposProposicao():
                   referencias_tiposTramitacao():
                   referencias_situacoesDeputado():
                   referencias_situacoesEvento():
                   referencias_situacoesOrgao():
                   referencias_situacoesProposicao():
                   referencias_tiposEvento():
                   referencias_tiposOrgao():
                   referencias_tiposProposicao():
                   referencias_tiposTramitacao():
                   referencias_uf():      
                  """    
        print(metodos)
# /proposicoes/{id}/votacoes
# /votacoes/{id}
# /votacoes/{id}/votos
# /referencias/situacoesOrgao
