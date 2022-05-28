# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

# To check whether two words are anagrams
def find_anagram(word, anagram):

    word = str(input("Enter a word: "))
    anagram = str(input("Enter another word: "))

    if sorted(word) == sorted(anagram):
        return True
    else:
        return False