def max3(num1,num2,num3):
    if (num1 >= num2) and (num1 >= num3):
        print num1 ,"num1 Is graetest"
    elif (num2 >= num1) and (num2 >= num3):
        print num2, "num2 is greatest"
    else:
         print num3, "num3 is greatest"

max3(num1=299,num2=11,num3=15)