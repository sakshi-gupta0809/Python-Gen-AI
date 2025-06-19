
# Manage Component-Level Error Logs Using Tuples as Dictionary Keys  You will manage a dictionary that stores error logs for different operations of different modules in different applications. Each key in the dictionary is a tuple:
# (App Name, Module Name, Operation)
# Each value is a list of error messages                                                                                                                                   error_logs = {
#     ("App1", "Login", "submit"): ["timeout", "invalid credentials"],
#     ("App1", "Dashboard", "load"): ["data not found"],
#     ("App2", "Server", "memory"): ["memory leak", "threshold crossed"]
# }                                                                                                                                                                                                           Ask the user to input:
# App name
# Module name
# Operation name
# A new error message to add                                                                                                                                           Check if the Key Exists in the Dictionary
# If it exists, append the new error to the existing list.
# If it does not exist, ask the user if they want to create a new entry. If yes, create the entry with the error message as a new list. 


error_logs ={
    ("App1", "Login", "submit"): ["timeout", "invalid credentials"],
    ("App1", "Dashboard", "load"): ["data not found"],
    ("App2", "Server", "memory"): ["memory leak", "threshold crossed"]
}

App_name = input("Enter App Name:")
Module_name = input("Enter Module Name:")
Operation_name = input("Enter Operation name:")

key = (App_name,Module_name,Operation_name)

if(key in error_logs):
    errorMessage = input("Enter new error message:")
    error_logs[key].append(errorMessage)
    print(error_logs)
else:
    print("App name, Module name and Operation name is not exist")  
    flag = input("you want to create a new entry for it if yes press Y else N:")
    if(flag == 'Y'):
        errorMessage = input("Enter new error message:")
        error_logs[key] = errorMessage
        print(error_logs)
    else:
        print("Thank-you")