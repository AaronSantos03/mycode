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
    print("\nChoices:")
    print(list[0])
    print(list[1])
    print(list[2])
    print(list[3])
    print(list[4])
    print(list[5])

    if Bulbasaur > Squirtle:
        input("What would you like to know about Bulbasaur? -")
        break
    if Squirtle > Charmander:
        input("What would you like to know about Squirtle? -")
        break
    if Charmander > Chikorita:
        input("What would you like to know about Charmander? -")
        break
    if Chikorita > Cyndaquil:
        input("What would you like to know about Chikorita? -")
        break
    if Cyndaquil > Totodile:
        input("What would you like to know about Cyndaquil? -")
        break
    if Totodile > Bulbasaur:
        input("What would you like to know about Totodile? -")
    else:
        print("Invalid Answer")
        break

with open("pokedex.txt") as pokedata:
    for x in csv.DictReader(pokedata):
        if pokedict["Name"] == pokename:
            if pokedict["Type 1"]:
                print("{pokedict['Name]} is a {pokedict['Type 1']} type!")

            
            
            
     

    








