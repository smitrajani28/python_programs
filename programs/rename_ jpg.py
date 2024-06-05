import os
list1 = os.listdir("files")
os.chdir("files")
for i in range(1,len(list1)+1):
    n = str(i)+".png"
    print(n)
    os.rename(list1[i-1],n)
