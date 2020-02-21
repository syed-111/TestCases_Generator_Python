import random;
import string;
file_name=input("Enter your File name:");
file_name+=".txt";
f= open(file_name,"w+");
t=int(input("Enter number of test cases:"));
if(t>1):
    f.write(str(t)+"\n");
print("Select your choice\n1.array\n2.string");
c=int(input())
if(c==1):
    max_size=int(input("Enter max size of array:"));
    min_value=int(input("Enter min value of array:"));
    max_value=int(input("Enter max value of array:"));
    while t:
        array_size=random.randint(1, max_size);
        f.write(str(array_size)+"\n");
        while(array_size):
            value=random.randint(min_value, max_value);
            f.write(str(value)+" ");
            array_size-=1;
        t-=1;
        f.write("\n");
if(c==2):
    cc=int(input("Enter your choice\n1.lowercase\n2.uppercase\n3.lowercase and uppercase\n4.numeric string\n5.binary string\n6.lowercase,uppercase and numberic\n"));
    s="";
    max_size=int(input("Enter max size of String:"));
    if(cc==1):
        s=string.ascii_lowercase;
        print(s);
        ma=25;
    elif(cc==2):
        s=string.ascii_uppercase;
        ma=25;
    elif(cc==3):
        s=string.ascii_lowercase;
        s+=string.ascii_uppercase;
        ma=51;
    elif(cc==4):
        s=string.digits;
        ma=9;
    elif(cc==5):
        s+="0";
        s+="1";
        ma=1;
    else:
        s=string.ascii_lowercase;
        s+=string.ascii_uppercase;
        s+=string.digits;
        ma=61;
    while t:
        str_length=random.randint(1,max_size);
        f.write(str(str_length)+"\n");
        while str_length:
            value=random.randint(0,ma);
            value%=(ma+1);
            f.write(s[value]);
            str_length-=1;
        f.write("\n");
        t-=1
f.close()
