#  ------Mini Project of Exception and File Handling------
from pathlib import Path
import os

def readFileandFolder():
    path = Path('')
    items = list(path.rglob('*'))
    for i,items in enumerate(items):
        print(f"{i+1}: {items}.")

def createFile():
    try:
        readFileandFolder()
        name = input("Please tell your file name:")
        p = Path(name)
        if not p.exists():
            with open(p,'w') as fs:
                data = input("What you want to write in this file:")
                fs.write(data)
            print("File created sucessfully.")
        else:
            print("File already exist.")
    except Exception as err:
        print(f"An error occured as {err}.")

def readFile():
    try:
        readFileandFolder()
        name = input("Please tell which file do you wanna read:")
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p,'r') as fs:
                data = fs.read()
                print(data)
            print("Readed sucessfully.")
        else:
            print("File does not exist.")
    except Exception as err:
        print(f"An error occured as {err}.")

def updateFile():
    try:
        readFileandFolder()
        name = input("Tell which file you want update:")
        p = Path(name)
        if p.exists() and p.is_file():
            print("Press 1 for changing the name of your file.")
            print("Press 2 for overwriting the data of your file.")
            print("Press 3 for appending content in your file.")
            res = int(input("Please tell your response:"))
            if res == 1:
                name2 = input("Tell your new file name.")
                p2 = Path(name2)
                p.rename(p2)
                print("File updated sucessfully.")
            if res == 2:
                with open(p,'w') as fs:
                    data =  input("Tell what you want to write:")
                    fs.write(data)
                print("File updated sucessfully.")
            if res == 3:
                with open(p,'a') as fs:
                    data =  input("Tell what you want to write:")
                    fs.write("\n" + data)
                print("File updated sucessfully.")
    except Exception as err:
        print(f"An error occured as {err}.")

def deleteFile():
    try:
        readFileandFolder()
        name = input("Which file you want to delete:")
        p = Path(name)
        if p.exists() and p.is_file():
            os.remove(p)
            print("File deleted sucessfully.")
        else:
            print("No such file exists.")
    except Exception as err:
        print(f"An error ocurred as {err}")

while True:
    print("--Main Meun--")
    print("Press 1 to create a file.")
    print("Press 2 to read a file.")
    print("Press 3 to update a file.")
    print("Press 4 to delete a file.")
    print("Press 5 to exit.")
    res = int(input("Please tell your response:"))
    if res == 1:
        createFile()
    elif res == 2:
        readFile()
    elif res == 3:
        updateFile()
    elif res == 4:
        deleteFile()
    elif res == 5:
        break
    else:
        print("Invaild response. Please enter between 1-5.")

        