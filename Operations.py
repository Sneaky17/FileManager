import os
import shutil
import zipfile
import sys
from stat import *
import time

def copy():
    decision = input("Do you want to copy 1) folder or 2)file? ")
    if decision == '1':
        folder_path = input("Specify folder path: ")
        folder_new_path = input("Specify destination: ")
        if os.path.exists(folder_path):
            if os.path.exists(folder_new_path):
                shutil.copytree(folder_path, folder_new_path)
                print("Done!")
            else:
                print("Destination path does not exist. Do you want to create it? y/n")
                dirdec = input().lower()
                if dirdec == 'y':
                    os.mkdir(folder_new_path)
                    shutil.copytree(folder_path, folder_new_path)
                    print("Done!")
                if dirdec == 'n':
                    sys.exit(0)
        else:
            print("Invalid path!")
    elif decision == '2':
        path = input("Specify file path: ")
        if os.path.exists(path):
            dst = input("Specify file destination: ")
            shutil.copy(path, dst)
            print('Copy successful!')
        else:
            print('File not found at %s' % path)

def deldir():
    print('Delete 1) single file or 2) whole folder?')
    choice = input()
    if choice == '1':

        path = input('Specify file path: ')

        if os.path.exists(path):
            os.remove(path)
        else:
            print('Invalid path!')
    elif choice == '2':
        path = input('Specify folder path: ')
        if os.path.exists(path):
            shutil.rmtree(path)
            print("Done!")
        else:
            print('Invalid path!')
    else:
        print('Invalid choice!')

def mkdir():
    path = input('Specify new dir path: ')

    if os.path.exists(path):
        print('Path already exists %s ' % path)
    else:
        os.makedirs(path)
        print('Dir successfully created %s ' % path)

def rename():
    path = input('Specify path to file: ')
    if os.path.exists(path):
        os.chdir(path)
        old_name = input('Specify file name: ')
        new_name = input('Give new file name: ')
        try:
            os.rename(old_name,new_name)
            print("Done!")
        except FileNotFoundError:
            print('File not found!')
    else:
        print("Invalid path!")

def zip():
    path = input('Specify path: ')
    new_path = input('Specify zip copy path: ')
    if os.path.exists(path):
        if os.path.exists(new_path):
            os.chdir(new_path)
            shutil.make_archive('zip_copy', 'zip', path)
            print("Done")
        else:
            print("Path for zip copy does not exists. Do you want to create it? y/n")
            decision = input().lower()
            if decision == 'y':
                os.mkdir(new_path)
                os.chdir(new_path)
                shutil.make_archive('zip_copy', 'zip', path)
                print("Done!")
            elif decision == 'n':
                print("Exiting...")
                sys.exit(0)
    else:
        print("Invalid path!")

def edit():
    print("Keep in mind that not all files can be edited using Notepad!")
    path = input("Specify file path: ")
    try:
        os.startfile(path)
    except FileNotFoundError:
        print("File not found!")

def extract():
    path = input('Specify path: ')
    if os.path.exists(path):
        new_path = input("Specify destination: ")
        if os.path.exists(new_path):
            shutil.unpack_archive(path, new_path, 'zip')
            print("Done!")
        else:
            print("Path for zip copy does not exists. Do you want to create it? y/n")
            decision = input().lower()
            if decision == 'y':
                os.mkdir(new_path)
                os.chdir(new_path)
                shutil.unpack_archive(path, new_path, 'zip')
                print("Done!")
            elif decision =='n':
                print("Exiting...")
                sys.exit(0)
    else:
        print("Invalid path!")

def move():
    path = input("Specify path to a file or folder you wish to move: ")
    if os.path.exists(path):
        dst = input("Specify destination: ")
        if os.path.exists(dst):
            shutil.move(path, dst)
            print("Done!")
        else:
            choice = input("Destination path does not exist. Do you want to create it? y/n").lower()
            if choice == 'y':
                os.mkdir(dst)
                shutil.move(path, dst)
                print("Done!")
            elif choice == 'n':
                print("Exiting...")
                sys.exit(0)
    else:
        print("Source path invalid!")


#TODO add dropbox support
