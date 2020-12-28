# Return the number of different transformations among all the words, given a list of words.
# If empty list, will there be 1 or 0 transformations?
# If there's a letter/character not in the alphabet, should I handle it a certain way?
# Are the words sorted in a certain way (alphabetically, for instance)?
# 

def uniqueMorseRepresentations(words: List[str]) -> int:

    morse_code_alphabet = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."];
