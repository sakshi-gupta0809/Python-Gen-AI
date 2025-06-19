
# You have a dictionary attendance where each key is:
# pythonCopyEdit(Student ID, Course ID)
# And value is a list of attended dates.
# pythonCopyEditattendance = {
#     ("S001", "C101"): ["2025-06-01", "2025-06-08"],
#     ("S002", "C102"): ["2025-06-05"]
# }
# Task:
# Take user input for:
# Student ID
# Course ID
# New attendance date
# Update list or ask to create if key is new.

attendance = {
    ("S001", "C101"): ["2025-06-01", "2025-06-08"],
    ("S002", "C102"): ["2025-06-05"]
}

Student_ID = input("Enter the StudentId: ")
Course_ID = input("enter the Course Id: ")

key = (Student_ID,Course_ID)
if(key in attendance):
    newAttendence = input("Enter new attendence list: ")
    if(newAttendence not in attendance[key]):
        attendance[key].append(newAttendence)
        print(attendance)
    else:
        print("Date is already exists")
else:
    print("you do'nt have student_Id and course Id")
    flag = input("if you want to add a new record press 'Y' else 'N': ")
    if(flag == 'Y'):
        newAttendence = input("Enter new attendence list: ")
        attendance[key] = newAttendence
        print(attendance)
    else:
        print("Thank-you")
        



# attendance = {
#     ("S001", "C101"): ["2025-06-01", "2025-06-08"],
#     ("S002", "C102"): ["2025-06-05"]
# }

# def update_attendance():
   
#     student_id = input("Enter Student ID: ").strip()
#     course_id = input("Enter Course ID: ").strip()
#     new_date = input("Enter new attendance date (YYYY-MM-DD): ").strip()
#     # List1=[new_date]
#     key = (student_id, course_id)
   
   
#     if key in attendance:
       
#         if new_date not in attendance[key]:
#             attendance[key].append(new_date)
#             print(f"Attendance date  added  {attendance}.")
#         else:
#             print(f"Attendance date  already exists {attendance}.")
#     else:
#         # create = input(f"Record {key} not found. Create new entry? (yes/no): ").strip().lower()
#         choice=input("y or n")
#         if(choice=="y"):
#            attendance[key]=new_date
#         print("The new entry has been added")
#         print(attendance)  
   
   
#     print("\nUpdated Attendance Records:")
# update_attendance()