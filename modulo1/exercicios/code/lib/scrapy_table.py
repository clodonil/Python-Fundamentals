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
      def __init__(self, url):
          # links
          self.url = url

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
          all_table = []
          for table in page.find_all('table'):
              ntable = [] 
              rows = table.find_all('tr')
              for row in rows:
                  cols = row.find_all('td')
                  if not cols:
                     cols = row.find_all('th')

                  cols = [ele.text.strip() for ele in cols]
                  ntable.append([ele for ele in cols if ele])
              all_table.append(ntable)
          return all_table     
   

      def get_tables(self, ntables=-1):
          '''
             Metodo para iniciar acao da classe
          '''
          all_tables = []
          page = self.get_page(self.url)
          if page:
              all_tables = self.busca_table(page)

              if ntables != -1:
                 return all_tables[ntables]

          return all_tables

