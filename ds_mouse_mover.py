# Tristan Caetano
# DS Mouse Mover

# Importing libraries
import pyautogui
import keyboard
    
# Function to reset the mouse position
def reset_pos():
    # CENTER
    center_coor = [1437, 525]
    pyautogui.mouseUp()
    pyautogui.moveTo(center_coor[0], center_coor[1])
    pyautogui.mouseDown()

def screen_loop():
    # Setting screen limits for the location of the game

    # TOP Y = 164
    tlimitY = 164
        
    # BOTTOM Y = 398
    blimitY = 936

    # LEFT X = 960
    llimitX = 960

    # RIGHT X = 1917
    rlimitX = 1917

    # Value that keeps the loop going until m is pressed
    keep_loop = True

    # While loop that resets mouse potitions
    while keep_loop:

        # Holding down the mouse button for touch screen
        pyautogui.mouseDown()

        # Check left limit
        if pyautogui.position()[0] < llimitX:
            reset_pos()
            print("Far Left")

        # Check right limit
        elif pyautogui.position()[0] > rlimitX:
            reset_pos()
            print("Far Right")

        # Check top limit
        elif pyautogui.position()[1] < tlimitY:
            reset_pos()
            print("Far Top")

        # Check bottom limit
        elif pyautogui.position()[1] > blimitY:
            reset_pos()
            print("Far Bottom")

        # If m is pressed, program stops
        if keyboard.is_pressed("m"):
            keep_loop = False

# Function call to start loop
screen_loop()
    
