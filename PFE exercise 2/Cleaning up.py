#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Susannah
"""
import pandas as pd
#these are the dataframes after I had edited them and read them back into the file
p = pd.read_csv('./data/clean/pokemon.csv')
m = pd.read_csv('./data/clean/poke_moves.csv')
d = pd.read_csv('./data/clean/encounters.csv')
l = pd.read_csv('./data/clean/locations.csv')

# Merge DataFrames #I like the way this was done in class, but I could not
#figure out how to make it work in any other of my subsequent dataframes. I was very confused, even after looking at the notes on brightspace
pm = p.merge(m, how='left', left_on='id', right_on='pokemon_id', suffixes=('_poke', '_pokemoves'))
pmd = pm.merge(d, how='left', left_on='move_id', right_on='id', suffixes=('_pm', '_d'))

d[['pokemon_id','location_area_id']].drop_duplicates() #<<<<<This gives us pokemon_id and their locations from 'encounters'
p[['id','identifier']].drop_duplicates()#<<< from 'pokemon'

dp = d.merge(p) #merging "encounters" with "pokemon"
dp.drop_duplicates().dropna()
dp.info()

columns_to_drop = [['encounter_slot_id', 'species_id','height','weight','base_experience','order','is_default']]  # Replace with your specific column names
#Here I se the drop method to eliminate the specified columns
improved_dp = dp.drop(columns=columns_to_drop)
# Now df contains the DataFrame with specified columns I didn't want
improved_dp.info()
#now it has a new name


##this is all the cleaning and reading back into files in Spyder:

M = pd.read_csv('./data/orig/moves.csv')
M[['id','identifier','power']].drop_duplicates()

columns_to_drop = ['generation_id','type_id','pp','accuracy','priority','target_id','damage_class_id','effect_id','effect_chance','contest_type_id','contest_effect_id','super_contest_effect_id']
moves = M.drop(columns=columns_to_drop).dropna()
moves.to_csv('./data/clean/moves.csv')

m[['pokemon_id','move_id','level']].drop_duplicates()
pokemoves_column_drop = ['version_group_id','pokemon_move_method_id','order']
new_poke_moves = m.drop(columns=pokemoves_column_drop)
new_poke_moves.to_csv('./data/clean/poke_moves.csv')

p[['id','identifier']].drop_duplicates
poke_columns_drop = ['height','species_id','weight','base_experience','order','is_default']
clean_pokemon = p.drop(columns = poke_columns_drop)
p = p.rename(columns={'id': 'Index ID'})
p = p.rename(columns={'identifier': 'Name'})

clean_pokemon.to_csv('./data/clean/pokemon.csv')


d[['id','location_area_id','pokemon_id','min_level','max_level']]
things_to_drop = ['version_id','encounter_slot_id']

new_encounters = d.drop(columns = things_to_drop)

new_encounters.to_csv('./data/clean/encounters.csv')

print(moves)
print(improved_dp)






















