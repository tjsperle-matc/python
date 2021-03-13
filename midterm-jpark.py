#! /usr/bin/env python3

print("Name:Tyler Sperle")

password_database = {'Username':'dnedry', 'Password':'please'}

command_database = {'reboot':'OK. I will reboot all park systems.', 'shutdown'
:'OK. I will shut down all park systems.', 'done':'I hate all this hacker stuff.'}

white_rabbit_object = 0
counter = 0

while( not(white_rabbit_object) and (counter < 3)):
    input_user = input("Username: ")
    input_password = input("Password: ")

    if((input_user == password_database["Username"]) and
    (input_password == password_database["Password"])):
        white_rabbit_object = 1
        print("Hi Dennis. You're still the best hacker in Jurassic Park.")
        command = input(f"Please Enter a command {command_database.keys()}: ")

        if command in command_database.keys():
            print(command_database[command])
        else:
            print("The Lysine Contingency has been put into effect.")
    else:
        counter += 1
        if(counter < 3):
            print(f"You didn't say the magic word {counter}")
        else:
            for i in range(0,25):
                print("You didn't say the magic word! ")


