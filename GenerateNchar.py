def generate_n_chars(n,c):
    st = ''
    for i in range(n):
        st = st + c
    return st
if __name__ == '__main__':
    print generate_n_chars(3,'b')