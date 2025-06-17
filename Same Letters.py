# Defines variable for first name
firstName = "Jazmin"

# Prompts user for sentence from user
sentence = input("Please enter your sentence here: ")

# Empty string to store letters
sameLetters = ""

# Initializes the letter counter for the first name
letterCount = 0

# For loop through the sentence
for char in sentence:
    if char.lower() in firstName.lower(): # Checks if letter in sentence
        sameLetters = sameLetters + char # Adds the letter found to the empty string
        letterCount = letterCount + 1 # Increases the number every time a letter is found
        
# Prints the total of all of the letters that were found
print(sameLetters)
print("There were " + str(letterCount) + " letters in the sentence from my first name - Jazmin.")