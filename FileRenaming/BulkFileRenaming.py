import os
import datetime
import re

def read_in_files(destination):
    """Read in files from folder destination

    inputs:
        destination - folder location of files

    output:
        file_list - list of all files in destination
    """

    if os.path.isdir(destination):
        file_list = os.listdir(destination)
    else:
        raise Exception(f"{destination} is not a valid folder")

    if not file_list:
        raise Exception("No files found in folder")

    return file_list

def remove_directories(destination, object_list):
    """remove directories from file_list

    inputs:
        file_list - a list of all found files in directory

    outputs:
        file_list -  a list of only files in directory
    """

    file_list = []

    for object in object_list:

        object_destination = os.path.join(destination, object)

        if os.path.isfile(object_destination):
            file_list.append(object)

    return file_list


def remove_old_time(old_string):
    """Remove old time and date from old_string

    inputs:
        old_string - string that we want to remove old date from

    outputs:
        cleaned_string - string cleaned
    """

    #set string to match as used data format
    #assumes date format that we specified later in the program
    string_to_match = "\d+d\d+m\d+y-\d+h\d+m\d+s_"
    cleaned_string = re.sub(string_to_match, "", old_string)

    return cleaned_string

if __name__ == "__main__":

    destination_folder = "files_to_rename"

    #read in all objects
    destination_objects = read_in_files(destination_folder)
    #remove subdirectories from list
    destination_files = remove_directories(destination_folder, destination_objects)

    #read in datetime
    current_datetime = datetime.datetime.now()
    #change to a valid string to prefix files
    current_datetime_str = current_datetime.strftime("%dd%mm%Yy-%Hh%Mm%Ss")

    #clean file names
    cleaned_file_names = {file:remove_old_time(file) for file in destination_files}

    #rename files
    files_renamed = {original_file_name:current_datetime_str + "_" + cleaned_file_name
                     for original_file_name, cleaned_file_name in cleaned_file_names.items()}

    #rename files in location
    for key, value in files_renamed.items():

        original_name = os.path.join(destination_folder, key)
        new_name = os.path.join(destination_folder, value)

        os.rename(original_name, new_name)