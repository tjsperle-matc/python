#!/usr/bin/env python3

print("""You enter a dark froom with two doors. 
Do you go through door #1, door #2, or door #3?""")


door = input("-> ")

# == Door Number 1 logic =======================
if door =="1":

    print("There's a giant fire breathing dragon in front of you guarding her eggs.")
    print("What do you do?\n")

    print("1. Take an egg.")
    print("2. Say what's up to the dragon.")

    # == dragon logic ============================
    dragon = input("-> ")

    if dragon == "1":
        print("1) The dragon incinerated you alive.  Good job!")
    elif dragon == "2":
        print("2) The dragon waives hello with her little arm. Nice!")
    else:
        print(f"N)Well, doing {dragon} is probably better.")
        print("The dragon flew away.")

# == Door Number 2 logic =======================
elif door == "2":
    print("You find yourself at the top of Mt. Everest.")
    print("What are you gonna do?\n")

    print("1. Snowboard/Ski down.")
    print("2. Climb down.")
    print("3. Jump off.")

    # == Insanity logic ========================
    insanity = input("-> ")

    if insanity == "1" or insanity == "2":
        print("1) You somehow survive, but with severe frostbite.")
        print("1) Good Job!")
    elif insanity == "3":
        print("N) You get some sick air time on the way down, but didn't quite stick the landing.")
        print("N) You're dead!")
    else:
        print("N) You decide to walk back through the door.")
        print("N) Good decision!")

# == Door Number 3 logic =======================
elif door =="3":

    print("You find yourself getting chased by a tiger.")
    print("What do you do?\n")

    print("1. Stop in your tracks, and pet the tiger.")
    print("2. Run like hell.")

    # == Tiger logic ============================
    tiger = input("-> ")

    if tiger == "1":
        print("1) All he wanted was a rub, he's purring like a kitten!")
    elif tiger == "2":
        print("2) The tiger catches you and rips you to shreds. Good job!")
    else:
        print(f"N)Well, doing {tiger} is probably better.")
        print("The tiger fled away.")

else:
    print("You did not select a door??? Good Call :)")
