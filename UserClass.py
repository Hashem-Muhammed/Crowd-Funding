import re

class user:
 
    def registeration(self):
        while True:
            name_regex='^[A-Za-z]+(?:\s[A-Za-z]+)*$'
            self.f_name=input("please enter your first name : ")
            if (re.search(name_regex,self.f_name)):
                self.l_name=input("please enter your last name : ")
                if (re.search(name_regex,self.l_name)):
                    regex = '^[a-z0-9]+[\._]?[ a-z0-9]+[@]\w+[. ]\w{2,3}$'
                    self.email=input("please enter your email: ")
                
                    if(re.search(regex,self.email)):
                        #print("valid mail")
                        self.password=input("please enter your password : ")
                        password_conf=input("please confirm your password : ")
                        if (password_conf==self.password):
                            mobile_regex = '^01[0125][0-9]{8}$'
                            self.mobile=input("please enter your phonr number:")
                        
                            if (re.search(mobile_regex,self.mobile)):
                                print("registeration done successfully =)")
                                break
                                
                                
                            else:
                                print("please enter valid phone number")
                                continue
                                

                        else:
                            print("not matching passwords")
                            continue
                                
                    else:
                        print("please enter valid email")
                        continue
                
                else:
                    print("lname entered is not a string")  
                    continue      
            
            else:
                print("fname entered is not a string")
                continue
        
       
    @staticmethod
    def login(arr):  #arr from saved file 
        while True:
            regex = '^[a-z0-9]+[\._]?[ a-z0-9]+[@]\w+[. ]\w{2,3}$'
            logEmail=input("please enter your email: ")
            logPassword=input("please enter your password : ")       
            if(re.search(regex,logEmail)):
               for elem in arr:
                    if elem.email==logEmail and logPassword == elem.password:
                            print("You have logged in successfully")
                            #print(f"Hello {elem.f_name} , you have logged in")
                            return elem
               else:
                   print("Invalid email or password")
                           
    def __eq__(self, other):
        return self.f_name==other.f_name and self.email == other.email    
         












  
        
        
        


