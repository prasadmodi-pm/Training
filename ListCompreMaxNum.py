li = [1,2,3,10,30,25,39,78,21,14]
print reduce(lambda x,y: x if x > y else y, li)
