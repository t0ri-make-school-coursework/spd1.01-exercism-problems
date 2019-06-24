"""
Convert a phrase to its acronym.
"""

def acronym(words):
    output = str()
    for word in words.split(' '):
        output += word[0].upper()
    return output


def main():
    test_inputs = [
      'Input 1',
      'Test Input Number Two',
      'A Final Input',
    ]
    for words in test_inputs:
        print('{}: {}'.format(words, acronym(words)))


if __name__ == "__main__":
    main()