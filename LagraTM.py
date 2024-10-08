class user():
    def __init__(self, name, psswd):
        self.name = name
        self.psswd = psswd
        self.lager = []
    def returnera_lager(self):
        return self.lager
    def lagg_till_vara_varor(self, vara):
        self.lager.append(vara)
        def __str__(self):
            return f"Namn: {self.name}, Lager: {self.lager}"
    def returnera_uppgifter(self):
        return f"User({self.name}, {self.psswd})"

test_user = user("John", "password")

def start_page():
    print("Welcome to Lagra (TM)!")
    print("1) Loggin")
    print("2) Create account")
    print("q) Quit")
    
    while True:
        choice = input("> ")
