import random

words = [
    'cloud', 'grape', 'peach', 'mango', 'melon', 'shop', 'bag', 'laptop',
    'waste', 'olive', 'pear', 'prune', 'eat', 'light', 'chair', 'figs'
]

def generate_random_word(length):
    word = random.choice(words)
    while len(word) != length:
        word= random.choice(words)

    return word
def cows_and_bulls(secret_word, guess):
    cows = 0
    bulls = 0
    secret_list = list(secret_word)
    guess_list = list(guess)

    for i in range(length):
        if guess_list[i] == secret_list[i]:
            bulls += 1
            secret_list[i] = '-'
            guess_list[i] = '_'
    for i in range(length):
        if guess_list[i] in secret_list:
            cows += 1

    return cows, bulls


print("Welcome to the Cows and Bulls game with words!")
length = int(input("Enter the number of letters in the word you want to guess: "))
secret_word = generate_random_word(length)
print(f"A random {length}-letter word has been generated.")
print("Try to guess the word! You will get feedback in the form of 'Cows' and 'Bulls'.")
print("Bulls represent correct letters in the correct positions.")
print("Cows represent correct letters but in the wrong positions.")
attempts = 0
while True:
      guess = input(f"Enter your guess ({length} letters): ").lower()

      if len(guess) != length:
          print(f"Please enter a word with exactly {length} letters.")
          continue

      attempts += 1
      cows, bulls = cows_and_bulls(secret_word, guess)

      if bulls == length:
          print(f"Congratulations! You've guessed the word '{secret_word}' correctly in {attempts} attempts!")
          break
      else:
          print(f"{cows} Cows, {bulls} Bulls")
          print("Try again!\n")