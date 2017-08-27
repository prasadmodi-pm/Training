from random import randrange
def guess():
    a = randrange(1,20)
    print a
    while True:
        i = int(input("Take a guess"))
        if a < i:
            print "Your guess is too high", a

        elif a > i:
            print "Your guess is too low", a

        else:
            print "Good Job", a
            break

guess()