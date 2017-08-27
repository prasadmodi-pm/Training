def map_list_for(wd):
    leng = []
    for i in wd:
        leng.append(len(i))
    return leng

def map_list(wd):
    return map(len,wd)

def List_comp(wd):
    x = [len(l) for l in wd]
    return x

if __name__ == '__main__':
    wd = ["Rahul","Omkar","Shivam"]
    print map_list_for(wd)
    print map_list_for(wd)
    print List_comp(wd)
