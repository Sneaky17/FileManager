import os, shutil, sys, zipfile
import Operations


def menu():
    print("1) Copy and paste")
    print("2) Delete")
    print("3) Create new folder")
    print("4) Cut and move folder")
    print("5) Change name")
    print("6) Edit")
    print("7) Create ZIP copy")
    print("8) Extract ZIP")
    print("0) Exit")

def picking():
    choice = input('Pick option: ')
    if choice == "1":
        Operations.copy()
    elif choice == "2":
        Operations.deldir()
    elif choice == "3":
        Operations.mkdir()
    elif choice == "4":
        Operations.move()
    elif choice == "5":
        Operations.rename()
    elif choice == "6":
        Operations.edit()
    elif choice == "7":
        Operations.zip()
    elif choice == "8":
        Operations.extract()
    elif choice == "0":
        sys.exit(0)
    else:
        print ("Invalid choice!")


