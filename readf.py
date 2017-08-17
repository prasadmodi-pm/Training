from filewrite import filewrt

def readfile():
    file = open('pras.txt','r+')
    print file.read()
readfile()


'''def copy(source,destin):
    with open(source, 'r+') as src, open(destin, 'w+') as dst:
        copy(src,dst)

copy(source='pras.txt',destin='pras.txt')'''