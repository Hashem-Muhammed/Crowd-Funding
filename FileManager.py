import pickle
from UserClass import user
from project import project

users_file = "Crowd-Funding/Files/users.pk"
projects_file = "Crowd-Funding/Files/projects.pk"


def save(object):
    myfile = ""
    print("Saving")
    caller = type(object)
    if caller is user:
        myfile = users_file
    if caller is project:
        myfile = projects_file

    if not myfile:
        raise Exception("Undefined caller")

    with open(myfile, "ab") as f:
        if object is not None:
            pickle.dump(object, f, pickle.HIGHEST_PROTOCOL)
            print("Saved to %s" % myfile)


def load_users():
    ls = []
    with open(users_file, "rb") as f:
        while True:
            try:
                a = pickle.load(f)
            except EOFError:
                break
            else:
                ls.append(a)
    return ls


def load_projects():
    ls = []
    with open(projects_file, "rb") as f:
        while True:
            try:
                a = pickle.load(f)
            except EOFError:
                break
            else:
                ls.append(a)
    return ls


def save_all(objects, myfile):
    with open(myfile, "wb") as f:
            for obj in objects:
                if obj is not None:
                    pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)


def delete(object):
    myfile = ""
    caller = type(object)
    if caller is user:
        myfile = users_file
        arr = load_users()
    if caller is project:
        myfile = projects_file
        arr = load_projects()
    arr.remove(object)
    save_all(arr, myfile)


def edit(oldobject, newobject):
    arr = load_projects()
    arr.remove(oldobject)
    arr.append(newobject)
    save_all(arr, projects_file)



