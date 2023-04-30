import FileManager
from UserClass import user 
user_1 = user("hasnm" , "das" , "das" , "das" , "das")
#user_1.save_user()
FileManager.save(user_1)
arr = FileManager.load_users()
for el in arr:
    print(el.f_name)