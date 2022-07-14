# Tristan Caetano
# DS Mouse Mover

# Importing Libraries
import pyautogui as pag
import keyboard

# Function to reset the mouse position
def reset_pos(center, hold_click):
    # CENTER 1437, 525
    if hold_click:
        pag.mouseUp()

    pag.moveTo(center[0], center[1])

    if hold_click:
        pag.mouseDown()


# Setting screen limits for the location of the game
def screen_loop(limits, stop_char, center_point, hold_click):

    # TOP Y = 164
    tlimitY = limits[0]

    # BOTTOM Y = 936
    blimitY = limits[1]

    # LEFT X = 960
    llimitX = limits[2]

    # RIGHT X = 1917
    rlimitX = limits[3]

    # If the centerpoint is to be set automatically
    if center_point == -1:
        center_point = [((llimitX + rlimitX) / 2), ((tlimitY + blimitY) / 2)]

    # Value that keeps the loop going until m is pressed
    keep_loop = True

    # While loop that resets mouse potitions
    while keep_loop:

        # Holding down the mouse button for touch screen
        if hold_click:
            pag.mouseDown()

        # Check left limit
        if pag.position()[0] < llimitX:
            reset_pos(center_point, hold_click)
            print("Far Left")

        # Check right limit
        elif pag.position()[0] > rlimitX:
            reset_pos(center_point, hold_click)
            print("Far Right")

        # Check top limit
        elif pag.position()[1] < tlimitY:
            reset_pos(center_point, hold_click)
            print("Far Top")

        # Check bottom limit
        elif pag.position()[1] > blimitY:
            reset_pos(center_point, hold_click)
            print("Far Bottom")

        # If m is pressed, program stops
        if keyboard.is_pressed(stop_char):
            keep_loop = False