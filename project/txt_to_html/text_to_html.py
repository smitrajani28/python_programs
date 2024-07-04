import os
import re
import datetime


enter_path = input("Enter a path of folder where .txt files are located : ")
print("getting files from given location...")
allfiles = os.listdir(f"{enter_path}")
fname = [f for f in allfiles if f.endswith('.txt')]
print("extracting text from files...")
for i in range(len(fname)):
    with open(f"{enter_path}/{fname[i]}","r") as f1:
        lines = f1.read()
    editedlines = ""
    list1 = lines.split("\n")
    for j in range(len(list1)):
        paragraph = ""
        try:
            if list1[j].find("B-") >= 0:
                list1[j]= list1[j].replace("B-", "")
                list1[j] = "<b>" + list1[j] + "</b><br>"

            if list1[j].find("b-") >= 0:
                list1[j] = list1[j].replace("b-", "")
                list1[j] = "<li>" + list1[j] + "</li>"
            
            if list1[j].find("p-") >= 0:
                list1[j] = list1[j].replace("p-", "")
                if list1[j].find("-p") >= 0:
                    list1[j] = list1[j].replace("-p", "")
                    paragraph += list1[j]
                    
                else:
                    paragraph += list1[j]
                    k = j+1
                    while(list1[k].find("-p") < 0):
                        paragraph += " " + list1[k]
                        list1.pop(k)
                    list1[k] = list1[k].replace("-p", "")
                    paragraph += " " + list1[k]
                    list1.pop(k)

                list1[j] = "<p>&nbsp;&nbsp;&nbsp;&nbsp;" + paragraph + "</p>"
                

        except:
            pass

    count = 0
    for j in range(len(list1)):
        try:
            if ((not list1[j].startswith("<li>")) and (count > 0)):
                list1[j] = "</ul>" +list1[j] 
                count -=1
            elif ((list1[j].endswith("</li>")) and (j == len(list1)-1)):
                list1[j] =  list1[j] + "</ul>"
            if (list1[j].startswith("<li>")) and (count == 0):
                list1[j] = "<ul>" + list1[j]
                count +=1
        except:
            pass

    for j in range(len(list1)):        
        editedlines += list1[j] 

    filename = fname[i]
    filename = re.sub(r'\.txt$', '.html', filename)
    headpart = '''<html>
        <head>
        </head>
        <body>
        '''
    bottompart='''</body>
    </html>'''
    finaldoc = headpart + editedlines + bottompart

    datetime1 = datetime.datetime.now()
    today = f"{datetime1.year}-{datetime1.month}-{datetime1.day}"
    if not os.path.exists(f"{enter_path}/{today}"):
        os.mkdir(f"{enter_path}/{today}")
    f = open(f"{enter_path}/{today}/{filename}","w")
    f.write(finaldoc)
    print(f"{filename} converted successfully...")
print("converting process completed successfully...")
