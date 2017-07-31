#Ask user for their name
#Print welcome message
#Ask user for difficulty level
#Return paragraph for the chosen setting
#Print paragraph to user with ___BLANKS____ instead of answers
#Convert the paragraph into a list using the split function
#Ask user for answers, starting with ___1___
#If user is correct, replace ___BLANKS___ with correct answer (in upper cases).
#Return and print updated paragraph
#Keep going until the end of split difficulty_paragraph
#Return new, replaced string.
#Print congratulatory message
#Ask user if they want to play again

import string
################################################################################
'''GLOBAL VARIABLES'''

blanks = ["___1___", "___2___", "___3___", "___4___"]

easy_paragraph = "\nYou chose the ___1___ difficulty level. This project is the third submission for ___2___'s IPND. The scripting language being used for this project is ___3___. This game is called fill in the ___4___s\n"
medium_paragraph = "\nThe current President of the United States is Donald ___1___. He ran as a member of the ___2___ party. Before that, he was famous for saying 'You're ___3___!' on his TV show, Celebrity Apprentice. He is notorious for having small ___4___s.\n"
hard_paragraph = "\nSettlers of ___1___ is a German board game first produced in 1995. It is an ___2___-based game where players have to build settlements and cities. The goal of the game is to get ten (10) ___3___ points. There are five (5) different resources: Brick, Ore, ___4___, Wheat, and Wood.\n"

easy_answers = ["easy", "udacity", "python", "blank"]
medium_answers = ["trump", "republican", "fired", "hand"]
hard_answers = ["catan", "economy", "victory", "sheep"]

user_name = raw_input("\nHey there, stranger. What's your name? ")


################################################################################
'''Helper Functions'''

def hello_message(name):
    '''Welcome message to the user because .. why not?
    Inputs - User input of their name.
    Outputs - Pleasantries and instruction.'''

    print "\nHey there " + name +"! Thanks for playing this game with me. \nPlease select a difficulty level by typing the corresponding number"

def restart():
    '''Allows the user to restart the program. Case insensitive.
    Inputs - NONE
    Outputs - If user wants to restart, back to beginning of program. If not, exits'''
    print "\nShall we play a game?"
    user_restart = raw_input("\nType Y or YES to play again: ").lower()
    if user_restart == "y" or user_restart == "yes":
        print "\nExcellent. Let's play!"
        run_game(user_name)
    elif user_restart == "n" or user_restart == "no":
        print "\nUntil next time ... "
        exit()
    else:
        print "\nI didn't understand that."
        restart()

def game_setup(diff):
    '''Function that determines which question / answer has been chosen.
    Inputs - Difficulty level (chosen by user)
    Outputs - Paragraph & answers that correspond with user's choice'''

    if diff == "1":
        print "You chose EASY. This'll be a piece of cake."
        return easy_paragraph, easy_answers
    elif diff == "2":
        print "You chose MEDIUM. This should not be too tough."
        return medium_paragraph, medium_answers
    elif diff == "3":
        print "You chose HARD. Honestly, it's still simple."
        return hard_paragraph, hard_answers

def get_answers(diff, paragraph, answers):
    '''This function gets the user's answers to each blank. User inputs are case insensitive -- the program will respond appropriately whether or not the user capitalizes any letters.
    Input - Chosen difficulty & it's corresponding paragraph and answers.
    Output - The updated paragraph that replaces BLANKs with the answers'''

    user_answer = ""
    index = 0
    death_counter = int(raw_input("\nHow many guesses would you like? "))
    while index < len(blanks):
        question = "\nWhat is your answer for " + blanks[index] + "?"
        print question

        user_answer = raw_input("\nType your answer here: ").lower()
        if user_answer == answers[index]:
            paragraph = string.replace(paragraph, blanks[index], user_answer.upper())
            print paragraph
            index += 1
        else:
            death_counter -= 1
            print "That was wrong! You have " + str(death_counter) + " lives left."
            if death_counter == 0:
                print "You lose!"
                restart()
            print paragraph

    paragraph = ''.join(paragraph)
    return paragraph


################################################################################

def run_game(user_name):
    '''This function runs the main game.
    Inputs - User's name from input when application launches. Better UI for restarting games -- only have to input once upon launching
    Outputs - Everythang'''

    hello_message(user_name)

    user_difficulty = raw_input("\nEASY - 1 || MEDIUM - 2 || HARD - 3 ")

    if user_difficulty == "1" or user_difficulty == "2" or user_difficulty == "3":
        paragraph, answers = game_setup(user_difficulty)
        print paragraph

        replaced = get_answers(user_difficulty, paragraph, answers)

        print "Congratulations " + user_name + "!"
        restart()

    else:
        print "\nI'm sorry, I didn't understand what you just typed."
        restart()


run_game(user_name)
