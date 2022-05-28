# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

# To check whether two words are anagrams
def find_anagram(word, anagram):

    if (sorted(word) == sorted(anagram)):
        return True
    else:
        return False

print(find_anagram("stone", "notes"))
