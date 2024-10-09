class user:
    def __init__(self, name, psswd):
        self.name = name
        self.psswd = psswd
        self.lager = []

    def kolla_upgifter(self, input_name, input_psswd):
        return True if self.name == input_name and self.psswd == input_psswd else False
        
    

    def add_item(self, vara):
        self.lager.append(vara)
        def __str__(self):
            return f"Namn: {self.name}, Lager: {self.lager}"

    def return_details(self):
        return f"User: ({self.name}, Psswd {self.psswd})"

    def return_lager(self):
        return self.lager

test_user = user("NisseNisseNils", "123")
test_user.lager.append("Gurka")
users = []
users.append(test_user)


def start_page():
    print("----------------------")
    print("Welcome to Lagra (TM)!")
    print("----------------------")
    print("1) Login")
    print("2) Create account")
    print("q) Quit")

    while True:
        choice = input("> ")
        if int(choice) == 1:
            return 1
        elif choice == "q":
            quit()
        elif int(choice) == 2:
            return
        else:
            print("please enter valid input")
        

'''
def login_input(): 
    try:
        int(user_input)
        continue
    except:
        print("Invalid input")
        continue '''
def login():
    print("---------------")
    print("Please enter details")
    user_name = str(input("User: "))
    user_passwd = str(input("Password: "))
    
    for user in users:
        if user_name == user.name:
            while True:
                check = user.kolla_upgifter(user_name, user_passwd)
                if check:
                    print(f"Välkommen {user.name}")
                    return user
                else: 
                    print("password incorrect")
                    user_passwd = str(input("Re-enter password: "))
                    continue
            
        else:
            continue


def create_account():
    print("---------------")
    print("Please enter details")
    user_name = str(input("User: "))
    user_passwd = str(input("Password: "))


    new_user = user(user_name, user_passwd)
    users.append(new_user)

    print(new_user.return_details(), "has been created")


def action(user):
    print("Select an action")
    choice = input("")

def enter_lager(user):
    item_order = 0
    for item in user.return_lager():
        item_order += 1
        print(f"{item_order}) {item}")
    action(user)

def system():
    current_user = None
    system_is_running = True
    while system_is_running:
        if current_user != None:
            enter_lager(current_user)


        else:
            user_input = start_page()
            current_user=login() if user_input == 1 else create_account()
    
    
system()