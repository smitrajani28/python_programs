# class details:
#     def __init__(self,n,o):
#         self.name = n
#         self.occ = o
# a = details("smit", "student")
# print(a.name,a.occ)

# # decorator
# def greet(fx):
#     def mfx(*args,**kwargs):
#         print("hello")
#         fx(*args, **kwargs)
#         print("bye")
#     return mfx
# @greet
# def hello():
#     print("hello")
# @greet
# def sum1(a,b):
#     print(a+b)

# hello()
# sum1(2,3)



#getter and setter
# class class1:
#     def __init__(self,n,o):
#         self.name = n
#         self.occupation = o

#     @property 
#     def value1(self):
#         return self.name + " " +self.occupation

#     @value1.setter
#     def value1(self, new_value):
#         self.name = new_value


# a= class1("smit", "student")
# a.value1="karan"
# print(a.value1)

class c1:
    company = "poco"
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def show(self):
        print(f"hello {self.name} with salary of {self.salary}")

    # @classmethod
    # def change_company(cls,chn):
    #     cls.company = chn
    @classmethod
    def fromstr(cls, string):
        return cls(string.split("-")[0],string.split("-")[1])

string = "smit-120000"
e1 = c1.fromstr(string)
e1.show()
# e1.change_company("MI")
# e1.show()
# print(c1.company)