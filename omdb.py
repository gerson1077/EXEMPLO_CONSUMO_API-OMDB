import requests
from pprint import pprint

'''
A primeira coisa a fazer é ir ao site http://www.omdbapi.com/
e clicar no link API key.

Cadastre-se, abra o e-mail e valide sua chave. Depois, você
poderá acessar o OMDb.
'''

'coloque aqui a sua chave de acesso à api'
api_key = '32edef49'

'''
Antes de fazer qualquer função, vamos experimentar
consultar o OMDb pelo navegador.

Digite, por exemplo, a seguinte URL no Firefox:
    http://www.omdbapi.com/?s=star%20wars&apikey=32edef49

Observe que vemos uma lista de 10 filmes, mas há mais resultados.

Para ver a página 2, acesse
    http://www.omdbapi.com/?s=star%20wars&page=2&apikey=e51a115c
'''


'''
Observe que nas URLs acima, estamos passando parâmetros.
Na URL http://www.omdbapi.com/?s=star%20wars&page=2&apikey=32edef49
definimos 3 parâmetros:
 * s=star wars
 * page=2
 * apikey=32edef49
'''

'''
QUESTÃO 1
Olhando para os resultados da consulta
http://www.omdbapi.com/?s=star%20wars&apikey=32edef49,
quantos filmes foram encontrados para o termo "star wars"?

Resposta: 921

QUESTÃO 2
Consultando a documentação em www.omdbapi.com, você
pode aprender a filtrar os resultados da sua busca,
ficando apenas com filmes, eliminando jogos e séries.

Como fazer isso?

Se você fizer essa consulta, quantos filmes
existem para a busca star wars?

Resposta: 649

QUESTÃO 3:
E se ao invés de filmes você quiser só jogos,
quantos existem?

Resposta: 110

'''




'''
Vou te deixar dois exemplos de como acessar a URL. Nesse exemplo,
eu estou retornando o dicionário inteiro.
'''

def busca_por_id(film_id):
    url = f"http://www.omdbapi.com/?apikey={api_key}&i={film_id}"
    pedido = requests.get(url)
    dicionario_do_pedido = pedido.json()
    return dicionario_do_pedido

def busca_por_texto(texto_buscar):
    url = f"http://www.omdbapi.com/?apikey={api_key}&s={texto_buscar}"
    pedido = requests.get(url) #conectar na URL
    dicionario_do_pedido = pedido.json() #transformo a string que eu recebi num dicionário de python
    return dicionario_do_pedido

'''
Experimente! chame d1=busca_por_texto('star wars') e examine o
dicionário d1 retornado.
'''

'''
Agora, faça uma função busca_qtd_total que retorna quantos
itens (pode ser filme, jogo, série ou o que for) batem com
uma determinada busca.
'''
def busca_qtd_total(texto_buscar):
    
    total = busca_por_texto(texto_buscar)
    return total['totalResults']

'''
Faça uma função busca_qtd_filmes que retorna quantos
filmes batem com uma determinada busca.
'''
def busca_qtd_filmes(texto_buscar):
    url = f"http://www.omdbapi.com/?apikey={api_key}&s={texto_buscar}&type=movie"
    pedido = requests.get(url) #conectar na URL
    dicionario_do_pedido = pedido.json() #transformo a string que eu recebi num dicionário de python
    return dicionario_do_pedido['totalResults']
# alternativa
def busca_qtd_especifica(texto_buscar, tipo):
    url = f"http://www.omdbapi.com/?apikey={api_key}&s={texto_buscar}&type={tipo}"
    pedido = requests.get(url) #conectar na URL
    dicionario_do_pedido = pedido.json() #transformo a string que eu recebi num dicionário de python
    return dicionario_do_pedido['totalResults']


'''
Faça uma função busca_qtd_jogos que retorna quantos
jogos batem com uma determinada busca.
'''
def busca_qtd_jogos(texto_buscar):
    url = f"http://www.omdbapi.com/?apikey={api_key}&s={texto_buscar}&type=game"
    pedido = requests.get(url) #conectar na URL
    dicionario_do_pedido = pedido.json() #transformo a string que eu recebi num dicionário de python
    return dicionario_do_pedido['totalResults']

