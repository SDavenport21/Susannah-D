#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author Susannah Davenport
Python II
Pokemon
Prof. Auerbeck


*Please read this first:

I split up the two sections of the assignment (search by region/serch by name)
because I couldn't figure out how to tie the two together. I know it's not exactly right
but I am here to learn!

Comments explain everything below

"""





## These objects (Poke_Kanto, Poke_Johto, etc) were taken from encounters and locations. I used the common variable of the region id (1-8)
#I later realized that Locations did not have a location id 8.
##The Cities objects contain lists copy and pasted directly from the csv file
##That was the only way I could get the city names to load into objects. I kept getting errors, which made no sense so I imporvised.
Poke_Kanto = ['tentacool'
,'wingull'
,'tentacruel'
,'pelipper'
,'finneon'
,'magikarp'
,'gyarados'
,'lumineon'
,'staryu']

Poke_Johto = ['psyduck'
,'golduck'
,'magikarp'
,'barboach'
,'whiscash'
,'gyarados']

Poke_Hoenn = ['tentacool', 'wingull','tentacruel','pelipper','remoraid','magikarp','remoraid','gyarados','octillery']

Cities_of_Kanto = ['pallet-town','rock-tunnel','kanto-route','kanto-sea-route','celadon-city','cerulean-city','cinnabar-island','mt-moon','digletts-cave','fuchsia-city','seafoam-islands','cerulean-cave','vermilion-city','kanto-victory-road'
,'viridian-city'
,'viridian-forest'
,'power-plant'
,'pokemon-tower'
,'pokemon-mansion'
,'kanto-safari-zone'
,'pewter-city'
,'lavender-town'
,'indigo-plateau'
,'saffron-city'
,'monean-chamber'
,'liptoo-chamber'
,'weepth-chamber'
,'dilford-chamber'
,'scufib-chamber'
,'rixy-chamber'
,'viapos-chamber'
,'ss-anne'
,'mt-ember'
,'berry-forest'
,'icefall-cave'
,'pattern-bush'
,'lost-cave'
,'kindle-road'
,'treasure-beach'
,'cape-brink'
,'bond-bridge'
,'three-isle-port'
,'resort-gorgeous'
,'five-isle-meadow'
,'memorial-pillar'
,'outcast-island'
,'green-path'
,'water-path'
,'trainer-tower'
,'canyon-entrance'
,'sevault-canyon'
,'tanoby-ruins'
,'one-island'
,'five-island'
,'kanto-altering-cave']


Johto_cities = ['johto-route'
,'ruins-of-alph'
,'slowpoke-well'
,'sprout-tower'
,'bell-tower'
,'tohjo-falls'
,'union-cave'
,'unknown-all-poliwag'
,'unknown-all-rattata'
,'unknown-all-bugs'
,'violet-city'
,'whirl-islands'
,'azalea-town'
,'goldenrod-city'
,'mahogany-town'
,'johto-lighthouse'
,'team-rocket-hq'
,'goldenrod-tunnel'
,'mt-silver-cave'
,'pokeathlon-dome'
,'ss-aqua'
,'safari-zone-gate'
,'cliff-cave'
,'frontier-access'
,'bellchime-trail'
,'sinjoh-ruins'
,'embedded-tower'
,'pokewalker'
,'cliff-edge-gate'
,'radio-tower']

Cities_of_Hoenn = ['petalburg-city','slateport-city','lilycove-city','mossdeep-city'
,'sootopolis-city'
,'ever-grande-city'
,'meteor-falls'
,'rusturf-tunnel'
,'granite-cave'
,'petalburg-woods'
,'jagged-pass'
,'fiery-path'
,'mt-pyre'
,'seafloor-cavern'
,'cave-of-origin'
,'hoenn-victory-road'
,'shoal-cave'
,'new-mauville'
,'abandoned-ship'
,'sky-pillar'
,'hoenn-route'
,'hoenn-safari-zone'
,'dewford-town'
,'pacifidlog-town'
,'magma-hideout'
,'mirage-tower'
,'desert-underpass'
,'artisan-cave'
,'hoenn-altering-cave']

Sinnoh_cities = ['canalave-city'
,'eterna-city'
,'pastoria-city'
,'sunyshore-city'
,'sinnoh-pokemon-league'
,'oreburgh-mine'
,'valley-windworks'
,'eterna-forest'
,'fuego-ironworks'
,'mt-coronet'
,'great-marsh'
,'solaceon-ruins'
,'sinnoh-victory-road'
,'ravaged-path'
,'oreburgh-gate'
,'stark-mountain'
,'spring-path'
,'turnback-cave'
,'snowpoint-temple'
,'wayward-cave'
,'ruin-maniac-cave'
,'trophy-garden'
,'iron-island'
,'old-chateau'
,'lake-verity'
,'lake-valor'
,'lake-acuity'
,'valor-lakefront'
,'acuity-lakefront'
,'sinnoh-route-201'
,'lost-tower'
,'twinleaf-town'
,'celestic-town'
,'resort-area'
,'sandgem-town'
,'floaroma-town'
,'solaceon-town'
,'jubilife-city'
,'oreburgh-city'
,'hearthome-city'
,'veilstone-city'
,'snowpoint-city'
,'spear-pillar'
,'pal-park'
,'amity-square'
,'floaroma-meadow'
,'fullmoon-island'
,'sendoff-spring'
,'flower-paradise'
,'maniac-tunnel'
,'galactic-hq'
,'verity-lakefront'
,'newmoon-island'
,'sinnoh-battle-tower'
,'fight-area'
,'survival-area'
,'seabreak-path'
,'sinnoh-hall-of-origin-1'
,'sinnoh-hall-of-origin-2'
,'verity-cavern'
,'valor-cavern'
,'acuity-cavern'
,'jubilife-tv'
,'poketch-co'
,'trainers-school'
,'mining-museum'
,'sinnoh-flower-shop'
,'sinnoh-cycle-shop'
,'contest-hall'
,'poffin-house'
,'sinnoh-foreign-building'
,'pokemon-day-care'
,'veilstone-store'
,'sinnoh-game-corner'
,'canalave-library'
,'vista-lighthouse'
,'sunyshore-market'
,'footstep-house'
,'sinnoh-cafe'
,'grand-lake'
,'sinnoh-restaurant'
,'battle-park'
,'battle-frontier'
,'battle-factory'
,'battle-castle'
,'battle-arcade'
,'battle-hall'
,'distortion-world'
,'sinnoh-global-terminal'
,'sinnoh-villa'
,'battleground'
,'rotoms-room'
,'tg-eterna-bldg'
,'iron-ruins'
,'iceberg-ruins'
,'rock-peak-ruins'
]

Cities_of_Unova = ['unova-mystery-zone'
,'unova-faraway-place'
,'nuvema-town'
,'accumula-town'
,'striaton-city'
,'nacrene-city'
,'castelia-city'
,'nimbasa-city'
,'driftveil-city'
,'mistralton-city'
,'icirrus-city'
,'opelucid-city'
,'unova-route-1'
,'dreamyard'
,'pinwheel-forest'
,'desert-resort'
,'relic-castle'
,'cold-storage'
,'chargestone-cave'
,'twist-mountain'
,'dragonspiral-tower'
,'unova-victory-road'
,'lacunosa-town'
,'undella-town'
,'anville-town'
,'unova-pokemon-league'
,'ns-castle'
,'royal-unova'
,'gear-station'
,'battle-subway'
,'musical-theater'
,'black-city'
,'white-forest'
,'unity-tower'
,'wellspring-cave'
,'mistralton-cave'
,'rumination-field'
,'celestial-tower'
,'moor-of-icirrus'
,'unova-shopping-mall'
,'challengers-cave'
,'poke-transfer-lab'
,'giant-chasm'
,'liberty-garden'
,'p2-laboratory'
,'skyarrow-bridge'
,'driftveil-drawbridge'
,'tubeline-bridge'
,'village-bridge'
,'marvelous-bridge'
,'entralink'
,'abundant-shrine'
,'undella-bay'
,'lostlorn-forest'
,'trial-chamber'
,'guidance-chamber'
,'entree-forest'
,'accumula-gate'
,'undella-gate'
,'nacrene-gate'
,'castelia-gate'
,'nimbasa-gate'
,'opelucid-gate'
,'black-gate'
,'white-gate'
,'bridge-gate'
,'route-gate'
,'abyssal-ruins']



Cities_of_Kalos = ['vaniville-town,kalos-route-1,vaniville-pathway,aquacorde-town,avance-trail,santalune-forest,ouvert-way,santalune-city,parterre-way,lumiose-city,prism-tower,lysandre-labs,versant-road,camphrier-town,shabboneau-castle, palais-lane, parfum-palace,rivière-walk,cyllage-city,muraille-coast,ambrette-town,spikes-passag,battle-chateau ,menhir-trail,geosenge-town,miroir-way,reflection-cave,shalour-city,tower-of-mastery,fourrage-road,coumarine-city,lumiose-badlands,laverre-nature-trail,laverre-city,poke-ball-factory,brun-way,dendemille-town,melancolie-path,frost-cavern,mamoswine-road,anistar-city,vallee-etroite-way,couriway-town,grande-vallee-way,snowbelle-city,winding-woods,detourner-way,kalos-victory-road,kalos-pokemon-league,kiloude-city,battle-maison,azure-bay,dendemille-gate,couriway-gate,ambrette-gate,lumiose-gate,shalour-gate,coumarine-gate,laverre-gate,anistar-gate,snowbelle-gate']

Cities_of_Alola =['alola-route ,kalae-bay,melemele-sea,hauoli-city--beachfront,hauoli-city--shopping-district,hauoli-city--marina,iki-town,mahalo-trail,mahalo-trail--plank-bridge,ruins-of-conflict,ten-carat-hill,ten-carat-hill--farthest-hollow,hauoli-cemetery,melemele-meadow,seaward-cave,berry-fields,verdant-cavern--trial-site,verdant-cavern--totems-den,hano-grand-resort,hano-beach,akala-meadow,paniola-town,heahea-city,konikoni-city,royal-avenue,memorial-hill,,paniola-ranch,wela-volcano-par,wela-volcano-park--totems-den,brooklet-hill,brooklet-hill--totems-den,lush-jung,ruins-of-life,akala-outskirts,digletts-tunnel,battle-royal-dome,secluded-shore,tapu-village,haina-desert,ulaula-meado,po-town,malie-city,malie-garden,mount-hokulani']

###Now, for each region (1-7) and all of the pokemon found in their respective regions are ready to work with

print('Greetinigs! I see you wish to collect some information. Please enter Region to search by region, or enter Name to search by name')
user_selection = input().strip() #Taking user input, moving onward into if, elif, and else
if user_selection == 'Region': #If the user inputs one of the seven regions, they will be shown a list to choose from 
    print("Excellent! Please choose from the following: Kanto, Johto, Hoenn, Sinnoh, Unova, Kalos, Alola, Galar")
    region_answer = input().strip() ##stripping away white space for my following code

    if region_answer == 'Kanto':
        print('There are a variety of cities in Kanto. If you would like to view them, please input "View". Otherwise, type "Move on"')
        region_answer = input().strip()

        if region_answer == 'View':
            print("The cities in Kanto are: " + ', '.join(Cities_of_Kanto) + ' Type the word "Pokemon" if you want to know which Pokemon are found in Kanto.')
            #concatenating string with an object containing certain city names using .join() and then I prompt user to input Pokemon if they want to know more
            poke_answer = input().strip().sort() ##added .sort() to return the pokemons in alphabetical order
            
            if poke_answer == 'Pokemon':
                print('These are the Pokemon usually found in the cities of Kanto: Tentacool, Wingull, Tentacruel, Pelipper, Finneon, Magikarp, Gyarados, Lumineon, Staryu.')

        elif region_answer == 'Move on':
         
            pass #making sure there is no weird nonsense to backfire on me
                  #I tested this pretty thoroughly but if any issues arise I would very much like to know so that I can improve my code  
    elif region_answer == 'Johto': ##here you will see the exact same process repeated for 7 regions. Yay! Search by region!
    
        print('There are a variety of cities in Johto. If you would like to view them, please input "View". Otherwise, type "Move on"')
        region_answer = input().strip()

        if region_answer == 'View':
            print("The cities in Johto are: " + ', '.join(Johto_cities))
            print('Type the word "Pokemon" if you want to know which Pokemon are found in Johto.')

            poke_answer = input().strip().sort()

            if poke_answer == 'Pokemon':
                print('These are the Pokemon usually found in the cities of Johto: Psyduck, Golduck, Magikarp, Barboach, Whiscash, Gyarados.')
    elif region_answer == 'Hoenn':
        print('There are a variety of cities in Hoenn If you would like to view them, please input "View". Otherwise, type "Move on"')
        region_answer = input().strip()

        if region_answer == 'View':
            print("The cities in Hoenn are: " + ', '.join(Cities_of_Hoenn))
            print('Type the word "Pokemon" if you want to know which Pokemon are found in Hoenn.')
            poke_answer = input().strip().sort()
            
            if poke_answer == 'Pokemon':
                print('These are the Pokemon usually found in the cities of Hoenn: Tentacool, wingull,tentacruel,pelipper,remoraid,magikarp,remoraid''gyarados''octillery')

        elif region_answer == 'Move on':
            pass

    elif region_answer == 'Sinnoh':
        print('There are a variety of cities in Sinnoh. If you would like to view them, please input "View". Otherwise, type "Move on"')
        region_answer = input().strip()

        if region_answer == 'View':
            print("The cities in Johto are: " + ', '.join(Sinnoh_cities))
            print('Type the word "Pokemon" if you want to know which Pokemon are found in Sinnoh.')

            poke_answer = input().strip().sort()

            if poke_answer == 'Pokemon':
                print('These are the Pokemon usually found in the cities of Sinnoh: Tentacruel, pelipper, mantyke,magikarp, remoraid,gyarados,staryu,octillery')

    elif region_answer == 'Unova':
        print('There are a variety of cities in Unova If you would like to view them, please input "View". Otherwise, type "Move on"')
        region_answer = input().strip()

        if region_answer == 'View':
            print("The cities in Unova are: " + ', '.join(Cities_of_Unova))
            print('Type the word "Pokemon" if you want to know which Pokemon are found in Hoenn.')
            poke_answer = input().strip().sort()
            
            if poke_answer == 'Pokemon':
                print('These are the Pokemon usually found in the cities of Unova: pelipper, tentacruel, magikarp, remoraid, gyarados, octillery, luvdisc')

        elif region_answer == 'Move on':
            pass
        
    elif region_answer == 'Kalos':
        print('There are a variet of cities in Kalos. If you would like to view them, please input "View".Otherwise, type "Move on"')
        region_answer = input().strip()
        
        if region_answer == 'View':
            print("The cities in Kalos are: " ', '.join(Cities_of_Kalos))
            print('Type the word "Pokemon" if you want to know which Pokemon are found in the cities of Kalos.')
            poke_answer = input().strip().sort()
            
            if poke_answer == 'Pokemon':
                print('These are the Pokemon usually found in the cities of Kalos: Zubat , Geodude , Onix')
    elif region_answer == 'Alola':
        print('There are a variety of cities in Alola. If you would like to view them, please input "View". Otherwise, type "Move on"')
        
        region_answer = input().strip()

        if region_answer == 'View':
            print("The cities in Alola are: " + ', '.join(Cities_of_Alola))
            print('Type the word "Pokemon" if you want to know which Pokemon are found in Sinnoh.')

            poke_answer = input().strip().sort()

            if poke_answer == 'Pokemon':
                print('These are the Pokemon usually found in the cities of Alola: Geodude, zubat, onix')



