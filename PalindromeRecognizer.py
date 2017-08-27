from Palindrome import is_palindrome
import string

def check_palin(sentence):
    sentence = ''.join([i for i in sentence.lower().split()])
    sentence =''.join([j for j in sentence if j not in string.punctuation])

    return is_palindrome(sentence)

if __name__ == '__main__':
    print check_palin("Go hang a salami I'm a lasagna hog.")