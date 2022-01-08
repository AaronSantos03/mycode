#!.usr/bin/env python

#Disney Villain quiz

print("Please answer the following questions to see what Disney villain you are!")

Scar = 0
Ursala = 0
Hades = 0



while True:
    response = input("Out of the 3 Disney movies, which is your favorite?(Lion King, the little mermaid, Hercules)")
    if response == "Lion King":
        break
    if response == "the little mermaid":
            break
    if response == "Hercules":
                break
    else:
        print("Invalid")

while True:
      list = ["A.I'm surrounded by idiots", "B.Man F*** this", "C.I hate everyone", "D.All of the above"]
      print("\nMy catchphrase is: ")
      print(list[0])
      print(list[1])
      print(list[2])
      print(list[3]) 

      response = input(" - ")
      if response == "A":
          Scar += 1
          break
      elif response == "a":
          Ursala += 2
          break
      if response == "B":
          Scar += 1
          break
      elif response == "b":
          Ursala += 2
          break
      if response == "C":
          Hades += 3
          break
      elif response == "c":
          break
      if response == "D":
          Hades += 3
          break
      elif response == "d":
          break
      else:
          print("Invalid")
                

while True:
    list = ["A.Spongebob", "B.Goku", "C.Sonic", "D.Naruto"]
    print("\nWho would you choose as your sidekick: ")
    print(list[0])
    print(list[1])
    print(list[2])
    print(list[3])

    response = input(" - ")
    if response == "A":
        Scar += 1
        break
    elif response == "a":
        Ursala += 2
        break
    if response == "B":
        Scar += 1
        break
    elif response == "b":
        Ursala += 2
        break
    if response == "C":
        Hades += 3
        break
    elif response == "c":
        break
    if response == "D":
        Hades += 3
        break
    elif response == "d":
        break
    else:
        print("Invalid")


while True:
    list = ["A.a castle", "B.Tacobell", "C.the underworld", "D.Walmart aisle 4"]
    print("\nWhere would you want your evil lair to be?: ")
    print(list[0])
    print(list[1])
    print(list[2])
    print(list[3])

    response = input(" - ")
    if response == "A":
        Scar += 1
        break
    elif response == "a":
        Ursala += 2
        break
    if response == "B":
        Scar += 1
        break
    elif response == "b":
        Ursala += 2
        break
    if response == "C":
        Hades += 3
        break
    elif response == "c":
        break
    if response == "D":
        Hades += 3
        break
    elif response == "d":
        break
    else:
        print("Invalid")


while True:
    if Scar > Ursala:
        input("You are Scar! Click here --> https://images.app.goo.gl/KN3nELDDzdvTEXVG8")
        break
    if Ursala > Scar:
        input("You are Ursala! Click here --> https://images.app.goo.gl/DHFQnQu5paFWMzzY7")
        break
    if Hades > Scar:
        input("You are Hades! Click here --> https://images.app.goo.gl/sZmXDuHj98MBJeFu9")
        break
    if Hades > Ursala:
        input("You are Hades! Click here --> https://images.app.goo.gl/Hx5dtq33MWLox3EY6")
        break
    if Ursala > Hades:
        input("You are Ursala! Click here --> https://images.app.goo.gl/dawC73pn3PVYX1ws5")
        break
    if Scar > Hades:
        input("You are Scar! Click here --> https://images.app.goo.gl/AihioKpVm5Uz5wPF8")
        break

    print("Thank you for playing!!!!")

    
  
