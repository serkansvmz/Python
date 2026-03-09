import random

def load_words():
    with open(r"C:\Users\SERKAN\Desktop\python\kendi projelerim\words.txt", "r", encoding="utf-8") as f:
        words = [line.strip() for line in f if line.strip()]
    return random.choice(words)


stages = [
"""
   -----
   |   |
   O   |
  /|\  |
  / \  |
       |
---------
""",
"""
   -----
   |   |
   O   |
  /|\  |
  /    |
       |
---------
""",
"""
   -----
   |   |
   O   |
  /|\  |
       |
       |
---------
""",
"""
   -----
   |   |
   O   |
  /|   |
       |
       |
---------
""",
"""
   -----
   |   |
   O   |
   |   |
       |
       |
---------
""",
"""
   -----
   |   |
   O   |
       |
       |
       |
---------
""",
"""
   -----
   |   |
       |
       |
       |
       |
---------
"""
]


def display_word(word, guessed):
    result = ""
    for letter in word:
        if letter in guessed:
            result += letter + " "
        else:
            result += "_ "
    return result


def hangman():

    word = load_words()
    guessed = []
    wrong = []
    lives = 6

    print("🎮 Welcome to Hangman")

    while lives > 0:

        print(stages[lives])
        print("Word:", display_word(word, guessed))
        print("Wrong letters:", wrong)

        guess = input("Guess a letter: ").lower()

        if guess in guessed or guess in wrong:
            print("⚠️ You already guessed that letter!")
            continue

        if guess in word:
            guessed.append(guess)
            print("✅ Correct guess!")
        else:
            wrong.append(guess)
            lives -= 1
            print(f"❌ Wrong guess! {lives} lives left.")

        if set(word) <= set(guessed):
            print("\n🏆 Congratulations! You guessed the word:", word)
            return

    print(stages[0])
    print("💀 Game Over! The word was:", word)


hangman()
