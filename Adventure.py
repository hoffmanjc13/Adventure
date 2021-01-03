print("   _________________________________________________________")
print(" /|     -_-                                             _-  |\ ")
print("/ |_-_- _                                         -_- _-   -| \ ")
print("  |                            _-  _--                      | ")
print("  |                            ,                            | ")
print("  |      .-'````````'.        '(`        .-'```````'-.      | ")
print("  |    .` |           `.      `)'      .` |           `.    | ")
print("  |   /   |   ()        \      U      /   |    ()       \   | ")
print("  |  |    |    :         | o   T   o |    |    :         |  | ")
print("  |  |    |     :        |  .  |  .  |    |    :         |  | ")
print("  |  |    |     :        |   . | .   |    |    :         |  | ")
print("  |  |    |     :        |    .|.    |    |    :         |  | ")
print("  |  |    |____:_________|     |     |    |____:_________|  | ")
print("  |  |   /  __ :   -     |     !     |   /     `'() _ -  |  | ")
print("  |  |  / __  ()        -|        -  |  /  __--      -   |  | ")
print("  |  | /        __-- _   |   _- _ -  | /        __--_    |  | ")
print("  |__|/__________________|___________|/__________________|__| ")
print(" /         -_                  --_             _ -        -_ \ ")
print("/   -_- _ -             _- _---                       -_-  -_ \ ")
print("Game by: Julia Hoffman and Katelyn Jefri")
print("")
print("")
print("You are the knight Sir... Sir...")
print("What was your name again?")
name = input(">>> ")
print("Right! I knew that. You're Sir %s, fighter of MONSTERS and slayer of DRAGONS." %name)
print("Well, you haven't slain your dragon yet. Instead, you managed to get captured by his guards during an ill advised attempt to kill him. You are now in the depths of his dungeons, awaiting your death by DRAGONFIRE. Rather unfortunate, in my opinion.")
print("")
print("But never let it be said that Sir %s backed down from a challege!" %name)
print("You look around your CELL. You think you could break down the barred DOOR if you ran at it. You also spot a small PEBBLE on the floor.")
print("")
print("Do you:")
print("run at the door")
print("throw the pebble")
while(True):
    answer1 = input(">>> ").lower()
    if(answer1 == "run at the door"):
        print("The bars were stronger than they looked. Not that you'd know; you tripped on the pebble and fell, cracking your skull on the STONE FLOOR and spilling more goo on the wall as you die. Eww.")
        print("")
        print("Play again?")
        exit()
    elif(answer1 == "throw the pebble"):
        print("Your JAILER hears the sound and comes to investigate. As he walks past your cell, you reach out and grab his KEYS. You unlock your cell and step into the hall.")
        print("")
        print("You glance to your LEFT, then to your RIGHT, where you see a cracked DOOR. The hall to your left is dim and feels foreboding, but the door to your right is softly BUZZING.")
        break
    else:
        print("Are you daft? That's not one of your options. Hurry up and get out of this cell.")
print("")
print("Do you:")
print("go left")
print("go right")
while(True):
    answer2 = input(">>> ").lower()
    if(answer2 == "go left"):
        print("A few twists and turns later, you find yourself in a STAIRWELL.")
        print("")
        print("The stairs UP look clean. The stairs DOWN are unlit and look like they're several centuries old.")
        print("")
        print("Do you:")
        print("go up")
        print("go down")
        break
    elif(answer2 == "go right"):
        print("You proceed to the door as the buzzing gets louder. You open it to find-")
        print("")
        print("AHHHH! $@^&! Wasps! I hate wasps!")
        print("")
        print("They swarm you and- Ick. I'm not looking anymore. Suffice it to say, you're dead. Don't ever come back to this room.")
        print("")
        print("*sigh* Play again?")
        quit()
    else:
        print("That makes no sense, idiot. Try one of your options, and do it quick. The jailer won't be gone forever.")
while(True):
    answer3 = input(">>> ").lower()
    if(answer3 == "go down"):
        print("You head down into the murk, only to run into the jailer and his SWORD. It's better than dragonfire, you suppose. Or you would, if you weren't dead.")
        print("")
        print("Pay more attention next time. Play again?")
        quit()
    elif(answer3 == "go up"):
        print("You regret that decision pretty quickly as you huff and puff your way up more flights of stairs than you care to count. You arrive in a room that appears to be the ARMORY. Even better, it has WINDOWS.")
        print("There are only two SWORDS hanging on the walls. One of the swords is a beautiful BLADE, you assume. The scabbard is decorated with firey GOLD and stunning orange SAPPHIRES. The other has no scabbard and would better be described as a CLUB than a sword based on its total lack of sharp edges.")
        print("")
        print("Do you:")
        print("grab the bejeweled blade")
        print("grab the sorry-excuse-for-a-sword")
        break
    else:
        print("The dungeon rats seem to have a higher IQ than you do. The mess you just suggested isn't an option. Now pick one of your options before you get caught and killed.")

while(True):
    answer4 = input(">>> ").lower()
    if(answer4 == "grab the bejeweled blade"):
        print("You pull the weapon from its scabbard, only for a ray of SUNSHINE to reflect off the perfectly polished blade, blinding you. Unable to see, you trip and fall down the stairs.")
        print("")
        print("You should really reflect on your life choices. Or death choices in this case. Play again?")
        quit()
    elif(answer4 == "grab the sorry-excuse-for-a-sword"):
        print("Now armed, you decide that your new piece of knightly steel must have a knightly name.")
        swordName = input("What do you name it? ")
        print("")
        print("You slide %s into your belt and leave the armory. Now all that's left to do is find the dragon. Fortunately for you, it is ASLEEP right outside the armory. Even better, it doesn't wake up when you walk in. Best of all, the CASTLE GATES loom right behind it." %swordName)
        print("")
        print("You realize that it would be easy enough to walk up to it and STAB IT with %s. Any good knight should always kill the dragon. But on the other hand, the WAY OUT you've been pining for ever since you got dragged into the dungeons is right there. You could just leave and be free." %swordName)
        print("Do you:")
        print("stab the dragon")
        print("leave through the gates")
        break
    else:
        print("I'm afraid I don't understand since I don't speak nincompoop. And I don't intend to learn, though you seem bent on giving me plenty of time to. Now pick a weapon before I get too bored of your stupidity.")

while(True):
    answer5 = input(">>> ").lower()
    if(answer5 == "stab the dragon"):
        print("You walk up to the hulking beast and plunge %s into his SCALY HIDE. The good news is that the sword somehow musters the structural integrity to survive the impact. The bad news is that the dragon seems to dislike rusty chunks of metal sticking out of its side and torches you with DRAGONFIRE. The great news is that the lump of scrap you poked him with gives him TETANUS, killing him. So congratulations, %s. You are officially a DRAGONSLAYER. I guess you weren't that bad a knight after all." %(swordName,name))
        print("")
        print("Play again?")
        quit()
    elif(answer5 == "dance"):
        print("You twerk in the dragon's face. Unfortunatly, it appears the dragon hates twerking and bites your butt off before bathing you with dragonfire.")
        print("Play again?")
        quit()
    elif(answer5 == "leave through the gates"):
        print("That idea's almost as asinine as you are. You are a knight, albeit a stupid one. Knights must always fight the dragon, even if they have no sense. Pick a more fitting plan.")
    else:
        print("I told you your options. That was not one of them. Now pick before I lose my patience and wake the dragon for you.")
