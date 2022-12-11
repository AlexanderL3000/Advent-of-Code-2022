with open("05Input.txt") as f:
    data = f.read()
f.close()

data = data.splitlines()    

lst = {}
for i in range(9):
    lst[i+1] = []


for item in data[:8]:
    item= item.replace("   ", "").split(" ")
    for i in range(len(item)):
        if item[i] != "":
            lst[i+1].append(item[i])


for item in data[10:]:
    
    item = item.split(' ')
    nums = item[1]

    fr = int(item[3])
    to = int(item[5])
    for i in range(int(nums)):
        lst[to].insert(0,lst[fr].pop(int(nums)-i-1))
    print(lst, sep = "\n")
 
for i in range(9):
    print(lst[i+1][0].replace("[","").replace("]",""), end = "")





    
