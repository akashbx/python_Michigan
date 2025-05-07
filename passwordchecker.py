# Password File Cracker

import zipfile
import time
from itertools import product

def open_dict_file():
    while True:
        try:
            name = input("Enter dictionary file name: ")
            return open(name, 'r')
        except FileNotFoundError:
            print("File not found.")

def open_zip_file():
    while True:
        try:
            name = input("Enter zip file name: ")
            return zipfile.ZipFile(name), name
        except FileNotFoundError:
            print("File not found.")
        except zipfile.BadZipFile:
            print("Bad zip file format.")

def brute_force_attack(zip_file):
    print("Brute Force Cracking")
    charset = 'abcdefghijklmnopqrstuvwxyz'
    for length in range(1, 9):
        for pwd_tuple in product(charset, repeat=length):
            pwd = ''.join(pwd_tuple)
            try:
                zip_file.extractall(pwd=pwd.encode())
                print("Brute force password is", pwd)
                return True
            except:
                continue
    print("Brute force failed.")
    return False

def dictionary_attack(zip_file, dict_file):
    print("Dictionary Cracking")
    for word in dict_file:
        pwd = word.strip()
        try:
            zip_file.extractall(pwd=pwd.encode())
            print("Dictionary password is", pwd)
            return True
        except:
            continue
    print("No password found.")
    return False

def main():
    print("Cracking zip files.")
    print("Warning: cracking passwords without permission is illegal under the Computer Fraud and Abuse Act")
    print("and may result in up to 10 years in federal prison.")

    while True:
        choice = input("What type of cracking ('brute force','dictionary','both','q'): ").lower()
        if choice == 'q':
            break
        elif choice == 'dictionary':
            dict_file = open_dict_file()
            zip_file, _ = open_zip_file()
            start = time.process_time()
            dictionary_attack(zip_file, dict_file)
            end = time.process_time()
            print("Elapsed time (sec):", round(end - start, 4))
            dict_file.close()
            zip_file.close()
        elif choice == 'brute force':
            zip_file, _ = open_zip_file()
            start = time.process_time()
            brute_force_attack(zip_file)
            end = time.process_time()
            print("Elapsed time (sec):", round(end - start, 4))
            zip_file.close()
        elif choice == 'both':
            dict_file = open_dict_file()
            zip_file, zip_filename = open_zip_file()
            start = time.process_time()
            success = dictionary_attack(zip_file, dict_file)
            end = time.process_time()
            print("Dictionary Elapsed time (sec):", round(end - start, 4))
            dict_file.close()
            zip_file.close()

            if not success:
                zip_file = zipfile.ZipFile(zip_filename)
                start = time.process_time()
                brute_force_attack(zip_file)
                end = time.process_time()
                print("Brute Force Elapsed time (sec):", round(end - start, 4))
                zip_file.close()
        else:
            print("Invalid choice.")


main()
