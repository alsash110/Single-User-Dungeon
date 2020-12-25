import random


def roll_die(number_of_edges):
    """Generate a random number
    
    Genereates a random number in the range from 1 to user's input inclusively.
    
    :param number_of_edges:
    :precondition: number_of_edges should be a positive integer greater than 1
    :postcondition: the errorless generation of a random number
    :return: an integer between 1 and number_of_edges inclusive
    """
    
    return random.randint(1,number_of_edges)


def POSSIBLE_ACTIONS():
    """ Protect a tuple of possible actions.

      Protects the POSSIBLE_ACTIONS tuple by 
    """
    POSSIBLE_ACTIONS = ("north", "south", "east", "west", "quit")
    return POSSIBLE_ACTIONS


def POSSIBLE_ACTIONS_2():
    """ Protect a tuple of possible actions.

        Protects the POSSIBLE_ACTIONS_2 tuple by 
    """
    POSSIBLE_ACTIONS_2 = ("fight", "flee", "quit")
    return POSSIBLE_ACTIONS_2


def POSSIBLE_DIRECTIONS():
    POSSIBLE_DIRECTIONS = ("north", "south", "east", "west")  
    return POSSIBLE_DIRECTIONS


def init_character(character_name):
    """Initiate the game
    
    Creates the player character and prints the introductory dialogue
    
    :param: the name of the character, entered by user
    :precondition: none
    :postcondition: none
    :return: the function returns a character with an initialized position (y,x coordinates), 10 hp and character name
    """
    
    your_character = [random.randint(1, 5), random.randint(1, 5), 10, character_name]
    print(f"\nYou wake up in a storage room of the SPACECRUISER-Chrisader. A fellow crewmate sits right next to you. He is missing a head and a left arm. You head to the nearest computer terminal and open up Slack messages:\n\nTo: {character_name}\n{character_name}! You took a nasty hit in the head so we brought you here. I don't know how you'll survive...... the monsters have infected everyone and damaged the engine of the Chrisader. Your regenerative shield will protect you. Don't let anything hit you past your shield! You are too weak to take such a hit!\n") 
    return your_character