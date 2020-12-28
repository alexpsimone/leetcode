# Return the number of different transformations among all the words, given a list of words.
# If empty list, will there be 1 or 0 transformations?
# If there's a letter/character not in the alphabet, should I handle it a certain way?
# Are the words sorted in a certain way (alphabetically, for instance)?

def uniqueMorseRepresentations(words: List[str]) -> int:

    morse_code_alphabet = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."];
    english_alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    if words == []:
        return 0
    
    # Generate a dictionary of letters to morse code equiv.
    english_to_morse = {}
    for idx, letter in enumerate(english_alphabet):
        english_to_morse[letter] = morse_code_alphabet[idx]
    # Initialize an empty set that I'll use to store unique words.
    unique_words = set()
    # Iterate through words list.
    for word in words:
    # Initialize an empty string that I'll use to build translated words one by one.
        translated_word = ''
        # At each word in words, iterate through each letter.
        for letter in word:
        # For each letter, concatenate the placeholder string with the next translated letter.
            translated_word += english_to_morse[letter]
        # At the end of each word, add the string to the set.
        unique_words.add(translated_word)
    # Finally, return the length of the set.
    return len(unique_words)

