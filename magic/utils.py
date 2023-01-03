import random
import string

MIN_LENGTH = 6


def generate_random_string(length=MIN_LENGTH):
    return ''.join((random.choice(string.ascii_lowercase) for x in range(length)))
