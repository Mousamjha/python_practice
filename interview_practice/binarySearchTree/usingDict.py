

class User:

    def __init__(self):
        self.users = []

    def insertion(self, username, user, email):
        i = 0
        while i < len(self.users):
            print("i: ", i)
            print("self.users[i]['username']: ", self.users[i]["username"], "and username: ", username)
            if self.users[i]["username"] > username:
                break
            i += 1
        self.users.insert(i, {"username": username, "user": user, "email": email})

    def find(self, username):
        for item in self.users:
            print("item: ", item)
            if item.get("username") == username:
                return item
        
    def update(self, username, user, email):
        target = self.find(username)
        print("target: ", target)
        target["username"], target["email"] = user, email

    def list_all(self):
        return [user["username"] for user in self.users]     

aakash = ('aakash', 'Aakash Rai', 'aakash@example.com')
u = User()
u.insertion(*aakash)
print(u.users)
dhiraj = ('dhiraj', 'Dhiraj Das', 'dhiraj@example.com')
u.insertion(*dhiraj)
print(u.users)
biraj = ('biraj', 'Biraj Das', 'biraj@example.com')
u.insertion(*biraj)
print(u.users)
print("biraj: ", u.find("biraj"))
u.update('biraj', "biraaj", "biraaj@emaple.com")
print("updated: ", u.users)
print(u.list_all())
# users.insert(aakash)
# print(users.users)
# aakash = User('aakash', 'Aakash Rai', 'aakash@example.com')
# biraj = User('biraj', 'Biraj Das', 'biraj@example.com')
# hemanth = User('hemanth', 'Hemanth Jain', 'hemanth@example.com')
# jadhesh = User('jadhesh', 'Jadhesh Verma', 'jadhesh@example.com')
# siddhant = User('siddhant', 'Siddhant Sinha', 'siddhant@example.com')
# sonaksh = User('sonaksh', 'Sonaksh Kumar', 'sonaksh@example.com')
# vishal = User('vishal', 'Vishal Goel', 'vishal@example.com')  
# aakash.insert
