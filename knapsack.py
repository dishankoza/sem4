def takeThird(lst):
    return(lst[2])
knapCap=int(input('enter the capacity of knapsack'))
profit=0
knapList=[]
l=[]
for i in range(int(input('enter the number of objects'))):
    l.append(input('enter profit and weight ').split())
    l[i]=list(map(int,l[i]))
    print(l)
    l[i].append(float(l[i][0]/l[i][1]))
l.sort(key=takeThird,reverse=True)
i=0
while(knapCap>0):
    if (knapCap<l[i][1]):
        r=float(knapCap/l[i][1])
        knapCap=0
        profit+=float(r*(l[i][0]))
        knapList.append(r)
        break
    knapList.append(1)
    knapCap-=l[i][1]
    profit+=l[i][0]
    i+=1
print('elements in kanpsack ',knapList)
print('profit is ',profit)