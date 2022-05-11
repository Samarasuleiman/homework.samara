import json
from pprint import pprint
print("x=3","y=6","z=4")
s=0
q1={}
l1=[]
asname=input("enter your name:")
with open("q.json","r") as f:
    q=json.loads(f.read())
    for i in q:
        print(i)
        var=input("enter the anser a or b:")
        l1.append(var)
        if var==q[i]:
            print("good")
            s=+1
        else:
            print("sory")
            s=s-1
    q1={asname:l1}      
    print(q1)
    print("end:",s)
