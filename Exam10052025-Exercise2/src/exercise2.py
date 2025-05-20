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
    


class UserManager:
    def __init__(self):
        self.__users = {}
        self.__log = []

    def add_user(self, username: str):
        if username not in self.__users:
            self.__users[username] = User(username)
        else:
            raise ValueError("User already exists")
        
    def check_in(self, username:str, time: int):
        if username in self.__users:
            try:
                self.__users[username].check_in(time)
                if self.__users[username].checked_in() == True:
                    self.__log.append(self.__users[username]._User__format(time))
                    return True
            except:
                return False
        else: 
            raise ValueError("Invalid username")
        
    def check_out(self, username:str, time: int):
        if username in self.__users:
            try:
                self.__users[username].check_out(time)
                if self.__users[username].checked_in() == False:
                    self.__log.append(self.__users[username]._User__format(time))
                    return True
            except:
                return False
        else:
            raise ValueError("Invalid username")
        
    def load_log(self):
        with open("logfile.csv") as logs:
            for line in logs:
                line = line.replace("\n","")
                action = line.split(";")
                timestamp = action[0]
                user_name = action[1]
                status = action[2]
                if user_name not in self.__users:
                    self.add_user(user_name)
                    if status == "checkIn":
                        self.check_in(user_name,timestamp)
                    if status == "checkOut":
                        self.check_out(user_name,timestamp)


    def save_log(self):
        with open("logfile.csv", "w") as file:
            for action in self.__log:
                file.write(action+"\n")
    
    def __str__(self):
        for log in self.__log:
            return f"{log}"

if __name__ == "__main__":
    manager = UserManager()

    manager.add_user("Tom")

    print(manager.check_in("Tom", 12))

    try:
        print(manager.check_in("Jerry", 12))
    except ValueError as error:
        print(error)

    try:
        print(manager.check_out("Jerry", 12))
    except ValueError as error:
        print(error)

    manager.add_user("Jerry")

    print(manager.check_out("Tom", 18))
    print(manager.check_in("Jerry", 11))
    print(manager.check_in("Jerry", 19))

    try:
        manager.add_user("Tom")
    except ValueError as error:
        print(error)

    print(manager.check_out("Jerry", 19))
    print(manager.check_out("Jerry", 20))
    
    print(manager.save_log())

    print(manager.load_log())























