def overlap(list1, list2):
    for i in list1:
        for j in list2:
            if i == j:
                return True
    return False

if __name__ == '__main__':
   print overlap(list1=[1,2,3],list2=[4,2,5])