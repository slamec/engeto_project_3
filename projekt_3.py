"""
projekt_3.py: třetí projekt do Engeto Online Python Akademie
author: Miroslav Kopecky
email: kopecky.mir@gmail.com
discord: Miro#8969

"""
from urllib import request
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
    city = soup.find_all(class_ = 'cislo')
    city_name = soup.find_all(class_ = 'overflow_name')
    
    for items in city:
        temp_list = [] 

        city_code = items.getText()
        link_obce = BASE_URL + items.find('a').get('href')
        temp_list.append(city_code)
        temp_list.append(link_obce)
        codes.append(temp_list)

    for items in city_name:
       city_name = items.getText()
       names.append(city_name)

def get_parties(url):
    """Scraps politican party name"""

    request = requests.get(url)
    soup = BeautifulSoup(request.content, 'html.parser')
    parties = soup.find_all(class_ = 'overflow_name')
    for items in parties:
        parties.append(items.getText())

def get_data(url):
    """Scraps data about: voters, envelopes, votes"""
    temp_list = []

    request = requests.get(url)
    soup = BeautifulSoup(request.content, 'html.parser')

    voters = soup.find(class_ = 'cislo', headers = 'sa2').getText()
    temp_list.append(int(voters.replace('\xa0', '')))

    envelopes = soup.find(class_= 'cislo', headers= 'sa3').getText()
    temp_list.append(int(envelopes.replace('\xa0', '')))

    votes = soup.find(class_= 'cislo' , headers= 'sa6').getText()
    temp_list.append(int(votes.replace("\xa0", '')))

    for number in range(1, 4):
        try:
            parties_count =  soup.find_all(class_= 'cislo', headers = f't{number}sa2 t{number}sb3')
            
            for items in parties_count:
                
                number = items.getText()
                temp_list.append(int(number.replace('\xa0', '')))
        except:
            continue #maybe trouble

    return temp_list