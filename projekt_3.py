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

HEADER = ["City code","City name","Voters","Envelopes", "Valid votes"]
BASE_URL = "https://volby.cz/pls/ps2017nss/"


def load_parameters():
    """Loads parameters from the command line a save them to a list"""

    parameters = sys.argv

    if len(parameters) != 3:

        print("Not enough parameters. Program has been terminated!")

    elif "https://volby.cz/pls/ps2017nss/" not in parameters[1]:

            print("First input must be a link.")

    elif ".csv" not in parameters[2]:

            print("Name of the out file has not been inserted.")
    else:

        return parameters[1], parameters[2]