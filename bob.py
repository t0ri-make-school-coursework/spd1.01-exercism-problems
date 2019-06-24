"""
Bob is a lackadaisical teenager. In conversation, his responses are very limited.

Bob answers 'Sure.' if you ask him a question.
He answers 'Whoa, chill out!' if you yell at him.
He answers 'Calm down, I know what I'm doing!' if you yell a question at him.
He says 'Fine. Be that way!' if you address him without actually saying anything.
He answers 'Whatever.' to anything else.
"""
import sys

def analyze_string(text):
    empty = False
    question = False
    upper = True

    # If string is empty
    if text == ' ':
        empty = True
    
    # If string ends in '?'
    if text[len(text) - 1] == '?':
        question = True
    
    # If string has lowercase letters
    for character in text:
        if character.islower():
            upper = False

    # Return list of bools
    return [empty, upper, question]


def bob_says(text):
    # Get bools for text input
    results = analyze_string(text)
    
    # If the string is...
    if results[0]: # empty
        return 'Fine. Be that way!'
    if results[1] and results[2]: # an uppercase question
        return 'Calm down, I know what I\'m doing!'
    if results[1]: # uppercase
        return 'Whoa, chill out!'
    if results[2]: # a question
        return 'Sure.'
    else:
        return 'Whatever.'


def main():
    test_cases = [
        'Hey Bob, what\'s up?',
        'Bob? You listening?',
        'BOB?',
        'BOB!',
        ' ',
        'You suck, Bob.',
    ]
    for input in test_cases:
        print('{} \nBob says: {}'.format(input, bob_says(input)))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print('Bob says:', bob_says(sys.argv[1]))
    else:
        main()