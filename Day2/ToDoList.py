dict1 = {}
seNo = 0

while True:
    flag = input("you want to add a task if yes press Y else N : ")
    if(flag == 'Y'):
        task = input("enter task : ")
        seNo += 1
        dict1[seNo] = task
        print(dict1)
    else:
        print("Thank-you")
        break