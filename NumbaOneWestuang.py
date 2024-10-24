import tkinter as tk
import csv

class MenuItem:
    def __init__(self, n, p, t):
        self.name = n
        self.price = p
        self.time = t

#Abstraktion, separat funktion för FIFO kö
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        return self.queue.pop(0)

root = tk.Tk()
root.title("NumbaOneWestuang")
label = tk.Label(root, text="Welcome to NumbaOneWestuang")
label.pack(pady=10)

menu = []
with open('menu.csv', mode='r') as file:
    reader = csv.reader(file)    
    for row in reader:
        print(row)
        item = MenuItem(str(row[0]), int(row[1]), int(row[2]))
        menu.append(item)


cart = Queue() #Skapar en ny FIFO kö
cartLabel = tk.Label(root, text="Cart: ")
cartLabel.pack(pady=10)
readyLabel = tk.Label(root, text="Pickup ready: \n")
readyLabel.pack(pady=10)

def addItem(item):
    cart.enqueue(item)
    updateDisplay()

def updateDisplay():
    order = "Cart: "
    price = 0
    for i in menu:
        count = cart.queue.count(i)
        if(count > 0):
            order += i.name + "(" + str(count) + ") "
            price += i.price * count
    cartLabel.config(text=order + " \nTotal: " + str(price)+ " ")

#Rekursiv funktion
def confirmOrder():
    if len(cart.queue) == 0: #basfall
        return
    foo = cart.dequeue()
    #kör funktionen en gång i taget rekursivt istället för loop
    def update_label():
        bar = readyLabel.cget("text")
        bar += foo.name + "\n"
        readyLabel.config(text= bar)
        updateDisplay()
        # näste item
        confirmOrder()
    readyLabel.after(foo.time * 1000, update_label)
        
def system():
    for i in menu:
        buttonName = i.name + "\n" + str(i.price)
        b = tk.Button(root, text=buttonName, command= lambda item=i: addItem(item))
        b.pack(pady=10)
    confirmButton = tk.Button(root, text="Confirm order", command=confirmOrder)
    confirmButton.pack(pady=20)
    root.mainloop()
    
system()