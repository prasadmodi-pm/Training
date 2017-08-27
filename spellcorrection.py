import re
def spellcor(string):
    string = re.sub(r'[.]([a-zA-Z])', r'. \1', string)
    string = re.sub(r'( )+', r'\1', string)
    return string
if __name__ == '__main__':
    print spellcor("This   is  very funny  and    cool.Indeed!")



