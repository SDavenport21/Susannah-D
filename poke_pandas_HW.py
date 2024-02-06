""""PFE
Professor Auerbeck

Pokemon!!
@author: Susannah
Adding on to Pokemon: a big and fancy while loop for teammate 
list manipulation! This was fun! (Matching indents was not.)
"""

import pandas as pd

p = pd.read_csv('data/orig/pokemon.csv')

team = []

while True:
    n = input("Welcome! What would you like to do:\n\n\t1) Build my own Pokemon team\n\n\t2) Generate a random team\n\n\t3) Exit program\n\ninput: ")
    
    if int(n) == 1:
        t = input("Who is your teammate? ")
        
        if p.loc[p['identifier'] == t].empty: #pandas checking the contents of 'identifier'
            print("Invalid Pokemon Name. Try again")
        else:
            if t in team: #if teammate is already in this team, return that it's already been added
                print(t + ' has already been added to your team!')
            else:
                print("Great! " + t + " has been added to your team!")
                team.append(t)

            if len(team) >= 6: #a concise way to track how many spots are left on the team
                print("You have now registered the maximum amount of teammates. Their names are " + ', '.join(team))
                break

    elif int(n) == 2:
        # user's second input "create random team"
        random_team = p.sample(n=6)['identifier']  # six possible names from the 'identifier' sample
        team_poke = random_team.tolist()
        count = 1
        print("Here are the members of your team: ")
        for pokemon in team_poke:
            print(f"{count}. {pokemon}") # a nice, refined way of listing stuff in rows
            count += 1
##The thing that is missing in this part of the script is the option to delete a name. I tried adding the option to delete with
#input stored in 'v' however, it seemed that every time I ran the code (even with matching indentation) I got some
#type of error. In theory, I thought that adding the option to delete a teammate would fit in well with the z or xy inputs--easy to remember/type/manipulate.
# I thought also that it could fit within the confines of the while loop. I tried it inside and outside the loops with no success
#I would really like to know what you would suggest, and also what sort of tactic (or technique?) that could be useful in future homeworks
#
        while True:  # This is a new while loop contained in the int(n)==2 section of code.
            z = input("Enter the name of a teammate you wish to move to another position in the list\ninput: ")
            xy = input("Where do you want to rank " + z + "? Please enter a number 1-6\ninput: ")
            # stored the NAME in z and stored the DIGIT (1-6) in xy
            if xy.isdigit():
                xy = int(xy)
                if 1 <= xy <= 6:
                    # if the entered digit is between 1 and six, the name gets put into its proper place
                    index = team_poke.index(z)
                    if xy - 1 == index:
                        # if the digit is equal to the teammate's current spot, try again!
                        print("This Pokemon is already in that spot. Please choose a different position.")
                        continue

                    nix = team_poke.pop(index)
                    # Here I used the index of the Pokemon to pop (or nix) it from the list
                    team_poke.insert(xy - 1, nix)
                    # I had to adjust xy to be a valid index in python, indexes start at 0 and not 1
                    print(team_poke)
                else:
                    print("Invalid input. Enter a valid number")  # wrapping up my conditionals
            else:
                print("That isn't a valid position. Please use 1-6")  # this part took forever to get right

            opt_out = input("Would you like to change the order of your team again? (y/n) ")
            # if we're done with messing around the teammate index, we can get out
            if opt_out == 'n':
                print("Goodbye!")


    elif int(n) == 3:
        # if the user enters 3 at the beginning of the script, this is what will be printed
        print("Goodbye!")
        break
