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

    def log_status(self):
        return self.__log

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
            for action in self.log_status():
                file.write(action+"\n")
    
    def __str__(self):
        for log in self.log_status():
            return f"{log}"
        

class UserInterface:
    def __init__(self):
        self.user_Manager = UserManager()

    def help(self):
        print("0 - Exit program")
        print("1 - Check in")
        print("2 - Check out")
        print("3 - Add user")
        print("4 - View log for user")
        print("5 - View log")

    def check_in_user(self):
        name = input("Username: ")
        time = input("Time: ")
        try:
            if self.user_Manager.check_in(name,time) == True:
                print("Checked in")
            else:
                print("User has already been checked in")
        except:
            print("Invalid Username")

    def check_out_user(self):
        name = input("Username: ")
        time = input("Time: ")
        try:
            if self.user_Manager.check_out(name, time) == True:
                print("Checked out")
            else :
                print("User has been already out")
        except:
            print("Invalid username")

    def add_user(self):
        name = input("Username: ")
        try:
            self.user_Manager.add_user(name)
            print("User creation succeeded !")
        except:
            print("User already exists")

    def user_log(self):
        name = input("Username: ")
        result = []
        for log in self.user_Manager.log_status() :
            if name ==  self.user_Manager.log_status()[1]:
                result.append(log)
        # print(result)
        if len(result) != 0 :
            for r in result :
                print(r)
        else:
            print(f"No logs for user {name}")

    def all_logs(self):
        if self.user_Manager.log_status() != 0:
            for log in self.user_Manager.log_status():
                print(log)
        else:
            print("Log is empty")

    def execute(self):
        self.help()
        while True:
            print("")
            cmd = input("Choose action: ")
            if cmd == "0":
                print("Closing program...")
                break
            elif cmd == "1":
                self.check_in_user()
            elif cmd == "2":
                self.check_out_user()
            elif cmd == "3":
                self.add_user()
            elif cmd == "4":
                self.user_log()
            elif cmd =="5":
                self.all_logs()
            else:
                self.help()

interface = UserInterface()
interface.execute()