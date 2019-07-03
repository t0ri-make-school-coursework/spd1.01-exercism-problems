#!python
from string import ascii_lowercase

def pangram(words):
    """Determine if a sentence is a pangram, a sentence using 
    every letter of the alphabet at least once."""
    alphabet = {key: 0 for (key) in list(ascii_lowercase)}
    for char in list(words):
        if char in alphabet:
            alphabet[char] += 1
    if 0 in alphabet.values():
        return False
    return True
  
def main():
    print(pangram('the quick brown fox jumps over the lazy dog'))


if __name__ == "__main__":
    main()
    


