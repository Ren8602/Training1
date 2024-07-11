def av(a):
    a = list(map(int, s.split()))   
    average = sum(a) / len(a)
    return average 

b =[]

while s:=input():
    b.append(av(s))

for i in b:
    print(i)


  

