def filewrt(filename,data):
   with open(filename,'w+') as f:
         f.write(data)

filewrt(filename='pras.txt', data='This is')