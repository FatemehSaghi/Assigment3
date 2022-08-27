import random
num_ran = 0
 
List = []
New_List = []

while True:
    num_ran = random.randint(1,1000)
    List.append(num_ran)
    if len (List) == 20:
        break
print('first list : ',List)

for i in List:
    New_List.append(i ** 2)
    
print('The second list : ',New_List)
