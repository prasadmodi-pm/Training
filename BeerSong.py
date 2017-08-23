def beer():
    b = "bottles of beer on the wall"
    be = "bottles of beer."
    ber ="Take one down, pass it around"

    for i in range(1,101):
        if i > 1:
            print i-1 , b , i-1, be , ber
beer()
