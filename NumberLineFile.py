import shutil
numb = []
for i in range(1,101):
    numb.append(str(i))
f = open('abc123.txt', 'w')
f.write('\n'.join(numb))
f.close()

c = shutil.copy('abc123.txt','xyz.txt')