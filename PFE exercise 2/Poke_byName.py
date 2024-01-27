#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


@author: Susannah
"""

import pandas as pd
p = pd.read_csv('./data/clean/pokemon.csv')
m = pd.read_csv('./data/clean/poke_moves.csv')
d = pd.read_csv('./data/clean/encounters.csv')
l = pd.read_csv('./data/clean/locations.csv')

pm = p.merge(m, how='left', left_on='id', right_on='pokemon_id', suffixes=('_poke', '_pokemoves'))
pmd = pm.merge(d, how='left', left_on='move_id', right_on='id', suffixes=('_pm', '_d'))

moves = m[['pokemon_id','move_id','level']].drop_duplicates().dropna()
d[['pokemon_id','location_area_id']].drop_duplicates() #<<<<<This gives us pokemon_id and their locations from 'encounters'
p[['id','identifier']].drop_duplicates()#

dp = d.merge(p)
dp.drop_duplicates().dropna()
dp.info()
#print(dp)

moves.drop_duplicates()
#print(moves.info())


m.drop_duplicates()


print("Type a Pokémon name:")
name = input()

while True:
    if name in dp['identifier'].values:
        result = dp[dp['identifier'] == name]
        for col, value in result.iloc[0].items():
            #result.iloc gives me all the items in the first row. 
            #if it had been result.iloc[3], i would have gotten the
            #info from the third row.
            print(f"{col}: {value}") #gives me the column and the value(s)
            
        
    else:
        print(f"The Pokémon '{name}' does not exist in the dataframe.")
        break

    print("\nType another Pokémon name (or type 'Moves' to see what your Pokemon has:")
    name = input()

    if name == 'Moves':
        ### I had to stop here. I wasn't able to continue. 
        break























    
