import re
import os

# base directory where all the passwords are stored
BASE_DIR = "C:\\Users\\nick\\Documents\\passwords"

# generate a list of all the files in the directory
FILES = os.listdir(BASE_DIR)


# main function to search for the site name in all the files
def main(site_name):
    # dictionary to store the data
    d = {}
    # loop through all the files
    for file in FILES:
        # open the file
        with open(BASE_DIR + "\\" + file, "r") as f:
            # loop through all the lines in the file
            for line in f:
                # search for the site name in the line
                if re.search(site_name, line, re.IGNORECASE):
                    data = line.split(",")
                    # add the match to the dictionary
                    d.update({data[0]: data[1:]})

    # check for matches
    if len(d) == 0:
        print("No data found for the site.")
    # print the matches
    else:
        print(f"{len(d)} records found for the site.")
        print("-------------------")
        for key, data in d.items():
            print("Site: ", key)
            print("Username: ", data[0])
            print("Password: ", data[1])
            print("URL: ", data[2])
            print("-------------------")


# main loop
print("Welcome to the Password Manager press Ctrl+C to exit the program.")
while True:
    site = input("Enter the site name: ")
    try:
        main(site)
    except Exception as e:
        print("Error: ", e)
        break
