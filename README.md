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

Output data:
```City code,City name,Voters,Envelopes,Valid votes,Občanská demokratická strana,Řád národa - Vlastenecká unie,CESTA ODPOVĚDNÉ SPOLEČNOSTI,Česká str.sociálně demokrat.,Radostné Česko,STAROSTOVÉ A NEZÁVISLÍ,Komunistická str.Čech a Moravy,Strana zelených,"ROZUMNÍ-stop migraci,diktát.EU",Strana svobodných občanů,Blok proti islam.-Obran.domova,Občanská demokratická aliance,Česká pirátská strana,Unie H.A.V.E.L.,Referendum o Evropské unii,TOP 09,ANO 2011,Dobrá volba 2016,SPR-Republ.str.Čsl. M.Sládka,Křesť.demokr.unie-Čs.str.lid.,Česká strana národně sociální,REALISTÉ,SPORTOVCI,Dělnic.str.sociální spravedl.,Svob.a př.dem.-T.Okamura (SPD),Strana Práv Občanů
529303,Benešov,13104,8485,8437,1052,10,2,624,3,802,597,109,35,112,6,11,948,3,6,414,2577,3,21,314,5,58,17,16,682,10
532568,Bernartice,191,148,148,4,0,0,17,0,6,7,1,4,0,0,0,7,0,0,3,39,0,0,37,0,3,0,0,20,0
530743,Bílkovice,170,121,118,7,0,0,15,0,8,18,0,2,0,0,0,3,0,0,2,47,1,0,6,0,0,0,0,9,0
532380,Blažejovice,96,80,77,6,0,0,5,0,3,11,0,0,3,0,0,5,1,0,0,29,0,0,6,0,0,0,0,8,0```
