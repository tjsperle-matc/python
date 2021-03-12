#! /usr/bin/env python3

print("Name:Tyler Sperle")

password_database = {'Username':'dnedry', 'Password':'please'}

command_database = {'reboot	':'OK. I will reboot all park systems.', 'shutdown	'
:'OK. I will shut down all park systems.', 'done	':'I hate all this hacker stuff.'}

white_rabbit_object = 0
counter = 0
try:

    while True:
        if white_rabbit_object == 0 and counter < 3:
            print("You didn't say the magic word. {counter}")
            counter += 1
        elif counter == 3:
            print("You didn't say the magic word!")
        elif white_rabbit_object == 1 and counter < 3:
            print("Hi, Dennis. You're still the best hacker in Jurrasic Park.")

