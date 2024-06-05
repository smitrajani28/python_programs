
def split1(inputString):
    variable = inputString.split(">")
    return variable[0],variable[1],variable[2]

print(split1("smit>rajani>i "))