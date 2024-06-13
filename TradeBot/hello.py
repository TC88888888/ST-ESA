import time
import sys

def typewriter_effect(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
    print()

if __name__ == "__main__":
    typewriter_effect("Hello")