<!-- $theme: gaia -->
# ![30%](image/logo2.png)
### Python Fundamentals

#### [Módulo 2](https://github.com/clodonil/Python-Fundamentals/tree/master/modulo2)

###### [Clodonil Trigo (@clodonil)](https://github.com/clodonil)



---
<!-- *template: invert -->
# Revisão
## Estrutura de Dados
* String/Number;
<small>
 ```python
 valor = "Tudo e possível"
 ```
</small>

* List; 
<small>
```python
lista = ['jose',30]
```
</small>

---
<!-- *template: invert -->
# Revisão
## Estrutura de Dados

* Tuple;
<small>
```python
lista = ('jose',30)
```
</small>

* Dictionary;
<small>
```python
lista = {'Nome':'jose Silva','idade':30}
```
</small>

---
<!-- *template: invert -->
# Revisão
## Controle de Fluxo 

- **if**

<small>
  
 ```python
 if x > 10 and x < 50:
    print("Valor maior 10 e menor qur 50")
 ```
</small>

- **for**
<small>
 ```python
 words = ['gato', 'cachorro', 'coelho']
 for key in words:
     print("Key -> {0}".format(key))
 ```
</small>

---
<!-- *template: invert -->
# Revisão
## Controle de Fluxo 

- **while**

<small>

```python
 x=0
 while x < 10:
   print("Valor de x = {0}".format(x))
   x +=1
 ```
</small>
  
---
	
# Módulo 2
# ![](image/ferramentas.jpg)
---

# Principais Métodos - Strings

<small>
  
```python
s = "se nada mudar, invente."
```

  
|Método | Sintaxe|Exemplo|
|-|-------|---|
|s.capitalize()	|s.capitalize()|"Titulo"|
|s.center(width, char)	|`s.center(50,'-')`|--texto--
|s.ljust(width, char)	|`s.ljust(30,'-')`|texto---
|s.rjust	|`s.rjust(30,'-')`|---texto|
|s.count(t, end)|`s.count('e')`  e `s.count('e',2,23)`| 3 e 2

</small>

---
# Principais Métodos - Strings

<small>

|Método | Sintaxe |Exemplo|
|-------|-------|------|
|s.find(t, start, end)	|`s.find('e'`) e `s.find('e',2,20)`| 1, 18
|s.rfind(t, start, end)	|`s.rfind('e')` e `s.rfind('e',2,20)`| 21, 18
|s.isalnum()  |`s.isalmun()`| False
|s.isalpha()	|`s.isalpha()`| False
|s.isdecimal()	|`s.isdecimal()`| False
|s.islower()	|`s.islower()`| True
|s.isupper()	|`s.isupper()`| False

</small>

---
# Principais Métodos - Strings

<small>

|Método | Sintaxe|Exemplo|
|-------|-------|---|
|s.isspace()	|`s.isspace()`| False
|s.join(t)	|`s = '.'` , `t='dois'` e  `s.join(t)`|'d.o.i.s'
|s.lower()	|`s.lowe()`|
|s.upper()	|`s.upper()`|
|s.partition(t)|`s.partition('m')`|
|s.split(t, n)|	`s.split('e')`|
|s.splitlines(f)|`s.splitlines()`|

</small>

---
# Principais Métodos - Strings

<small>

|Método | Descrição|Sintaxe|
|-------|-------|---|
|s.strip(t)|Remove espaço no inicio e fim da string |`s.strip()`| 
|s.lstrip(chars)|Remove espaço do lado esquerdo|`s.lstrip()`|
|s.rstrip(chars)|Remove espaço do lado direito|`s.rstrip()`|
|s.swapcase()|Inverte para lowe()/upper()|`s.swapcase()`|
|s.title()|Primeiros caracteres em Maiúscula	|`s.title()`|

</small>

---
<!-- page_number: true -->
# Principais Métodos - Number


* Inteiro

<small>


```python
a=10
```

| Méthodo  | Descrição  | Exemplo|
|----------|------------|--------|
|bit_length |  Quantidade de bit para guardar o inteiro         | ``bin(a)`` ; ```a.bit_length()```    
|to_bytes|  Retonar os bytes que representam o inteiro.         |   ```a.to_bytes(2, byteorder='big')``` |

</small>

---

# Principais Métodos - Number


* Float

<small>

```python
a=10.1
```

| Méthodo  | Descrição  | Exemplo|
|---------|-------------|-------|
|as_integer_ratio| Retorna um par de inteiros cuja proporção é gual ao float original| ```a.as_integer_ratio()```       |    
|hex| Converte um float em Hex          | ```a.hex()```       |  
|is_integer|  Verifica se o conteúdo do float é Inteiro         |   ```float(10).is_integer()``` |  

</small>

---
# Principais Métodos - List

<small>

```python
lista=[]
```

| Méthodo  | Descrição  | Exemplo| 
|----------|------------|--------|
|append    | Adiciona um item no final da lista           |  ```lista.append('jose')```         |
|copy  | Faz uma copia da lista           |   ```lista_b = lista.copy()```         |
|count  |  retorna o número de ocorrência de um item          | ```lista.count('jose')```    |
|extend  | Prolonga a lista, adicionando no fim todos os elementos de outra lista            | ```lista.extend([10,'maria'])```      |

</small>

---
# Principais Métodos - List

<small><small>

