class User:
    def __init__(self,username: str):
        self.__username = username
        self.__checked_in = False

    def checked_in(self):
        return self.__checked_in
    
    def __format(self, timestamp: int):
        if self.checked_in() == True:
            return f"{timestamp};{self.__username};CheckIn"
        else :
            return f"{timestamp};{self.__username};CheckOut"
            
    
    def check_in(self, time:int):
        if self.__checked_in == False:
                self.__checked_in = True
                return self.__format(time)
        else:
            raise ValueError("User has already been checked in")

    def check_out(self, time:int):
        if self.__checked_in == True:
                self.__checked_in = False
                return self.__format(time)
        else: 
            raise ValueError("User has not been checked in")

    def __str__(self):
        return f"{self.__username}"
    

if __name__ == "__main__":
    user1 = User("George")
    user2 = User("John")

    print("User 1:", user1)
    print("User 2:", user2)

    print(user1.check_in(12))
    print(user1.check_out(19))

    try:
        user1.check_out(19)
    except ValueError as error:
        print(error)

    try:
        user2.check_out(19)
    except ValueError as error:
        print(error)

    print(user2.check_in(20))

    try:
        user2.check_in(20)
    except ValueError as error:
        print(error)