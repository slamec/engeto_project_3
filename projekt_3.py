"""
projekt_3.py: třetí projekt do Engeto Online Python Akademie
author: Miroslav Kopecky
email: kopecky.mir@gmail.com
discord: Miro#8969

"""
from bs4 import BeautifulSoup
import requests
import sys
import csv

codes = []
names = []
completed_list = []
parties = []

HEADER = ['City code','City name','Voters','Envelopes', 'Valid votes']
BASE_URL = 'https://volby.cz/pls/ps2017nss/'


def load_parameters():
    """Loads parameters from the command line a save them to a list"""

    parameters = sys.argv

    if len(parameters) != 3:

        print('Not enough parameters. Program has been terminated!')

    elif 'https://volby.cz/pls/ps2017nss/' not in parameters[1]:

            print('First input must be a link.')

    elif '.csv' not in parameters[2]:

            print('Name of the out file has not been inserted.')
    else:

        return parameters[1], parameters[2]

def load_city(url):
    """Loads all cities from particular county and save to a list"""

    request = requests.get(url)
    soup = BeautifulSoup(request.content, 'html.parser')
    city = soup.find_all(class_= 'cislo')
    city_name = soup.find_all(class_= 'overflow_name')
    
    for items in city:
        temp_list= [] 

        city_code = items.getText()
        link_obce = BASE_URL + items.find('a').get('href')
        temp_list.append(city_code)
        temp_list.append(link_obce)
        codes.append(temp_list)

    for items in city_name:
       city_name = items.getText()
       names.append(city_name)