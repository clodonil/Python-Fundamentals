import requests


class DadosAbertos:
  def __init__(self):
       self.url = 'https://dadosabertos.camara.leg.br/api/v2/'

  def get(self,link):
      resposta = requests.get(link)
      return resposta.json()['dados']
  
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
     


st = DadosAbertos()

dados = st.evento_pauta(6174)
print(dados)
#print(dados)
#print(st.deputado_orgaos(73579))

#dados.situacoesDeputado()



# /referencias/situacoesEvento
# /referencias/tiposEvento
# /legislaturas
# /legislaturas/{id}
# /legislaturas/{id}/mesa
# /referencias/situacoesProposicao
# /referencias/tiposProposicao
# /referencias/tiposTramitacao
# /referencias/situacoesDeputado
# /referencias/situacoesEvento
# /referencias/situacoesOrgao
# /referencias/situacoesProposicao
# /referencias/tiposEvento
# /referencias/tiposOrgao
# /referencias/tiposProposicao
# /referencias/tiposTramitacao
# /referencias/uf
# /proposicoes/{id}/votacoes
# /votacoes/{id}
# /votacoes/{id}/votos
# /referencias/situacoesOrgao
