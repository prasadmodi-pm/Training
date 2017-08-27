def frequency(f):
    fr = {key: 0 for key in f}
    for i in f:
        fr[i] +=1
    return fr

if __name__ == '__main__':
    print frequency("abbabcbdbabdbdbabababcbcbab")
