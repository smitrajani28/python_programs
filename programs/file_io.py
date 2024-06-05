# read
# f = open("requirement.txt","r")
# print(f.read())
# f.close()

# write
# f =open("sample.txt", "w")
# f.write("hello world")
# f.close()

# append
# f =open("sample.txt", "a")
# f.write("\ni am smit rajani")
# f.close()

#text and binary file
# 1)
# f = open("sample.txt", "rt")
# print(f.read())
# f.close()
# 2)
# f = open("sample.txt", "rb")
# print(f.read())
# f.close()

# with keyword
# with open("sample2.txt", "w") as f:
#     f.write("okay..............")

#readline
# f = open("sample.txt", "r")
# i = 0
# while True:
#     i +=1
#     line = f.readline()
#     if not line:
#         break
#     m1 = line.split(",")[0]
#     m2 = line.split(",")[1]
#     m3 = line.split(",")[2]
    
#     print(f"marks of student {i} is {m1}")
#     print(f"marks of student {i} is {m2}")
#     print(f"marks of student {i} is {m3}")
#     print("")
#     print("---------------------------------------------------------------------------------")
#     print("")

# writelines
# f = open("sample2.txt", "w")
# lines = ["1st\n", "2nd\n", "3rd\n"]
# f.writelines(lines)
# f.close()
# other method
# f = open("sample2.txt", "w")
# lines = ["1st", "2nd", "3rd", "4th", "5th"]
# for line in lines:
#     f.write(line+"\n")

# seek and tell
# f= open("sample.txt","r")
# f.seek(10)
# print(f.tell())
# data = f.read()
# print(data)

# truncate
f = open("sample2.txt", "a")
f.write("hello world")
f.truncate(38)