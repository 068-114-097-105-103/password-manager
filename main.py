import re
import os

# base directory where all the passwords are stored
BASE_DIR = "DIRECTORY_PATH_HERE"

# generate a list of all the files in the directory
FILES = os.listdir(BASE_DIR)


# main function to search for the site name in all the files
def main():
    i = input("Press 1 to search for a site\nPress 2 to add a new record\n")
    if i == "1":
        site = input("Enter the site name: ")
        find(site)
    elif i == "2":
        add()


def add():
    site = input("Enter the site name: ")
    url = input("Enter the URL: ")
    username = input("Enter the username: ")
    password = input("Enter the password: ")
    with open(BASE_DIR + "\\" + "My-pass.csv", "a") as f:
        f.write(f"\n{site},{url},{username},{password}")
    print("Record added successfully.")


def find(site_name):
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
            print("URL: ", data[0])
            print("Username: ", data[1])
            print("password: ", data[2])
            print("-------------------")


# main loop
print("Welcome to the Password Manager press Ctrl+C to exit the program.")
while True:
    try:
        main()
    except Exception as e:
        print("Error: ", e)
        continue
