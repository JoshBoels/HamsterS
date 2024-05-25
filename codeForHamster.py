#Josh Boelema,
#This program is set to solve a maze using the hamsterS robot
#import the roboid library
from roboid import *

# Create a Hamster robot object
hamster = HamsterS()

# Create an empty list to hold open directions
opens = []
class Block:
    def __init__(self, cor):
        self.cor = cor

# Create a 5x5 maze made of Block objects
maze = []
for x in range(5):
    tmp = []
    for y in range(5):
        tmp.append(Block([x, y]))
    maze.append(tmp)


# Function to print the maze
def print_maze():
    for i in range(5):
        string = ""
        for j in range(5):
            string += str(maze[j][i].cor) + " "
        print(string)

# Function to scan for open directions and add them to the "opens" list
def scan():
    wait(400)
    FRONT = hamster.left_proximity()
    RIGHT = hamster.right_proximity()

    if FRONT < 30:
        # print("FRONT OPEN")
        opens.append("F")

    if RIGHT < 40:
        # print("RIGHT OPEN")
        opens.append("R")

    wait(400)
    hamster.turn_left(90, 50)
    LEFT = hamster.left_proximity()
    if LEFT < 30:
        # print("LEFT OPEN")
        opens.append("L")
    wait(40)
    hamster.turn_right(90, 50)
# Function to make a decision based on the available directions
def make_decision():
    if len(opens) == 0:
        return 'B'
    else:
        if "F" in opens:
            return "F"
        else:
            if "L" in opens:
                return "L"
            else:
                return "R"

# Print the maze
print_maze()

# Set starting coordinates and direction
current_cor = [4, 4]
current_dir = "W"

# Check function
def check():
    if current_cor == [1, 2]:
        if current_dir == "N":
            # Check right proximity sensor
            if hamster.right_proximity() < 30:
                # Turn right, move forward and make sound
                hamster.turn_right(90, 50)
                hamster.move_forward(9, 50)
                hamster.sound_until_done(4, 10)
                exit(0)
        elif current_dir == "S":
            # Turn left and check left proximity sensor
            hamster.turn_left(90, 50)
            if hamster.left_proximity() < 30:
                # Move forward and make sound
                hamster.move_forward(9, 50)
                hamster.sound_until_done(4, 10)
                exit(0)
            else:
                # Turn right
                hamster.turn_right(90, 50)
        elif current_dir == "E":
            # Check left proximity sensor
            if hamster.left_proximity() < 30:
                # Move forward and make sound
                hamster.move_forward(9, 50)
                hamster.sound_until_done(4, 10)
                exit(0)

    # elif current is 2,1
    elif current_cor == [2, 1]:
        if current_dir == "E":
            if hamster.right_proximity() < 30:
                # turn right 90 degrees and move forward
                hamster.turn_right(90, 50)
                hamster.move_forward(9, 50)
                hamster.sound_until_done(4, 10)
                # exit the program
                exit(0)
        elif current_dir == "W":
            # turn left 90 degrees
            hamster.turn_left(90, 50)
            if hamster.left_proximity() < 30:
                # move forward and make sound
                hamster.move_forward(9, 50)
                hamster.sound_until_done(4, 10)
                # exit the program
                exit(0)
            else:
                # turn right 90 degrees
                hamster.turn_right(90, 50)
        elif current_dir == "S":
            if hamster.left_proximity() < 30:
                # move forward and make sound
                hamster.move_forward(9, 50)
                hamster.sound_until_done(4, 10)
                # exit the program
                exit(0)

    # elif current is 3,2
    elif current_cor == [3, 2]:
        if current_dir == "S":
            # If the right proximity sensor detects an obstacle
            if hamster.right_proximity() < 30:
                hamster.turn_right(90, 50)
                hamster.move_forward(9, 50)
                hamster.sound_until_done(4, 10)
                exit(0)
        elif current_dir == "N":
            hamster.turn_left(90, 50)
            # If the left proximity sensor detects an obstacle
            if hamster.left_proximity() < 30:
                hamster.move_forward(9, 50)
                hamster.sound_until_done(4, 10)
                exit(0)
            else:
                hamster.turn_right(90, 50)
        elif current_dir == "W":
            # If the left proximity sensor detects an obstacle
            if hamster.left_proximity() < 30:
                hamster.move_forward(9, 50)
                hamster.sound_until_done(4, 10)
                exit(0)

    #elif current is 2,3
    elif current_cor == [2, 3]:
        if current_dir == "W":
            # If the right proximity sensor detects an obstacle
            if hamster.right_proximity() < 30:
                hamster.turn_right(90, 50)
                hamster.move_forward(9, 50)
                hamster.sound_until_done(4, 10)
                exit(0)
        elif current_dir == "E":
            hamster.turn_left(90, 50)
            # If the left proximity sensor detects an obstacle
            if hamster.left_proximity() < 30:
                hamster.move_forward(9, 50)
                hamster.sound_until_done(4, 10)
                exit(0)
            else:
                hamster.turn_right(90, 50)
        elif current_dir == "N":
            # If the left proximity sensor detects an obstacle
            if hamster.left_proximity() < 30:
                hamster.move_forward(9, 50)
                hamster.sound_until_done(4, 10)
                exit(0)

#while statement for the goal state
while True:
    if current_cor == [2, 2]:
        print("END GOAL")
        hamster.sound_until_done(4, 10)
        break

    hamster.move_forward(9, 80)
    if hamster.left_proximity() > 75:
        hamster.move_backward(1.4, 30)
    # Update current coordinates based on current direction
    if current_dir == "N":
        current_cor = [current_cor[0], current_cor[1] - 1]
    elif current_dir == "S":
        current_cor = [current_cor[0], current_cor[1] + 1]
    elif current_dir == "W":
        current_cor = [current_cor[0] - 1, current_cor[1]]
    elif current_dir == "E":
        current_cor = [current_cor[0] + 1, current_cor[1]]
    print(current_cor)

    check()# Check if the current position is a decision point and take appropriate action
    F = hamster.left_proximity()
    R = hamster.right_proximity()

    # Check if there's an obstacle in front or on the right
    if F > 55 or R < 30:
        scan()
        choice = make_decision()
        opens.clear()

        # Change direction based on the chosen option
        if choice == "B":
            if current_dir == "N":
                current_dir = "S"
            elif current_dir == "S":
                current_dir = "N"
            elif current_dir == "W":
                current_dir = "E"
            elif current_dir == "E":
                current_dir = "W"
            # print("turn back")
            hamster.turn_right(180, 50)
            print(current_dir)
            hamster.move_backward(2, 30)

        if choice == "L":
            if current_dir == "N":
                current_dir = "W"
            elif current_dir == "S":
                current_dir = "E"
            elif current_dir == "W":
                current_dir = "S"
            elif current_dir == "E":
                current_dir = "N"
            # print("turn left")
            hamster.turn_left(90, 50)
            print(current_dir)

        #if choice is right then change current directory
        if choice == "R":
            if current_dir == "N":
                current_dir = "E"
            elif current_dir == "S":
                current_dir = "W"
            elif current_dir == "W":
                current_dir = "N"
            elif current_dir == "E":
                current_dir = "S"

            # print("turn right")
            hamster.turn_right(90, 50)
            print(current_dir)
        if choice == "F":

            # print("go straight")
            print(current_dir)
            pass
    else:
        pass
    # print("\n")
    
    wait(400)
