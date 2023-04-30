from FileManager import *
from UserClass import user 
from project import project
import datetime
#function takes the data of project and creat instance from class project and save it  
def create_project():
    title=input("enter project title:\n")
    details=input("enter project description:\n")
    target=input("enter project target:\n")
#valdiate date and time format entered by the user
    while True :
        start_date=input("enter project start date :\n")
        end_date=input("enter project end date :\n")
        if datetime.datetime.strptime(start_date, "%Y-%m-%d %H:%M") and datetime.datetime.strptime(end_date, "%Y-%m-%d %H:%M"):
            break;
        else:
            print("Invalid date format")

    email=input("enter project creator email :\n")
    project_1=project(title,details,target,start_date,end_date,email) 
    save(project_1)
     
#function to view all projects that are saved in our database
def view_projects():
    arr = load_projects()
    for ele in arr:
        print(ele)

#function takes title of project drom the user then return the object of this project
def fetch_project():
    title=input("enter title of your project:\n")
    arr=load_projects()
    for obj in arr:
        if obj.title == title:
            return obj

#function takes the object of a project and object of current user and if the broject belongs to that user he can update it
def update_project(project_obj,user):
  
    if user.email == project_obj.email:
        new_project=create_project()
        edit(project_obj,new_project)
    else:
        print("you are not allowed to  update in this project")    


#function takes the object of a project and object of current user and if the broject belongs to that user he can delete it
def delete_project(project_obj,user):
    
    if user.email == project_obj.email:
        delete(project_obj)
    else:
        print("you are not allowed to  delete  this project")    


# main loop
current_user = None
while True:
    print("=== Main Menu ===")
    print("1. Register")
    print("2. Login")
    print("3. Create Project")
    print("4. View Projects")
    print("5. Edit Project")
    print("6. Delete Project")
    print("7. Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        user_1=user()
        user_1.registeration
        save(user_1)
    elif choice == 2:
        arr =load_users()
        current_user = user.login(arr)
    elif choice == 3:
        if current_user is None:
            print("You must be logged in to create a project")
        else:
            create_project()
    elif choice == 4:
        view_projects()
    elif choice == 5:
        if current_user is None:
            print("You must be logged in to edit a project")
        else:
            project_obj=fetch_project() 
            update_project(project_obj,current_user)
    elif choice == 6:
        if current_user is None:
            print("You must be logged in to delete a project")
        else:
            project_obj=fetch_project()
            delete_project(project_obj,current_user)
    elif choice == 7:
        break
    else:
        print("Invalid choice")
