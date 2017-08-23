def FilterL(L,n):
    lw = []

    for j in range(len(L)):
        if len(L[j]) > n:
            lw.append(L[j])
    print lw
FilterL(L = ['Rambhau','Ponu','Sonu',"Srikanth","Savitri","ramu"], n =5)
