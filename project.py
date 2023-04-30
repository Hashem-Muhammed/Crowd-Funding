from FileManager import *
import re
import datetime
class project:
    def __init__(self,title,details,target,start_date,end_date,email):
        self.title = title
        self.details = details
        self.target = target
        self.start_date = start_date
        self.end_date = end_date
        self.email = email

    def __eq__(self, other):
        if isinstance(other, project):
            return self.title == other.title and self.details == other.details and self.target == other.target and self.start_date == other.start_date and self.end_date == other.end_date and self.creator == other.creator
        return False    
    
    def __str__(self):
        return f"({self.title},{self.details},{self.target},{self.start_date},{self.end_date},{self.email})"

def create_project():
    t=input("enter project title:\n")
    d=input("enter project description:\n")
    t2=input("enter project target:\n")
    while True :
        s=input("enter project start date :\n")
        e=input("enter project end date :\n")
        if datetime.datetime.strptime(s, "%Y-%m-%d %H:%M") and datetime.datetime.strptime(e, "%Y-%m-%d %H:%M"):
            break;
        else:
            print("Invalid date format")

    c=input("enter project creator email :\n")
    project_1=project(t,d,t2,s,e,c) 
    save(project_1)
     
    
    
    
def view():
    print(load_projects())

def fetch_project():
    title=input("enter title of your project")
    arr=load_projects()
    for obj in arr:
        if obj.title == title:
            return obj

#project_obj=fetch_project()  

def update(project_obj,user):
  
    if user.email == project_obj.email:
        new_project=create_project()
        edit(project_obj,new_project)
    else:
        print("you are not allowed to  update in this project")    


def delete_project(project_obj,user):
    
    if user.email == project_obj.email:
        delete(project_obj)
    else:
        print("you are not allowed to  delete  this project")    