'''
Agora, vamos aprender a ver os detalhes de um filme.

Por exemplo, na lista de filmes podemos ver que o filme
star wars original (de 1977) tem id 'tt0076759'

Acessando a URL
http://www.omdbapi.com/?i=tt0076759&apikey={SUA-CHAVE-VEM-AQUI}
podemos ver mais detalhes.

Observe que agora não temos mais o parâmetro 's=star%20wars'
mas sim i=tt0076759. Mudou o nome da "variável", não só
o valor.
'''

'''
Faça uma função nome_do_filme_por_id que recebe a id de
um filme e retorna o seu nome.
'''
def nome_do_filme_por_id(id_filme):
    url = f"http://www.omdbapi.com/?apikey={api_key}&i={id_filme}"
    pedido = requests.get(url)
    dicionario_do_pedido = pedido.json()
    return dicionario_do_pedido['Title']

'''
Faça uma função ano_do_filme_por_id que recebe a id de
um filme e retorna o seu ano de lançamento.
'''
def ano_do_filme_por_id(id_filme):
    url = f"http://www.omdbapi.com/?apikey={api_key}&i={id_filme}"
    pedido = requests.get(url)
    dicionario_do_pedido = pedido.json()
    return dicionario_do_pedido['Year']

'''
Peguemos vários dados de um filme de uma vez.

A ideia é receber uma id e retornar 
um dicionário com diversos dados do filme.

O dicionário deve ter as seguintes chaves:
 * ano
 * nome
 * diretor
 * genero

E os dados devem ser preenchidos baseado nos dados do site.
'''
# def dados_do_filme_por_id(id_filme):
#     url = f"http://www.omdbapi.com/?apikey={api_key}&i={id_filme}"
#     pedido = requests.get(url)
#     dicionario_do_pedido = pedido.json()
    
#     dicionario = {}
#     dicionario['ano'] = dicionario_do_pedido['Year']
#     dicionario['nome'] = dicionario_do_pedido['Title']
#     dicionario['diretor'] = dicionario_do_pedido['Director']
#     dicionario['genero'] = dicionario_do_pedido['Genre']
    
    # return dicionario
    
#otimizar o código
def dados_do_filme_por_id(id_filme):
    dicionario_do_pedido = busca_por_id(id_filme)
    
    dicionario = {}
    dicionario['ano'] = dicionario_do_pedido['Year']
    dicionario['nome'] = dicionario_do_pedido['Title']
    dicionario['diretor'] = dicionario_do_pedido['Director']
    dicionario['genero'] = dicionario_do_pedido['Genre']
    
    return dicionario


'''
Voltando para a busca...

Faça uma função busca_filmes que, dada uma busca, retorna
os dez primeiros items (filmes, series, jogos ou o que for)
que batem com a busca.

A sua resposta deve ser uma lista, cada filme representado por 
um dicionário. cada dicionario deve conter os campos
'nome' (valor Title da resposta) e 'ano' (valor Year da resposta).
'''
#sugestão copilot
# def busca_filmes(texto_buscar):
#     dicionario_do_pedido = busca_por_texto(texto_buscar)
#     lista = []
    
#     for i in range(10):
#         dicionario = {}
#         dicionario['nome'] = dicionario_do_pedido['Search'][i]['Title']
#         dicionario['ano'] = dicionario_do_pedido['Search'][i]['Year']
#         lista.append(dicionario)
    
#     return lista

def busca_filmes(texto_buscar):
    dic_busca = busca_por_texto(texto_buscar)
    lista_de_filmes = dic_busca['Search']
    lista_resposta = []
    for filme in lista_de_filmes:
        dic = {}
        dic['nome'] = filme['Title']
        dic['ano'] = filme['Year']
        #guardar o dicionário na lista
        lista_resposta.append(dic)
           
    return lista_resposta


'''
Faça uma função busca_filmes_grande que, dada uma busca, retorna
os VINTE primeiros filmes que batem com a busca.
'''
def busca_filmes_grande(texto_buscar):
    dic_busca = busca_por_texto(texto_buscar)
    lista_de_filmes = dic_busca['Search']
    lista_resposta = []
    for filme in lista_de_filmes[:20]:
        dic = {}
        dic['nome'] = filme['Title']
        dic['ano'] = filme['Year']
        #guardar o dicionário na lista
        lista_resposta.append(dic)
           
    return lista_resposta


