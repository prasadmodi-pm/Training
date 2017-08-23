def Is_pangram(words):
    alphabets ="abcdefghijklmnopqrstuvwxyz"
    li = ""
    for letters in words:
        if letters in alphabets:
            li = li + letters

    for letters in alphabets:
        if letters not in li:
            print li +"     "+alphabets
            print letters
            return False

    return True

Is_pangram(words="Hi this is prasad")