| Méthodo  | Descrição  | Exemplo| 
|----------|------------|--------|
|index  |Retorna o índice do primeiro item pesquisado| ```lista.index('jose')```         |
|insert  | Insere um item em uma posição especificada. | ```lista.insert(0,'pedro')```  |
|pop  |Remove o item na posição dada. |   ```lista.pop()``` ```lista.pop(0)``` |
|remove  | Remove o primeiro item encontrado na lista conforme o valor passado.     |   ```lista.remove('jose')```  |
|reverse  |Inverte a ordem dos elementos na lista |    ```lista.reverse()``` |
|sort  |  Ordena os itens na própria lista|  ```lista.sort()```|
|clear  | Limpa toda a lista (remove tudo)| ```lista.clear()```|

</small></small>

---
# Principais Métodos - Tuple

<small>

```python
t = ('jose','maria','pedro')
```
|Método|Descrição| Exemplo|
|------|---------|--------|
|t.count(x) |  Retorna o número de itens que são iguais a x       |  ```t.count('jose')```       |
|t.index(x) |  Retorna o index do primeiro item encontrado que seja igual a x  | ``` t.index('pedro')``` |

</small>

---
## Principais Métodos - Dictionaries

<small><small>

```python
st = {'SP':'São Paulo','RJ':'Rio de Janeiro','MG':'Minas Gerais' }
```
|Métodos | Descrição | Exemplo |
|-------|-----------|---------|
|st.copy()| Faz uma cópia do dicionário| ```new = st.copy()```|
|st.get()      |Retorna um valor de uma chave         | ```st.get('SP')``` , ```st['SP']```        |
|st.items()    |Retorna uma visão do dicionário (key e value)        |```st.items()```         |
|st.keys()     |Retorna uma visão do dicionário (key)         |    ```st.keys()```     |
|st.values()   |Retorna uma visão do dicionário (value)         |   ```st.values()```      |
|st.pop()      |Remove e Retorna um valor de uma chave.         |   ```st.pop('RS')```      |

</small></small>

---
## Principais Métodos - Dicionário

<small>

|Métodos | Descrição | Exemplo |
|-------|-----------|---------|
|st.popitem()    |Remove e retorna um par(key, value) pela ordem de LIFO         | ```st.popitem()```         |
|st.update()     |Atualiza um dicionário.         |   ```st.update({'RS':'Rio Grande do Sul'})```      |
|st.clear()     | Limpa todos os elementos de um dicionário         | ```st.clear()```        |

</small>

---
## Principais Métodos - Set


<small>  

```python
conj1 = {1,3,4,5,6}        
conj2 = {200,300,400,500,1,2,3}
```
<small>


|Métodos | Descrição | Exemplos |
|--------|-----------|----------|
|conj1.add()	  | Adiciona elementos ao Set| ```conj1.add('jose')```|
|conj1.copy()	| Faz a cópia de um Set|```new = conj1.copy()``` |
|conj1.clear()	|Remove todos os elementos de um  set|``` new.clear()```|
|conj1.remove()|	Remove elementos de um Set| ```conj1.remove('jose')```|
|conj1.difference()|Retorna a diferença entre 2 Sets conj1 - conj2 |```conj1.difference(conj2)```|
|conj1.discard()	|Remove elemento de um Set, se estiver presente|```conj1.discard('jose')```|

</small></small>

---
## Principais Métodos - Set

<small><small>

|Métodos | Descrição | Exemplos |
|--------|-----------|----------|
|conj1.intersection()	|Retorna a interseção de 2 ou mais Sets|```conj1.intersection(conj2)```|
|conj1.pop()	|Remove um elemento arbitrario|```conj1.pop()```|
|conj1.union()	|Retorna um novo Set com a União entre Sets|```conj1.union(conj2)```|
|conj1.update()|	Add Elements to The Set.|``` conj1.update({8,4,5}) ```|

</small></small>

---
## Principais Métodos - Set
<small>

|Métodos | Descrição | Exemplos |
|--------|-----------|----------|
|len()	|Retorna o tamanho do Set|``` len(conj1) ```|
|max()	|Retorna o maior elemento de um Set|``` max(conj1)```|
|min()	|Retorna o menor elemento de um Set|``` min(conj1)```|
|sorted()|	Retorna uma lista ordenada| ``` sorted(conj1)```|
|sum()	|Retorna a soma de um Set|``` sum(conj1) ```|
|zip()	|Retorna a interação entre dois set|``` list(zip(conj1,conj2))```|

</small>

---
# Funções built-in

68 comandos internos.

<small><small><small>

|            |            | 		|      |        | |
|------------|------------|---------------------|------|--------|-----|
|abs()	      |`dict()`	      |help()	       |`min()`      |	setattr()|delattr()	|
|all()	      |dir()	       |hex()	        |next()	    |zip()|hash() |
|any()	      |divmod()     |	`id()`	        |object()	  |`sorted()`| memoryview()|
|ascii()	    |enumerate()	 |`input()`	      |oct()	     |`type()`| `set()`	|
|`bin()`	      |eval()       |	`int()`	       |open()     |	`str()`|complex()|
|`bool()`	     |exec()       |	isinstance()	|ord()	     |`sum()`|hasattr()|
|bytearray()	|filter()	    |issubclass()	 |pow()	     |super()|`max()` |
| vars()  |`float()`      |	iter()	      |`print()`    |	`tuple()`|round() |
|callable() 	|`format()`	    |`len()`	        |property()	|\__import__()|reversed()|
|chr()	      |`frozenset()`	 |`list()`	       |range()   	|map()|globals() |
|classmethod()	| getattr()	|locals()      |	repr()   	|compile()|

</small></small></small>

---

<!-- template: gaia -->

# Laboratório Módulo 2
