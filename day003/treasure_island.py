print('''
     .--------------------------------...
               ,'-------------------------------,'   |
              /                                /     |
             /________________________________/    ,'|
             |               ..               |  ,'  |
             |___________-==/88\==-___________|,' /) |.
             |  \    \     ((  ))     /    /  |  (/  |-. .
             |   \    \     \{}/     /    /   |    .' .  .
          . '|    \    \     )(     / _  /    |    ,   .  .
         . . |\    \    \    \/    _.( ~-.   /|\ ,' .   . .
       ` .  -`_-.--.______..._____( ,/  ` \~-.|,' .   .
        .  `    .     .       .  ,'\. ~-  . , .  .  .   .
           .  `   .     ,   .      , ~~-.' .  .    .
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
answer_1 = input("You've just arrived at the sandy beach. On your right, you have a jungle. On your left, you have a harbor with pirates. Where do you want to go? Type left or right.\n").lower()
if answer_1 == "right":
  print("You've escaped death by a nail. You've gone deep into the jungle and encounter a lake with dark waters. You need to get across it. If you swim, you'll get a lot faster. If you go around, you'll take a lot more time and may face dangerous creatures.")
  answer_2 = input("Type swim or go around.\n").lower()
  if answer_2 == "go around":
    print("You've managed to move silently and escape the jungle creatures.")
    print("You're now faced with three shiny portals: one yellow, one blue and one red. Two of them are death traps and only one will get you safe. Which one will you choose?")
    answer_3 = input("Type the color of the portal.\n").lower()
    if answer_3 == "red":
      print("You've been eaten by a Dragon! Game over.")
    elif answer_3 == "blue":
      print("You've been turned into stone by Medusa! Game over.")
    else:
      print("You found the treasure! Congratulations!")
  else:
    print("You've been mauled by crocodiles to death! Game over.")
else:
  print("You've been tortured to death! Game over.")
