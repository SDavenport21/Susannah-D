#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: Susannah
This is an attempt to find a pokemon from searching by region.
I wasn't able to get past the last level--seeing the pokemon by name in those regions
I tried a hundred different ways to get the pokemon id to line up with the names
so that I could finish this. '
"""

import pandas as pd


p = pd.read_csv('./data/orig/pokemon.csv')
m = pd.read_csv('./data/orig/poke_moves.csv')
d = pd.read_csv('./data/orig/encounters.csv')
l = pd.read_csv('./data/orig/locations.csv')




#I was happy with this, actually >>>Grouping by 'region_id' and aggregating 'identifier' values as a list
grouped = l.groupby('region_id')['identifier'].agg(list).reset_index()

print(grouped) #making sure grouped is an onject that'll give me everything grouped appropriately

print('Enter a number between 1.0 and 8.0. Please be sure to include your zero!')
#I wished I could get the numbers down to 1 and not 1.0, but there wasn't
#really an easy way to go about doing it without
#disrupting all of my code
num_selected = input()

if num_selected == '1.0':
   print("This region is called Kanto. Enter 'Cities' to see the cities in Kanto")

   city_answer = input()
  
   if city_answer == 'Cities':
       kanto_cities = grouped[grouped['region_id'] == 1]['identifier'].tolist()
       print('Cities in Kanto:', kanto_cities)
 #Region to cities, again and again and again      
       
elif num_selected == '2.0':
    print("This region is called Johto. Enter 'Cities' to see the cities in 'Johto")
    
    city_answer = input()
    
    if city_answer == 'Cities':
        Johto_cities = grouped[grouped['region_id'] == 1]['identifier'].tolist()
        print('Cities in Johto:', Johto_cities)
    
elif num_selected == '3.0':
    print("This region is called Hoenn. Enter 'Cities' to see the cities in 'Hoenn")
    
    city_answer = input()
    
    if city_answer == 'Cities':
        hoenn_cities = grouped[grouped['region_id'] == 1]['identifier'].tolist()
        print('Cities in Hoenn:', hoenn_cities)    
    
elif num_selected == '4.0':
        print("This region is called Sinna. Enter 'Cities' to see the cities in 'Sinnah")
        
        city_answer = input()
        
        if city_answer == 'Cities':
            Sinnah_cities = grouped[grouped['region_id'] == 1]['identifier'].tolist()
            print('Cities in Sinnah:', Sinnah_cities)

elif num_selected == '5.0':
    print("This region is called Unova. Enter 'Cities' to see the cities in 'Unova")
    
    city_answer = input()
    
    if city_answer == 'Cities':
        Unova_cities = grouped[grouped['region_id'] == 1]['identifier'].tolist()
        print('Cities in Unova:', Unova_cities)        
    
    
elif num_selected == '6.0':
    print("This region is called Kalos. Enter 'Cities' to see the cities in 'Kalos")
    
    city_answer = input()
    
    if city_answer == 'Cities':
        Kalos_cities = grouped[grouped['region_id'] == 1]['identifier'].tolist()
        print('Cities in Kalos:', Kalos_cities)    
    
    
    
elif num_selected == '7.0':
        print("This region is called Alola. Enter 'Cities' to see the cities in 'Alola")
        
        city_answer = input()
        
        if city_answer == 'Cities':
            Alola_cities = grouped[grouped['region_id'] == 1]['identifier'].tolist()
            print('Cities in Alola:', Alola_cities)
            
            
            
elif num_selected == '8.0':
      print("This region is called Galar. Enter 'Cities' to see the cities in 'Galar")
                
      city_answer = input()
                
      if city_answer == 'Cities':
         Galar_cities = grouped[grouped['region_id'] == 1]['identifier'].tolist()
         print('Cities in Galar:', Galar_cities)
  
##this was where I got lost. Again, finishing these segments of code is a major weak
#point for me.           
else:
    print("Let's try to find some pokemon in these cities! Enter 'keep going'")        
           
    city_answer = input()


if city_answer == 'keep going':
    print("Great! Type in a pokemon name")
    poke_answer = input()

    if poke_answer in p['identifier'].values:
        corresponding_id = p.loc[p['identifier'] == [poke_answer], 'id'].iloc[0]
        print("This pokemon's ID is " + corresponding_id + "and usually can be found in these cities.")
    else:
        print("Please try again")

























            
            
            
            