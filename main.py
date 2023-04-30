import FileManager
from UserClass import user 
# user_1 = user()
# user_1.registeration()
# FileManager.save(user_1)

arr = FileManager.load_users()
logged_in = user.login(arr)
print(logged_in.f_name)
