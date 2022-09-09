Third engeto project - elections scraper
# Project description
This script scraps elections data from this page [here.](https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103) 

# Libraries install
Libraries can be installed to a new virtual environment. To install all necessary libraries use the ```requirements.txt``` file. To install libraries use this command:

```pip install -r requirements.txt```

# Run the script
To run the the script use ```python projekt_3.py```. Example below (script, link, output file name):

```python projekt_3.py 'https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101' 'election_data.csv'```

DO NOT FORGET TO USE TWO ARGUMENTS! 

Data download and saving: 

```Data is being downloaded. It might take few seconds...```

```Saving the data to 'election_data.csv'.```

```Data has beed saved, see you next time.```

Output data (partial):

```City code,City name,Voters,Envelopes,Valid votes,Občanská demokratická strana...```
```532568,Bernartice,191,148,148,4,0,0,17,0,6,7,1,4,0,0,0,7,0,0,3,39,0,0,37,0,3,0,0,20,0
530743,Bílkovice,170,121,118,7,0,0,15,0,8,18,0,2,0,0,0,3,0,0,2,47,1,0,6,0,0,0,0,9,0
532380,Blažejovice,96,80,77,6,0,0,5,0,3,11,0,0,3,0,0,5,1,0,0,29,0,0,6,0,0,0,0,8,0
```
