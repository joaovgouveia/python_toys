#@author JotaV-0 | 2024

import drawing_handler as handler
import sys

def main():
    try:
        handler.draw(sys.argv[1])
        print("Done")
    except:
        print("Need a drawing name!")



if __name__ == "__main__":
    main()