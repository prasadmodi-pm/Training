import re
def verbing(v):
    es = ('o','ch','s','sh','x','z')
    if v.endswith('y'):
            return re.sub('y$','ies',v)
    elif v.endswith(es):
        return v + 'es'
    else:
        return v + 's'

if __name__ == '__main__':

    print verbing('try')
    print verbing('brush')
    print verbing('run')
    print verbing('fix')



