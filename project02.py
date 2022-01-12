#!/usr/bin/env python3

#Read Data Project

import csv 
 
Bulbasaur = 0
Squirtle = 0
Charmander = 0
Chikorita = 0
Cyndaquil = 0
Totodile = 0


while True:
    list = ["Bulbasaur", "Squirtle", "Charmander", "Chikorita", "Cyndaquil", "Totodile"] 
    print("\nWho is your favorite starter Pokemon?")
    print("[Gen 1]")    
    print(list[0])
    print(list[1])
    print(list[2])
    print("[Gen 2]")
    print(list[3])
    print(list[4])
    print(list[5])
    

    response = input(" - ")
    if response == "Bulbasaur":
        Bulbasaur += 1
        break
    elif response == "Squirtle":
        Squirtle += 2
        break
    if response == "Charmander":
        Charmander += 3
        break
    elif response == "Chikorita":
        Chikorita += 4
        break
    if response == "Cyndaquil":
        Cyndaquil += 5
        break
    elif response == "Totodile":
        Totodile += 6
        break
    else:
        print("Invalid Answer")
        break

    
while True:
    list = [">Type 1", ">HP", ">Attack", ">Defense", ">Sp. Atk", ">Sp. Def"]
    for x in list:
        print(x)
    


    if Bulbasaur > Squirtle:
        answer2= input("What would you like to know about Bulbasaur? -")
        break
    if Squirtle > Charmander:
        answer2=input("What would you like to know about Squirtle? -")
        break
    if Charmander > Chikorita:
        answer2=input("What would you like to know about Charmander? -")
        break
    if Chikorita > Cyndaquil:
        answer2=input("What would you like to know about Chikorita? -")
        break
    if Cyndaquil > Totodile:
        answer2=input("What would you like to know about Cyndaquil? -")
        break
    if Totodile > Bulbasaur:
        answer2=input("What would you like to know about Totodile? -")
    else:
        print("Invalid Answer")
        break

# response= name of the pokemon
# answer2= attack, hp, whatever

with open("pokedex.txt") as pokedata:
    for pokedict in csv.DictReader(pokedata):
        if pokedict["Name"] == response:
            if pokedict["Type 1"]:
                print(f"{pokedict['Name']} is a {pokedict[answer2]} type!")
                break
            elif answer2 == "HP":
                print(f"{pokedict['Name']} has an HP stat of {pokedict[answer2]}!")
                break
            elif answer2 == "Attack":
                print(f"{pokedict['Name']} has an Attack stat of {pokedict['Attack']}")
                break
            elif answer2 == "Defense":
                print(f"{pokedict['Name']} has a Defense stat of {pokedict['Defense']}")
                break
            elif answer2 == "Sp. Atk":
                print(f"{pokedict['Name']} has a Sp.Atk stat of {pokedict['Sp. Atk']}")
                break
            elif answer2 == "Sp. Def":
                print(f"{pokedict['Name']} has a Sp. Def stat of {pokedict['Sp. Def']}")
                break
            else:
                print("Invalid Answer")

            
               
            
     

    








