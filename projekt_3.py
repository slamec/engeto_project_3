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
parties = []
completed_list = []

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
        city_link = BASE_URL + items.find('a').get('href')
        temp_list.append(city_code)
        temp_list.append(city_link)
        codes.append(temp_list)

    for items in city_name:
       city = items.getText()
       names.append(city)

def get_parties(url):
    """Scraps politican party name"""

    request = requests.get(url)
    soup = BeautifulSoup(request.content, 'html.parser')
    party = soup.find_all(class_ = 'overflow_name')

    for items in party:
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
            continue #might be trouble

    return temp_list

# stazeni dat pro jednotlive obce
def data_by_city():

    cities = []

    print('Data is being downloaded. It might take few seconds...')
    
    get_parties(codes[1][1])

    for items in range(0, len(codes)):

        detail = []

        cities.extend(codes[items])
        cities.pop(1) # deletes hhtp

        detail = get_data(codes[items][1])

        cities.append(names[items])
        cities.extend(detail)
        
        completed_list.append(cities)

        cities = []

def save_data(data):
    """Save the scrapped data to a csv file"""

    temp_list = []

    temp_list.extend(HEADER)
    temp_list.extend(parties)

    print(f'Saving the data to {data}.')
    
    with open(data, "w", newline='', encoding='utf-8') as file:
        wr = csv.writer(file)

        wr.writerow(temp_list)
        wr.writerows(completed_list)

    print("Data has beed saved, see you next time.")

def main():
        url, data = load_parameters()
        load_city(url)
        data_by_city()
        save_data(data)

if __name__ == "__main__":
    main()