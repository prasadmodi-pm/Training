def translate():
    dict = {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"ar"}
    a = input("Enter in English: ")

    for k,v in dict.iteritems():
        if a in k:
            print v

translate()