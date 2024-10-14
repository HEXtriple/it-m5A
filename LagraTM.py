import time as t
import os
class User:
    def __init__(self, name, psswd):
        self.name = name
        self.psswd = psswd
        self.lager = []

    #Kollar användardetaljer i självaste klassen för att inte behöva exponera alla användares lösenord när systemet kolla inlogg
    def check_user_details(self, input_name, input_psswd):
        return True if self.name == input_name and self.psswd == input_psswd else False

    #Flertal abstraktioner så att dessa kan testas enskilt, samt tillåter upprepade användningar
    def add_item(self, vara):
        self.lager.append(vara)

    def remove_item(self, vara):
        self.lager.remove(vara)

    def return_details(self):
        return f"User: {self.name}, Psswd: {self.psswd}"
        
    def return_lager(self):
        return self.lager

#Här läggs en test användare till, som instruktionerna velat ha vid testning
test_user = User("NisseNisseNils", "123")
test_user.lager.append("Gurka")
users = []
users.append(test_user)
current_user = User(None, None)

def start_page():
    print("----------------------")
    print("Welcome to Lagra (TM)!")
    print("----------------------")
    print("1) Login")
    print("2) Create account")
    print("q) Quit")
    while True:
        choice = input("> ")
        match choice:
            case "1":
                return 1
            case "2":
                return
            case "q":
                quit()
            case _:
                print("Please enter valid input")
        
#Går igenom  listan med personer och kollar först om namnet stämmer överens med listans namn, och sedan om id och lösen stämmer
def login():
    print("---------------")
    print("Please enter details")
    user_name = str(input("User: "))
    user_passwd = str(input("Password: "))  
    for user in users:
        if user_name == user.name:
            # Tillåter några försök med med lösenordet 
            i = 1
            while i < 3:
                check = user.check_user_details(user_name, user_passwd)
                if check:
                    print(f"Välkommen {user.name}")
                    return user
                else: 
                    i +=1
                    print(f"password incorrect, you have {4-i} tries left")
                    user_passwd = str(input("Re-enter password: "))
                    continue
            print("To many wrong tries")
            return None
           
        else:
            continue
    print()
    print("Unable to find user")
    t.sleep(2)
    os.system('clear')
    return None

# Abstraktion, egen funktion för skapandet av nya konton
def create_account():
    print("---------------")
    print("Please enter details")
    user_name = str(input("User: "))
    user_passwd = str(input("Password: "))
    new_user = User(user_name, user_passwd)
    users.append(new_user)
    print(new_user.return_details(), "has been created")

#SAR A-Alternativ, låter användaren välja mellan förutsatta funktioner som interagerar med klassen
# "switch case" eller match-case användes för selektoren då det bara är en simpel input
def action(user):
    print("Select an action")
    print("1) Add item")
    print("2) Remove item")
    print("3) Log out")
    choice = input("")
    match choice:
        case "1":
            itemToAdd = input(">")
            user.add_item(itemToAdd)
        case "2":
            index = int(input("Index of item: ")) - 1
            if(index < 0 or index >= len(user.lager)): #Kollar så att man inte väljer ett objekt som inte är inom arrayen
                print("Invalid index")
                return
            itemToRemove = user.lager[index]
            user.remove_item(itemToRemove)
        case "3":
            global current_user
            current_user = None
        case _:
            print("Invalid input")

    print("---------------------")
        


def enter_lager(user):
    item_order = 0
    print("Items:")
    for item in user.return_lager():
        item_order += 1
        print(f"{item_order}) {item}")
    print("-------------------")
    action(user)

#Driftsatt system med en while loop för oändlig körning, inget basfall då funktionen quit() används för att stänga programmet
def system():
    global current_user
    current_user = None
    while True:
        if current_user != None:
            enter_lager(current_user)
        else:
            user_input = start_page()
            current_user=login() if user_input == 1 else create_account()
    
    
system()