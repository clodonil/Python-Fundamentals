Módulo 1 - Lista de Exercício
=========

Para realização desse exercício vamos utilizar a lista de municipios do Brasil, juntamente com a taxa de homicídio e a taxa de fecundidade. Vamos realizar o cruzamento dessas informações para obter respostas interessantes:

![lista_exercicio](https://github.com/clodonil/curso_python/blob/master/Imagens/m1_exercicio.JPG)

* https://pt.wikipedia.org/wiki/Lista_de_munic%C3%ADpios_do_Brasil_por_popula%C3%A7%C3%A3o
* https://pt.wikipedia.org/wiki/Lista_de_cidades_por_taxa_de_homic%C3%ADdios
* https://pt.wikipedia.org/wiki/Lista_de_unidades_federativas_do_Brasil_por_taxa_de_fecundidade

Para obter os valores da lista dinamicamente, será utilizado a biblioteca Scrapy_table. Se uma página tiver mais de uma tabela, informe qual delas deseja obter. Para obter as tabelas acima utilize o seguinte código:

```python
# importa a lib para obter as tabelas da Wikipedia
from  lib.scrapy_table import Scrapy_Table
# Variavel com o link da tabela
url="https://pt.wikipedia.org/wiki/C%C3%A2mara_Municipal_de_S%C3%A3o_Paulo"
# Inicia a class para obter a tabela
site_connect = Scrapy_Table(url)
# Pegando a tabela 5 (Vereadores em exercicio)
tables = site_connect.get_tables(5)
```

Com essa informação, vamos responder as perguntas abaixo.desenvolvendo os códigos em Python.
<span style=“color:green;”> text fsdfsdfsdfsdgoes here</span>
```css
>> Questões consideradas para nota:


1. **Listar o nome de todos os municpios do Brasil com o código do IBGE:**


2. **Listar os partidos que tiveram candidatos eleitos:**
   
3. **Mostrar o somatória de todos os votos em vereadores:**

4. **Pesquisar se tem algum vereador vereador com os seguintes nomes (João, Eduardo, josé):**
	
5. **O partido que tive mais vereadores eleitos:**
```

> Obrigatório para nota

6. **Numero total de votos por partidos:**

7. **Pesquisar se tem algum vereador está na lista de investigados na Lava Jato:**

8. **Pesquisar se tem algum vereador está na lista de investigados na Lava Jato:**

9. **Pesquisar se tem algum vereador está na lista de investigados na Lava Jato:**

10. **Pesquisar se tem algum vereador está na lista de investigados na Lava Jato:**
