from FileManager import *

class project:
    
    def __init__(self,title,details,target,start_date,end_date,email,donated=0):
        self.title = title
        self.details = details
        self.target = target
        self.start_date = start_date
        self.end_date = end_date
        self.email = email
        self.donated = donated
        

    def __eq__(self, other):
        if isinstance(other, project):
            return self.title == other.title and self.details == other.details and self.target == other.target and self.start_date == other.start_date and self.end_date == other.end_date and self.email == other.email
        return False    
    
    def __str__(self):
        return f"({self.title},{self.details},{self.target},{self.start_date},{self.end_date},{self.email},{self.donated})"




pro = project("a","b","c","d","e","f")
print(pro.donated)