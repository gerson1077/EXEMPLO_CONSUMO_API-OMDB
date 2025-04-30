import requests

#faça uma função usando a biblioteca requests
#que acessa a URL  /corredores do servidor de corredores
#via GET e devolve uma lista de dicionários com os corredores
def todos_corredores():
    #com quem vou me conectar?
    url = 'http://localhost:5000/corredores'
    #conectar na URL usando o verbo GET
    r = requests.get(url)
    lista = r.json()
    return lista

#faça uma função usando a biblioteca requests
#que acessa a URL  /corredores do servidor de corredores
#via POST, enviando um ddicionário de um novo corredor
#um corredor tem os campos "nome", "id" e "tempo"
def adiciona_corredor(nome, tempo, id):
    #com quem vou me conectar?
    url = 'http://localhost:5000/corredores'
    #conectar na URL usando o verbo POST
    dici_corredor = {"nome": nome, "tempo": tempo, "id": id}
    r = requests.post(url, json=dici_corredor)
    lista = r.json()
    return True

#faca um função usando a bibli resquests
#que acessa a URL /corredores/maior_tempo do servidor de corredores
#via GET e devolve o dicionário do corredor com o maior tempo (mais lento)
def maior_tempo():
    #com quem vou me conectar?
    url = 'http://localhost:5000/corredores/maior_tempo'
    #conectar na URL usando o verbo GET
    r = requests.get(url)
    #a resposta é um dicionário, então não precisa fazer json()
    dici_corredor = r.json()
    return dici_corredor['nome']

#faça uma função usando a biblioteca requests
#que acessa a URL  /corredores/maior_tempo do servidor de corredores
#via DELETE que irá deletar o corredor mais lento
#infelizmente o servidor tem um bug no caso da lista
#de corredores estar vazia, então você deve tratar esse erro no cliente
#abaixo código sugerido pelo copilot
def deleta_mais_lento():
    #com quem vou me conectar?
    url = 'http://localhost:5000/corredores/maior_tempo'
    #conectar na URL usando o verbo DELETE
    try:
        r = requests.delete(url)
        if r.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException as e:
        print(f"Erro ao conectar: {e}")
        return False

#pq a funcionalidade anterior consiste em um erro
#de design no servidor corredores_server.py?
'''
o verbo DELETE não deveria retornar o corredor deletado, mas sim um status de sucesso ou falha.
isto é, o verbo DELETE deveria ser idempotente, ou seja, não deveria alterar o estado do servidor.
isto é, o primeiro delete deveria deletar o mais lento, mas a nova chamada delete não deveria fazer nada.
'''

#faça uma função usando a biblioteca requests
#que acessa a URL  /corredores/ID do servidor de corredores
#onde ID um código numerico
#o acesso ocorre via GET e deve retornar o nome do corredor em questão e 
#seu melhor tempo em uma tupla (nome, tempo)
def corredor_por_id(id):
    #com quem vou me conectar?
    url = f'http://localhost:5000/corredores/{id}'
    #conectar na URL usando o verbo GET
    r = requests.get(url)
    if r.status_code == 200:
        corredor = r.json()
        return (corredor['corredor']['nome'], corredor['corredor']['tempo'])
    else:
        return None, None
    
#FAÇA UMA FUNÇÃO USANDO A BIBLIOTECA REQUESTS
#que acessa a URL  /corredores/ID do servidor de corredores
#onde ID um código numerico
#o acesso ocorrerá via DELETE, causando a remoção do corredor mais lento
#este modo de deletar é indenpotente, ou seja, se o corredor não existir
#não deve causar erro, mas sim retornar um status de sucesso ou falha
def deleta_corredor_por_id(id):
    #com quem vou me conectar?
    url = f'http://localhost:5000/corredores/{id}'
    #conectar na URL usando o verbo DELETE
    r = requests.delete(url)
    if r.status_code == 404:
        return "corredor não encontrado"
    else:
        return "ok"
    
#faça uma função usando a biblioteca requests
#que acessa a URL  /corredores/ID do servidor de corredores
#onde ID um código numerico
#o acesso ocorrerá via PUT, e você deverá enviar um dicionário cm novo tempo
#para atualizar o tempo do corredor, caso contrário o servidor deve retornar um erro
def atualiza_corredor_por_id(id, novo_tempo):
    #com quem vou me conectar?
    url = f'http://localhost:5000/corredores/{id}'
    #conectar na URL usando o verbo PUT
    r = requests.put(url, json={"tempo": novo_tempo})
    if r.status_code == 400:
        return "Tempo não pode ser maior que o atual"
    if r.status_code == 404:
        return "corredor não encontrado"
    else:
        return "tempo atualizado com sucesso"