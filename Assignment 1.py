#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author Susannah Davenport
Python II
Pokemon
Prof. Auerbeck


Please read! I am sure you will be confused by the fact that there are only twenty or so (out of thousands) pokemon
that are being used. I began this assignment working on this Names section, and actually
got really far by using a completely different idea. That was when I noticed there were still discrepancies and odd
sections that wouldn't cooperate. I had to scratch the entire thing. I know this is a common thing to run into. By the time I got one column of information 
shaved down to fit the data in *another* column, I realized I was working with a lot of missing variables too. I know 
this looks ridiculous, but part of why I'm very excited for this part of Python (datbase management, etc) is because
I know it will come up in every day work if I am fortunate enough to land a job in the tech industry. Additionally, YOu had mentioned
during class that updating someTHING (even if we're unsure) is better than nothing
because you can at least see where I'm trying to go with it...'
"""

#I assigned the salvaged pokemon names with their corresponding information so that they could be called later on
Tentacool = ['Name: Tentacool, Index: 72, Locations: Kanto and Hoenn, Minimum Level: 20, Maximum Level: 30 ']
Wingull =['Name: Wingull , Index: 278 , Locations: Kanto and Hoenn, Minimim Level: 20, Maximum Level: 50']
Tentacruel =['Name: Tentacruel, Index:  73, Locations: Kanto, Hoenn, Sinnoh, Unova, Minimum Level: 15 , Maximum Level: 20 ']
Pelipper =['Name: Pelipper, Index: 279 , Locations: Kanto, Hoenn, Sinnoh, Unova Minimum Level: 20, Maximum Level: 50 ']
Finneon = ['Name: Finneon, Index: 456, Locations: Kanto Minimum Level: 40, Maximum Level: 40']
Magikarp =['Name: Magikarp, Index: 129, Locations: Kanto, Johto, Hoenn, Sinnoh, Unova,  Minimum Level: 7, Maximum Level:7 ']
Staryu =['Name: Staryu, Index: 120, Locations: Kanto and Sinnoh Minimum Level: 9, Maximum Level: 9']
Psyduck = ['Name:Psyduck , Index: 54, Locations: Johto, Minimum Level: 25, Maximum Level: 25']
Golduck = ['Name: Golduck , Index: 55, Locations: Kanto Minimum Level: 10 , Maximum Level: 25']
Barboach = ['Name: Barhoach, Index: 339 , Locations: Johto Minimum Level: 39, Maximum Level: 39']
Wiscash = ['Name: Wiscash , Index: 340 , Locations: Johto Minimum Level: 39, Maximum Level:39']
Gyarados = ['Name: Gyarados , Index: 130 , Locations: Kanto, Johto, Hoenn, Sinnoh, Minimum Level: 8, Maximum Level: 8']
Remoraid = ['Name: Remoaraid , Index: 223 , Locations: Hoenn, Sinnoh, Unova,  Minimum Level: 20, Maximum Level: 30']
Octillery = ['Name: Octillery, Index: 224, Locations:Hoenn, Sinnoh, Unova, Minimum Level: 20, Maximum Level: 30 ']
Mantyke = ['Name: Mantyke, Index: 458, Locations: Sinnoh Minimum Level: 40, Maximum Level: 40']
Luvdisc = ['Name: Luvdisc, Index:370 , Locations: Unova Minimum Level: 39, Maximum Level: 39']
Zubat = ['Name: Zubat , Index: 41, Locations: Kalos and Alola, Minimum Level: 20, Maximum Level: 30']
Onix = ['Name: Onix, Index: 95, Locations: Kalos and Alola, Minimum Level: 10, Maximum Level: 25']
Geodude = ['Name: Geodude , Index: 74 , Locations: Kalos and Alola,  Minimum Level: 10, Maximum Level: 25']
Lumineon = ['Name: Lumineon, Index: 457, Locations: Kanto, Minimum Level: 40 , Maximum Level: 40']
Poke_Profiles = [Tentacool, Wingull, Tentacruel, Pelipper, Finneon, Magikarp, Staryu, Psyduck, Golduck, Barboach, Wiscash, Gyarados, Remoraid, Octillery, Mantyke, Luvdisc, Zubat, Onix, Geodude, Lumineon]

print("Greetings! Please enter Name to search for a Pokemon by name")
name_answer = input() #putting user input into an object

while True:  #this is a simple while loop that breaks upon invalid input. I'm not pleased with the tediousness, so I'd like to know how I can boil down this type of process
    if name_answer == 'Tentacool':
        print(Tentacool)
    elif name_answer == 'Wingull':
        print(Wingull)
    elif name_answer == 'Tentacruel':
        print(Tentacruel)
    elif name_answer == 'Pelipper':
        print(Pelipper)
    elif name_answer == 'Finneon':
        print(Finneon)
    elif name_answer == 'Magikarp':
        print(Magikarp)
    elif name_answer == 'Staryu':
        print(Staryu)
    elif name_answer == 'Psyduck':
        print(Psyduck)
    elif name_answer == 'Golduck':
        print(Golduck)
    elif name_answer == 'Barboach':
        print(Barboach)
    elif name_answer == 'Wiscash':
        print(Wiscash)
    elif name_answer == 'Gyarados':
        print(Gyarados)
    elif name_answer == 'Remoraid':
        print(Remoraid)
    elif name_answer == 'Octillery':
        print(Octillery)
    elif name_answer == 'Mantyke':
        print(Mantyke)
    elif name_answer == 'Luvdisc':
        print(Luvdisc)
    elif name_answer == 'Zubat':
        print(Zubat)
    elif name_answer == 'Onix':
        print(Onix)
    elif name_answer == 'Geodude':
        print(Geodude)
    elif name_answer == 'Lumineon':
        print(Lumineon)
    else: 
        print("Invalid Pokémon name.")
    break  
    
    
    