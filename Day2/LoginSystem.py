userID = "sakshi-gupta"
pass1 = "Sakshi08"

attemps = 0
max_attemps = 3


while max_attemps!=0:
    userName = input("Enter userName:")
    password = input("Enter password:")

    if(userName != userID  and pass1 != password ):

        max_attemps -= 1
        print(f"""your user name and password are invalid, you have {max_attemps} attemps remaing""")
        
        # attemps += 1
        # print(attemps)
        # print("your user name and password are invalid")
        # if (attemps == max_attemps):
        #     break
    else:
        print("you have successfully login")
        break
       

