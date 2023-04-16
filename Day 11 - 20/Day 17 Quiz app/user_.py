class User:
    def __init__(self, id, username):
        self.user = username
        self.id = id
        self.followers = 0
        self.following = 0

    def follow(self, user_):
        user_.followers += 1
        self.following += 1


user_1 = User(12, "aju")
user_2 = User(52, "umar")
# print(user_1.user)
# print(user_1.id)
user_1.follow(user_2)
print("umer",user_2.followers,"aju", user_1.following)
