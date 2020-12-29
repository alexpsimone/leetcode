# What about trailing spaces at the end of the list, like "Hello world   "

def lengthOfLastWord(s: str) -> int:
    
    words_list = (s.rstrip()).split(' ')

    if words_list == '':
        return 0
    else:
        return len(words_list[-1])

# print(clean_word)
# print(words_list)
print(lengthOfLastWord('Hello World'))
print(lengthOfLastWord('Hello World  '))
print(lengthOfLastWord('    '))