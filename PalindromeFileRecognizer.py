from PalindromeRecognizer import check_palin

def PaliF(f):
    file = open(f)
   # for line in file.read().split('\n'):
    #    if check_palin(line):
     #       print line
    line = [i for i in file.read().split('\n') if i in check_palin(f)]
    print line
if __name__ == '__main__':
    PaliF('pyz.txt')
