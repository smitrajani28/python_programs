class Solution:
    def reverseStr(s: str, k: int):
        temp = 0
        list1 = [char for char in s]
        for j in range(0,len(list1),2*k):
            for i in range(int(((k/2)))):
                print(i+j)
                temp = list1[i+j]
                list1[i+j] = list1[j+k-i-1]
                list1[j+k-i-1] = temp

        s = ''.join(list1)
        return s
    print(reverseStr("abcdefg",2))

        