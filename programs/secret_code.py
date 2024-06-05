import string
import random
while (True):
   print("what you want to do? :\n1.encode 2. decode 3. exit")
   choice = int(input("enter choice :"))
   if (choice < 1 or choice > 3):
       raise IndexError("value should be between 1 to 3")
   match choice:
      case 1:
         code = input("Enter a message : ")
         # code = "smit rajani"
         code1 = list(code.split())
         for i in range(len(code1)):
             if (len(code1[i]) > 2):
                 random1 = ''.join(random.choices(string.ascii_letters, k=3))
                 random2 = ''.join(random.choices(string.ascii_letters, k=3))
                 temp = code1[i][0]
                 code1[i] = code1[i][1:]
                 code1[i] = code1[i] + temp
                 code1[i] = random1 + code1[i] + random2
             else:
                 temp = code1[i][0]
                 code1[i] = code1[i][1:]
                 code1[i] = code1[i] + temp
         code = " ".join(code1)
         print(code)
         print("------------------------------------------------------")
      case 2:
         code = input("Enter a code : ")
         code1 = list(code.split())
         code2 = code1
         for i in range(len(code1)):
             if (len(code1[i]) > 2):
                 code1[i] = code1[i][3:-3]
                 temp = code1[i][len(code1[i])-1]
                 code1[i] = code1[i][:len(code1[i])-1]
                 code1[i] = temp + code1[i]
             else:
                 temp = code1[i][len(code1[i])-1]
                 code1[i] = code1[i][:len(code1[i])-1]
                 code1[i] = temp + code1[i]
         code = " ".join(code1)
         print(code)
         print("------------------------------------------------------")
      case 3:
         break
        