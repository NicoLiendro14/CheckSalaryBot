import requests
import json
import datetime
from bs4 import BeautifulSoup


def get_salary(input_salary):
    ret = get_response_salary(input_salary)
    json_ret = json.loads(ret.content)
    return json_ret['quoteData']['destinationAmount']


def get_response_salary(input_salary):
    url = "https://ya5w5myk2j.execute-api.us-east-1.amazonaws.com/prod/quote/external?originRoute=134&destinationRoute=86&amount=" + input_salary + "&way=origin"
    ret = requests.get(url)
    return ret


def convert_salary(salary):
    float_salary = float(salary)
    converted_salary = '${:,.2f}'.format(float_salary)
    return converted_salary


def get_dolar_blue():
    url = "https://www.dolarhoy.com/cotizaciondolarblue"
    ret = requests.get(url)
    html_doc = ret.text
    soup = BeautifulSoup(html_doc, 'html.parser')
    info = soup.find_all("span", {"class": "pull-right"})
    lista_dolar = []
    for inpu in info:
        dolar = inpu.contents[0]
        lista_dolar.append(dolar)
    return lista_dolar


def get_dolar_oficial():
    url = "https://www.dolarhoy.com/"
    ret = requests.get(url)
    html_doc = ret.text
    soup = BeautifulSoup(html_doc, 'html.parser')
    info = soup.find_all("td", {"class": "number"})
    lista_dolar = []
    cont = 0
    for inpu in info:
        if cont < 2:
            dolar = inpu.contents[0]
            lista_dolar.append(dolar)
            cont += 1
        else:
            break
    return lista_dolar


def get_all_dolars():
    lista_dolar_oficial = get_dolar_oficial()
    lista_dolar_blue = get_dolar_blue()
    for dolar in lista_dolar_blue:
        lista_dolar_oficial.append(dolar)
    return lista_dolar_oficial


if __name__ == '__main__':
    salary = get_salary("550000")
    convert_salary(salary)
