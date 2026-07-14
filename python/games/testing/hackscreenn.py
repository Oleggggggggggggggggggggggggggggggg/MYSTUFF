import random
import string
import time
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
RESET = '\033[0m'
# Pool includes letters, numbers, and symbols
character_pool = string.ascii_letters + string.digits + string.punctuation
print(f"{GREEN}START")
run = True
while run:
    random_characters = ''.join(random.choices(character_pool, k=100))
    print(random_characters)
    time.sleep(0.1)
