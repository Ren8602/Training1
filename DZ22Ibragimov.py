from typing import List, Dict
l = []

def make_most_common_keys(d: Dict[int, int]) -> List[int]:

    for i in sorted(d.items(), key=lambda item: item[1], reverse=True):
        l.append(i)
    k = [i[0] for i in l]    
    return l

      
code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)



# d =  {5:3, 3:5, 0:2, 4:6, 7:10}
# print(make_most_common_keys(d))
# [7, 4, 3, 5, 0]