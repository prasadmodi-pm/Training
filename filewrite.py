def filewrt(filename,data):
    if filename is '':
        filename = 'pre_file.txt'
    else:
         with open(filename,'w+') as f:
            f.write(data)

filewrt(filename='pras.txt', data='This is')