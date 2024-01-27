#@author JotaV-0 | 2024

import time
import random
import sys
from pynput.keyboard import Key, Controller

FOLDER_PATH = "./texts/"

keyboard = Controller()

def select_file(FILE_PATH):
    if sys.argv[1] is None:
        FILE_PATH += "default"
    else:
        FILE_PATH += sys.argv[1]

    FILE_PATH += ".txt"

    return FILE_PATH

def wait(wait_time):
    print("Starting in ...")
    for i in range(wait_time):
        print(wait_time - i)
        time.sleep(1)

    print("Ready")


def write_line(line):
    for c in line:
      keyboard.type(c)
      time.sleep(random.uniform(0.0125, 0.005))
    
    keyboard.tap(Key.enter)
    time.sleep(0.125)


def spam(file_path):
    with open(file_path, "r") as text:
        for line in text:
            write_line(line.strip())

    print("Done")


def main():
    wait(5)
    spam(select_file(FOLDER_PATH))


if __name__ == "__main__":
    main()