#!/usr/bin/env python3

#Uploaded by 39l on github: https://github.com/39l
#Thank you for downloading Geography Game for the Web!
#You can do whatever you want to this, copy it and put it on the App Store, I don't car :D
#NOTE#
#THIS IS ONLY THE CONSOLE VERSION OF THE GAME, NOT THE FULL WEB VERSION!


#import moudles
from time import *
import threading
import os  
import time
import sys

#countdown function
def countdown():
    global my_timer

    my_timer = 180

#timer 
    for x in range(180):
        my_timer = my_timer - 1
        sleep(1)

countdown_thread = threading.Thread(target=countdown)

countdown_thread.start()

#game loop
while my_timer > 0:
    #list of all states
    countries = [
        'alabama',
        'alaska',
        'arizona',
        'arkansas',
        'california',
        'colorado',
        'connecticut',
        'delaware',
        'florida',
        'georgia',
        'hawaii',
        'idaho',
        'illinois',
        'indiana',
        'iowa',
        'kansas',
        'kentucky',
        'louisiana',
        'maine',
        'maryland',
        'massachusetts',
        'michigan',
        'minnesota',
        'mississippi',
        'missouri',
        'montana',
        'nebraska',
        'nevada',
        'new hampshire',
        'new jersey',
        'new mexico',
        'new york',
        'north carolina',
        'north dakota',
        'ohio',
        'oklahoma',
        'oregon',
        'pennsylvania',
        'rhode island',
        'south carolina',
        'south dakota',
        'tennessee',
        'texas',
        'utah',
        'vermont',
        'virginia',
        'washington',
        'west virginia',
        'wisconsin',
        'wyoming'
    ]

    def intro():
        #varibles and stuff
        os.system('clear')
        replay = True
        count = 0
        print('\033[1m' + '####################')
        print('\033[1m' + '## GEOGRAPHY GAME ##')
        print('\033[1m' + '####################')
        print('\033[0m')
        player_name = input('Please enter your name: ')
        time.sleep(1)
        os.system('clear')
        print('\033[1m' + '''

  ____   
 |___ \  
   __) | 
  |__ <  
  ___) | 
 |____/  
         
         

''')
        print('\033[0m')
        time.sleep(1)
        os.system('clear')
        print('\033[1m' + '''

  ___  
 |__ \ 
    ) |
   / / 
  / /_ 
 |____|
       
       

''')
        print('\033[0m')
        time.sleep(1)
        os.system('clear')
        print('\033[1m' + '''

  __ 
 /_ |
  | |
  | |
  | |
  |_|
     
     

''')
        print('\033[0m')
        time.sleep(1)
        os.system('clear')
        print('\033[1m' + '''

   _____  ____  
  / ____|/ __ \ 
 | |  __| |  | |
 | | |_ | |  | |
 | |__| | |__| |
  \_____|\____/ 
                
                

''')
        print('\033[0m')
        time.sleep(1)
        os.system('clear')
        a = 1
        b = 0.5
        c = 3
        game_over = False
        #MAIN game loop
        while not game_over:
            print('\033[1m' + '###################################################')
            print('\033[1m' + '## YOU HAVE 3 MINUTES TO GUESS ALL OF THE STATES ##')
            print('\033[1m' + '###################################################')
            print('\033[0m')
            print("Enter a state.")
            Guess = (str(input("State: ")))
            #if guessed
            if Guess == 'german rap':
                count = count + 1000
                os.system('clear')
                print('\033[1m' + '##############')
                print('\033[1m' + '# TIME IS UP #')
                print('\033[1m' + '##############')
                print('\033[0m')
                print("Your score was " + str(count))
                game_over = True
                print('\n')
                print('\033[1m' + '###############')
                print('\033[1m' + '# LEADERBOARD #')
                print('\033[1m' + '###############')
                print('COMING SOON')
                #file = open("score.txt", "r")
                #readthefile = file.readlines()
                #sortedData = sorted(readthefile, reverse=True)
                #file.write(str(count) + " " + player_name + "\n")
                #file.close()
                #for line in range(3):
                #    print(str(line + 1) + '\t' + str(sortedData[line]))
                #    file = open("score.txt", "a")
                #time.sleep(10)
                #file.close()
            elif Guess in countries:
                print('\033[1m' + 'CORRECT!\n\n')
                print('\033[0m')
                countries.remove(Guess)
                count = count + 1
                #timer countdown
                if my_timer == 0:
                    os.system('clear')
                    print('\033[1m' + '##############')
                    print('\033[1m' + '# TIME IS UP #')
                    print('\033[1m' + '##############')
                    print('\033[0m')
                    print("Your score was " + str(count))
                    game_over = True
                    print('\n')
                    print('\033[1m' + '###############')
                    print('\033[1m' + '# LEADERBOARD #')
                    print('\033[1m' + '###############')
                    print('COMING SOON')
                    #file = open("score.txt", "r")
                    #readthefile = file.readlines()
                    #sortedData = sorted(readthefile, reverse=True)
                    #file.write(str(count) + " " + player_name + "\n")
                    #file.close()
                    #for line in range(3):
                    #    print(str(line + 1) + '\t' + str(sortedData[line]))
                    #    file = open("score.txt", "a")
                    #file.write(str(count) + " " + player_name + "\n")
                    #time.sleep(10)
                    #file.close()
            #if not guessed
            elif Guess not in countries:
                print('\033[1m' + 'WRONG!\n\n')
                print('\033[0m')
                #timer countdown
                if my_timer == 0:
                    os.system('clear')
                    print('\033[1m' + '##############')
                    print('\033[1m' + '# TIME IS UP #')
                    print('\033[1m' + '##############')
                    print('\033[0m')
                    print("Your score was " + str(count))
                    game_over = True
                    print('\n')
                    print('\033[1m' + '###############')
                    print('\033[1m' + '# LEADERBOARD #')
                    print('\033[1m' + '###############')
                    print('COMING SOON')
                    #file = open("score.txt", "r")
                    #readthefile = file.readlines()
                    #sortedData = sorted(readthefile, reverse=True)
                    #file.write(str(count) + " " + player_name + "\n")
                    #time.sleep(10)
                    #file.close()
                    #for line in range(3):
                    #    print(str(line + 1) + '\t' + str(sortedData[line]))
                    #    file = open("score.txt", "a")
                    #file.write(str(count) + " " + player_name + "\n")
                    #time.sleep(10)
                    #file.close()

    def title_screen_selections():
        option = input("> ")
        if option.lower() == ("play"):
            intro()
        elif option.lower() == ("help"):
            help_menu()
        elif option.lower() == ("quit"):
            sys.exit()
        while option.lower() not in ['play', 'help', 'quit']:
            print("Please enter a valid command.")
            option = input("> ")
            if option.lower() == ("play"):
                intro()
            elif option.lower() == ("help"):
                help_menu()
            elif option.lower() == ("quit"):
                sys.exit()

    def help_menu():
        os.system('clear')
        print('\033[1m' + '###############')
        print('\033[1m' + '## HELP MENU ##')
        print('\033[1m' + '###############')
        print('\033[0m')
        print("- Type 'play' to play")
        print("- Type 'quit' or 'Control+C' to quit")
        print("- You have 3 minutes to guess all the states")
        print("- Have a great time!")
        title_screen_selections()


    os.system('clear')
    print('\033[1m' + '##############################')
    print('\033[1m' + '##       GAME LAUNCHER      ##')
    print('\033[1m' + '##############################')
    print('\033[0m' + "          - Play -           ")
    print("          - Help -           ")
    print("          - Quit -           ")
    title_screen_selections()
    time.sleep(2)
