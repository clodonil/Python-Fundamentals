# -*- coding: utf-8 -*-
'''
classe: Scrapy
descrição: Exercicio para buscar todos os links de um site
autor: Clodonil Honorio Trigo
email: clodonil@nisled.org
data: 04 de julho de 2017
'''

import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse


class Scrapy_Table:
      def __init__(self):
          # links
          self.links = []
          self.domain = ""
          self.list_link = []

      def get_page(self,url):    
          '''
             Metodo que conecta na pagina
          '''
          #Domain
          self.domain = urlparse(url).netloc

          #conecta na pagina     
          fonte = requests.get(url)

          #Verifica se o status é de sucesso
          if fonte.status_code == 200:
              return  BeautifulSoup(fonte.text,"lxml")
          else:
              #Apresenta a mensagem de erro
              return(False)

      
      def busca_tag(self, page,tag):
          return page.find_all(tag)

      def busca_table(self,page):
          ''' 
              Metodo para buscar o links da pagina e verifica se pertece ao mesmo dominio
          '''
          for link in page.find_all('a', attrs={'class':'item__info-title'}):
              hlink = link.get('href')
              if len(link.text) > 0:
                 if not hlink in self.links:
                    self.links.append(hlink)
                    self.list_link.append([hlink,self.check_domain(hlink)]) 
         
          _next = page.find('li', attrs={'class':'pagination__next'})
          proximo = _next.a.get('href')
          if proximo == "#":
             return False
          else:
             return proximo
   
      def clear(self, tag):
           '''
              Limpar lixo da tag
           '''
           return tag.replace("\n","").replace("\t","")

      def check_domain(self,url):
           if self.domain == urlparse(url).netloc:
               return True
           else:
               return False

      def run(self, site):
          '''
             Metodo para iniciar acao da classe
          '''
          #Domain
          #self.domain = urlparse(site).netloc
          #self.list_link.append([site,True])
          #self.links.append(site)

          #while self.list_link:
          #     url = self.list_link.pop()
          #     if url[1]:
          _next=site
          while _next:
              _next = self.busca_links(self.get_page(_next))

          for k in self.links:
              print(k)
          return self.links


if __name__ == "__main__":
     url="https://pt.wikipedia.org/wiki/Lista_de_cidades_por_taxa_de_homic%C3%ADdios"
     site_connect = Scrapy_Table()
     tables = site_connect.run(url)
