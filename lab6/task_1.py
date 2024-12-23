

class UserAccount: 
    
    
    def __init__(self: object, username: str, email: str, password: str) -> None:

        self.username = username
        self.email = email 
        self.__password = password

    
    def set_password(self: object, new_password: str) -> None:

        self.__password = new_password 

    def check_password(self: object, password: str) -> bool:

       return True if self.__password == password else False

 

ac = UserAccount("root", "root@local.local", "example")

ac.set_password("password")


print(ac.check_password("password"))
