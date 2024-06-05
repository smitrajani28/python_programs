question = ["who is sachin tendulkar?", "who is narendra modi?","who is our national animal of india?", "how many colors are there in our natonal flag?"]
option = ["a.cricketer\tb.footballer\nc.gamer\td.politition", "a.cricketer\tb.footballer\nc.gamer\td.politition","a.peacock\tb.cock\nc.hen\td.crow", "a.1\tb.2\nc.3\td.4"]
limit=[1,3]
price = [10,20,30,40]
answer = ["a","d","a","d"]
temp=0
total = 0
j=0
for i in range(4):
    print(question[i])
    print(option[i])
    ans = input("enter your answer :")
    if(answer[i]==ans):
        if(i==limit[j]):
            total=price[i]
            j=j+1
        temp=price[i]
        txt ="you get price of {} rupees"
        print(txt.format(temp))
    else:
        txt ="you get price of {} rupees"
        print(txt.format(total))
        break
    print("----------------------------------------")