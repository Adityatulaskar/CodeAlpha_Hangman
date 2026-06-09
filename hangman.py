import random

# Words with categories and hints
WORDS = [
    {"word": "python",   "category": "Programming Language", "hint": "Created by Guido van Rossum"},
    {"word": "hangman",  "category": "Word Game",            "hint": "The game you are playing right now!"},
    {"word": "coding",   "category": "Programming Concept",  "hint": "Writing instructions for a computer"},
    {"word": "keyboard", "category": "Computer Hardware",    "hint": "You use this to type letters"},
    {"word": "program",  "category": "Programming Concept",  "hint": "A set of instructions run by a computer"},
]

HANGMAN_STAGES = [
    """
   -----
   |   |
   O   |
  /|\\  |
  / \\  |
       |
=========""",
    """
   -----
   |   |
   O   |
  /|\\  |
  /    |
       |
=========""",
    """
   -----
   |   |
   O   |
  /|\\  |
       |
       |
=========""",
    """
   -----
   |   |
   O   |
  /|   |
       |
       |
=========""",
    """
   -----
   |   |
   O   |
   |   |
       |
       |
=========""",
    """
   -----
   |   |
   O   |
       |
       |
       |
=========""",
    """
   -----
   |   |
       |
       |
       |
       |
=========""",
]

LETTER_HINT = "💡 Tip: Start with common letters → K, C, P, H, E, T, A, O, I, N, S, R"

def choose_difficulty():
    """Ask the player to choose a difficulty level."""
    print("\nChoose Difficulty:")
    print("  1. Easy   — Category + Hint + First letter revealed (9 wrong guesses)")
    print("  2. Medium — Category + First letter revealed (6 wrong guesses)")
    print("  3. Hard   — No hints at all (6 wrong guesses)")

    while True:
        choice = input("\nEnter 1, 2, or 3: ").strip()
        if choice == "1":
            return "easy", 9
        elif choice == "2":
            return "medium", 6
        elif choice == "3":
            return "hard", 6
        else:
            print("⚠️  Please enter 1, 2, or 3.")

def display_board(wrong_guesses, max_wrong, guessed_letters, word, difficulty, category, hint):
    """Display hangman stage, info, and word progress."""
    # Scale stage index to 6 stages regardless of max_wrong
    stage_index = round((wrong_guesses / max_wrong) * 6)
    stage_index = min(stage_index, 6)
    print(HANGMAN_STAGES[stage_index])

    print(f"Wrong guesses left: {max_wrong - wrong_guesses}")
    print(f"Guessed letters   : {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")

    # Show category and hint based on difficulty
    if difficulty in ("easy", "medium"):
        print(f"Category          : {category} 🏷️")
    if difficulty == "easy":
        print(f"Hint              : {hint} 💬")

    # Display word with blanks
    display_word = " ".join(letter if letter in guessed_letters else "_" for letter in word)
    print(f"\nWord: {display_word}\n")

def play_hangman():
    """Main game function."""
    print("=" * 45)
    print("          Welcome to HANGMAN! 🎮")
    print("=" * 45)

    difficulty, max_wrong = choose_difficulty()

    # Pick a random word
    entry = random.choice(WORDS)
    word     = entry["word"]
    category = entry["category"]
    hint     = entry["hint"]

    guessed_letters = set()
    wrong_guesses = 0

    # Easy/Medium: reveal first letter for free
    if difficulty in ("easy", "medium"):
        guessed_letters.add(word[0])
        print(f"\n✨ First letter revealed for free: '{word[0].upper()}'")

    print(f"\nThe word has {len(word)} letters. Good luck!\n")

    if difficulty == "hard":
        print(LETTER_HINT)

    while wrong_guesses < max_wrong:
        display_board(wrong_guesses, max_wrong, guessed_letters, word, difficulty, category, hint)

        # Check win
        if all(letter in guessed_letters for letter in word):
            print(f"🎉 Congratulations! You guessed the word: '{word.upper()}'")
            break

        guess = input("Guess a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("⚠️  Please enter a single letter.\n")
            continue

        if guess in guessed_letters:
            print(f"⚠️  You already guessed '{guess}'. Try a different letter.\n")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"✅ '{guess}' is in the word!\n")
        else:
            wrong_guesses += 1
            print(f"❌ '{guess}' is NOT in the word. ({max_wrong - wrong_guesses} guesses left)\n")

    else:
        display_board(wrong_guesses, max_wrong, guessed_letters, word, difficulty, category, hint)
        print(f"💀 Game over! The word was: '{word.upper()}'")
        print(f"   Category : {category}")
        print(f"   Hint     : {hint}")

    print()
    again = input("Play again? (yes/no): ").strip().lower()
    if again in ("yes", "y"):
        play_hangman()
    else:
        print("\nThanks for playing! Goodbye! 👋")

if __name__ == "__main__":
    play_hangman()
