"""Given a phrase, count the occurrences of each word in that phrase.

For example for the input "olly olly in come free"

olly: 2
in: 1
come: 1
free: 1"""

def word_count(phrase):
    occurences = dict()
    for word in phrase.split(' '):
        if word in occurences:
            occurences[word] += 1
        else:
            occurences[word] = 1
    return occurences

def main():
    print(word_count('hey i love this problem'))
    print(word_count('code code code string'))


if __name__ == "__main__":
    main()