from time import sleep

MIN_CHR = 32
MAX_CHR = 126

def find_text(text, time):
    line = ""
    for c in text:
        for i in range(MIN_CHR, MAX_CHR + 1):
            guess = chr(i)
            print(line + guess)
            sleep(time)
            if guess == c:
                line += guess
                break   

def main():
    text = "Hello World!"
    find_text(text, 0.002)

if __name__ == "__main__":
    main()