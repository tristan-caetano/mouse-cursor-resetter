# Tristan Caetano
# DS Mouse Mover

# Importing Libraries
from faulthandler import disable
from operator import truediv
import PySimpleGUI as sg
import pyautogui as pag
import ds_mouse_mover as dsmm
import keyboard
import save_load_config as slc
import os

# Getting limit values 
def getLimit(x_or_y, text, win):

    # Declaring init variable for return coordinate
    coor_set = 0

    # Finding the limits using mouse position
    while True:

        # Getting X and Y position of the mouse
        temp_coor = pag.position()
        
        # Update screen, and getting respective positions
        if x_or_y == "x":
            text.Update("X: " + str(temp_coor[0]))
            coor_set = temp_coor[0]
            win.refresh()
        elif x_or_y == "y":
            text.Update("Y: " + str(temp_coor[1]))
            coor_set = temp_coor[1]
            win.refresh()
        else:
            text.Update("Center: " + str(temp_coor[0]) + ", " + str(temp_coor[1]))
            coor_set = temp_coor
            win.refresh()
        
        # If m is pressed, program stops
        if keyboard.is_pressed("m"):
            return coor_set

# Main GUI function
def GUI():

    # Getting current dir
    current_dir = os.getcwd()

    # Holding text for buttons
    button_text = ["Top Limit Y", "Bottom Limit Y", "Left Limit X", "Right Limit X", "Centerpoint"]
    center_choice_txt = ["Auto Centerpoint", "Custom Centerpoint"]
    center_choice_button = sg.Button(center_choice_txt[0])

    # Holding limit values
    limits = [0,0,0,0]
    centerpoint = -1
    center_button = sg.Button(button_text[4])
    custom_center = False

    # Text boxes to hold values
    t_lim_text = sg.Text("Y: 0")
    b_lim_text = sg.Text("Y: 0")
    l_lim_text = sg.Text("X: 0")
    r_lim_text = sg.Text("X: 0")
    cen_text = sg.Text("Center: 0, 0")

    # Input text for filepath
    filepath_text = sg.InputText("NONE", key='-FILETEXT-')

    # Setting GUI layout
    layout = [[t_lim_text, b_lim_text, l_lim_text, r_lim_text, cen_text], 
            [sg.Button(button_text[0]), sg.Button(button_text[1]), sg.Button(button_text[2]), sg.Button(button_text[3]), center_button], 
            [center_choice_button, sg.Checkbox("Hold Left Click", default=True, key="-LEFT-")],
            [sg.Button("Start Looping"), sg.Button("Save Config")], 
            [sg.FileBrowse("Browse", initial_folder=current_dir, file_types = [("CSV Files", "*.csv")], key="-FILENAME-"), filepath_text, sg.Button("Load Config")]]

    # Create the window
    window = sg.Window("Mouse Looper", layout)

    # Create an event loop
    while True:
        event, values = window.read()

        # End program if user closes window
        if event == sg.WIN_CLOSED:
            break
        # Get top, bottom, left, and right limit values
        elif event == button_text[0]:
            limits[0] = getLimit("y", t_lim_text, window)
        elif event == button_text[1]:
            limits[1] = getLimit("y", b_lim_text, window)
        elif event == button_text[2]:
            limits[2] = getLimit("x", l_lim_text, window)
        elif event == button_text[3]:
            limits[3] = getLimit("x", r_lim_text, window)
        # Choice button for custom or auto centerpoint
        elif event == center_choice_txt[0]:
            if custom_center == False:
                centerpoint = -1
                cen_text.Update("Center: Auto")
                center_choice_button.Update(center_choice_txt[1])
                center_button.Update(disabled=True)
                custom_center = True
            elif custom_center == True:
                centerpoint = [0,0]
                cen_text.Update("Center: 0, 0")
                center_choice_button.Update(center_choice_txt[0])
                center_button.Update(disabled=False)
                custom_center = False
        # Starting the main program
        elif event == "Start Looping":
            dsmm.screen_loop(limits, "m", centerpoint, values['-LEFT-'])
        # Getting custom centerpoint
        elif event == button_text[4]:
            centerpoint = getLimit("cen", cen_text, window)
        values['FILETEXT'] = values['-FILENAME-']
        filepath_text.Update(values['-FILENAME-'])
            

        # Refreshing window for changes    
        window.refresh()

    # Closing window
    window.close()

# Starting program
GUI()