import general_mechanics
import doctest


def draw_board(player_position):
    """Draws the playing map of the game
    
    :param player_position: a list
    :precondition: the first two values in player_position must be an integer from 1 to 5 inclusive, where the first value is the vertical coordinate, and the second value is the horizontal coordinate.
    
    :postcondition: prints a 5 row and 5 column grid with the player's    position as the lambda symbol
    
    :return: none"""

    for rows in range(1, 6):
        for columns in range(1, 6):
            if (player_position[0] == rows) and player_position[1] == columns:
                # symbol for player character
                print("\u03BB", end=" ")
            else:
                # symbol for empty grid square
                print("\u25A2", end=" ")
        print()
    print()


def move(player_position, direction):
  """ Change the position of the player
      
      Changes the y and x coordinates if the player can go in the desired direction, otherwise returns the same player position. Uses the interpret_move,,
  
  :param player_position: player's current position (y and x coordinates). A list
  :param direction: a direction that the person wants to go to. A string
  :precondition: the first two elements in the player position list should be in the range of 1 to 5 inclusive.
  :postcondition: correctly computes the new player position
  >>> move([1, 2, 1, 'Chloe'], "north")
  There's a wall in front of you
  [1, 2, 1, 'Chloe']
  >>> move([5, 3, 10, 'Ivan'], "south")
  There's a wall in front of you   
  [5, 3, 10, 'Ivan']
  >>> move([4, 5, 9, 'Peter'], "east")
  There's a wall in front of you
  [4, 5, 9, 'Peter']
  >>> move([4, 1, 9, 'Peter'], "west")
  There's a wall in front of you
  [4, 1, 9, 'Peter'] 
  >>> move([4, 4, 9, 'Peter'], "east")
  [4, 5, 9, 'Peter'] 
  >>> move([4, 5, 9, 'Peter'], "west")
  [4, 4, 9, 'Peter'] 
  >>> move([4, 5, 9, 'Peter'], "south")
  [5, 5, 9, 'Peter']
  >>> move([4, 5, 9, 'Peter'], "north")
  [3, 5, 9, 'Peter']       
  """
  
  if direction in general_mechanics.POSSIBLE_DIRECTIONS():
      if player_position[0] == 1 and direction == "north":
          print("\nThere's a wall in front of you")
      elif player_position[0] == 5 and direction == "south":
          print("\nThere's a wall in front of you")
      elif player_position[1] == 1 and direction == "west":
        print("\nThere's a wall in front of you")
      elif player_position[1] == 5 and direction == "east":
        print("\nThere's a wall in front of you")
      else:
        player_position = interpret_move(player_position, direction)     
  else:
      print("Invalid direction input.")
  return player_position


def interpret_move(position, direction):
    """Moves the player in the game map
    
    :param position: a list
    :param direction: a string
    :precondition: The direction must be a string of "north", "south", "east", or "west". The first two elements in the position list should be in the range of 1 to 5 inclusive
    :postcondition: The function increments or decrements the first two indexed items in the position list depending on the string
    :return position: a list
        
    >>> interpret_move([2, 2, 1, 'Chloe'], "north")
    [1, 2, 1, 'Chloe']
    >>> interpret_move([2, 3, 10, 'Ivan'], "south")   
    [3, 3, 10, 'Ivan']
    >>> interpret_move([4, 4, 9, 'Peter'], "east")
    [4, 5, 9, 'Peter']    
    >>> interpret_move([4, 3, 9, 'Peter'], "west")
    [4, 2, 9, 'Peter']    """

    if direction == "north":
        position[0] -= 1
    elif direction == "south":
        position[0] += 1
    elif direction == "east":
        position[1] += 1
    elif direction == "west":
        position[1] -= 1
    return position
      

def main():

  doctest.testmod()


if __name__ == "__main__":
    main()
