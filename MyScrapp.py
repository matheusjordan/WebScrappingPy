import requests
from bs4 import BeautifulSoup
import lxml

url = "https://widget.coinlib.io/widget?type=full_v2&theme=light&cnt=10&pref_coin_id=3315&graph=no"

#Se conecta com a url
r = requests.get(url)

#Retorna o html do site
soup = BeautifulSoup(r.content, 'lxml')

#Retorna a tag TABLE que possi a CLASS : table coinlist
table = soup.find('table', attrs={'class':'table coinlist'})

#Retorna a tag TBODY que está dentro da tag TABLE
tbody = table.find('tbody')

#Retorna uma lista com todas as tags TR dentro do tbody
tr_list = tbody.find_all('tr')

#Loop que percorre todos as tags TR em tr_list
for tr in tr_list:

    #Retorna uma lista com todas as tags TD que possuem CLASS : ''
    td_list = tr.find_all('td', attrs={'class':''})

    #Retorna o conteúdo que está dentro  do atributo coin_id
    coin_id = tr['coin_id']

    #Loop que percorre todas as tags TD em td_list
    for td in td_list:

        #Retorna a tag DIV que possui a CLASS : tbl-currency -> Div que contêm o nome das cryptomoedas
        div_name = td.find('div', attrs={'class':'tbl-currency'})
        
        span_price = td.find('span', attrs={'class':f'tbl-price avgprice-{coin_id} price'})

        #Condicional que verifica se o o conteudo da variavel DIV é vazio ou nulo
        if(div_name):

            #Retorna a tag A
            a = div_name.find('a')
            
            #Retorna o conteudo da tag A
            coin_name = a.get_text()

            print('name:',coin_name)
        
        else:
            coin_price = span_price.get_text()
            print('price:',coin_price,'\n')