# Tristan Caetano
# DS Mouse Mover

# Importing Libraries
import csv

# Loading file
def load_file(load_path):

    # Getting file values
    file = open(load_path)
    loaded_vals = csv.reader(file)

    # Removing headers from loaded values
    header = next(loaded_vals)

    # Creating empty array to house the values
    all_items = []

    # Filling array with all values
    for item in loaded_vals:
        all_items.append(item)

    # Returning array
    return all_items[0]


# Saving file
def save_file(save_path, limits, center, left_click):

    # Getting saved file path
    file = open(save_path + ".csv", "w")
    file_to_write = (
        "top_lim_y, bottom_lim_y, left_lim_x, right_lim_x, cen_x, cen_y, hold_left\n"
    )

    # Creating string to be saved
    if center == -1:
        file_to_write += (
            str(limits[0])
            + ","
            + str(limits[1])
            + ","
            + str(limits[2])
            + ","
            + str(limits[3])
            + ",-1,-1,"
            + str(left_click)
        )
    else:
        file_to_write += (
            str(limits[0])
            + ","
            + str(limits[1])
            + ","
            + str(limits[2])
            + ","
            + str(limits[3])
            + ","
            + str(center[0])
            + ","
            + str(center[1])
            + ","
            + str(left_click)
        )

    # Saving file and closing
    file.write(file_to_write)
    file.close()
