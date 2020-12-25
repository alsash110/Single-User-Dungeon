import random
import general_mechanics
import environment
import combat


# Position = [row, column]
def main():
    """Drive the function.
  
    Drive the function.
    """
    # Set starting conditions
    # player_info shall contain [y position, x position, health]
    player_info = general_mechanics.init_character(input("Enter you character's name >>> "))
    user_action_input = ""
    environment.draw_board(player_info)
  
    # Primary game routine
    while player_info[2] > 0:
    
        print(f"Your current shield level is {player_info[2]}.")
        print(f"Possible actions: {general_mechanics.POSSIBLE_ACTIONS()}")
        user_action_input = input("What's your next action? >>> ")
    
        # Movement routine
        if user_action_input == "quit":
            player_info[2]=0
        else:
            # Return updated player coordinates if moved, returns same if hits wall
            # Create copy of list in different location in memory
            player_info_copy = player_info[:]
            if player_info_copy != environment.move(player_info, user_action_input):   
                

                # Check for monster and run combat routine if
                if combat.monster_check(player_info):
                  environment.draw_board(player_info)
                  player_info[2] = combat.combat_check(player_info[2])
          
            if player_info[2] > 0:
              environment.draw_board(player_info)
    print(f"\nYou fought well, {player_info[3]}, but the monsters are already eating your second and last leg.\nIt seems like you are dead.\nThanks for playing!")
        

  
if __name__ == "__main__":
    main()