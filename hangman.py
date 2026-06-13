import random

# 1. Words ki list - yahan apne words daal
words = ['ZARA', 'LAPTOP', 'PYTHON', 'GAMING', 'KANPUR', 'CODE']

# 2. Computer random word choose karega
word = random.choice(words)
guessed = ['_'] * len(word) # _ _ _ _ _ _ banayega
lives = 6 # 6 galti tak bachega

print("=== HANGMAN GAME ===")
print("Word:", ' '.join(guessed))
print(f"Tere paas {lives} lives hain 💖")

# 3. Jab tak lives hain aur word poora nahi hua
while lives > 0 and '_' in guessed:
    print("\n------------------")
    guess = input("Ek letter daal: ").upper()

    # Check karo letter word mein hai ya nahi
    if guess in word:
        print("✅ Sahi pakde hain!")
        # Sahi jagah pe letter daal do
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
    else:
        lives = lives - 1
        print(f"❌ Galat! {lives} lives bache")
        print("Hangman:", "O" if lives<=5 else "",
              "/|\\" if lives<=3 else "",
              "/ \\" if lives<=1 else "")

    print("Word:", ' '.join(guessed))

# 4. Result
if '_' not in guessed:
    print(f"\n JEET GAYA! Word tha: {word}")
else:
    print(f"\n GAME OVER! Word tha: {word}")