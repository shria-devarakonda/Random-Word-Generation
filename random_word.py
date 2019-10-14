import sys
import random
import string

v = "aeiou"
c = "".join(set(string.ascii_lowercase) - set(v))
def generate_word(length):
    word = ""
    for i in range(length):
        if i % 2 == 0:
            word += random.choice(c)
        else:
            word += random.choice(v)
    return word
if __name__ == "__main__":
    try:
        count = int(sys.argv[1])
    except:
        count = 5

    try:
        length = int(sys.argv[2])
    except:
        length = 6

    for i in range(count):
        print(generate_word(length))
