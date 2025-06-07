#Defining a class
class User:
    #Defining an attribute
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        #In this example, not necessary to put the parameter 'followers' bc it'll request the info unnecessarily later.
        self.followers = 0
        self.following = 0

    #Defining a method
    def follow(self, user):
        user.followers += 1
        self.following += 1

#Defining the objects
user_1 = User("001", "lucas")
print(user_1.id)
print(user_1.username)

user_2 = User("002", "john")
print(user_2.id)
print(user_2.username)

#Testing the method
user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
#--
print(user_2.followers)
print(user_2.following)
