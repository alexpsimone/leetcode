# Return the number of different transformations among all the words, given a list of words.
# If empty list, will there be 1 or 0 transformations?
# If there's a letter/character not in the alphabet, should I handle it a certain way?
# Are the words sorted in a certain way (alphabetically, for instance)?

def uniqueMorseRepresentations(words: List[str]) -> int:

    morse_code_alphabet = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."];

    # Generate a dictionary of letters to morse code equiv.
    # Initialize an empty set that I'll use to store unique words.
    # Iterate through words list.
    # Initialize an empty string that I'll use to build translated words one by one.
    # At each word in words, iterate through each letter.
    # For each letter, concatenate the placeholder string with the next translated letter.
    # At the end of each word, add the string to the set.
    # Finally, return the length of the set.

