import tkinter as tk
import time as t
from collections import deque


class MenuItem:
    def __init__(self, n, p, t):
        self.name = n
        self.price = p
        self.time = t

root = tk.Tk()
root.title("NumbaOneWestuang")
label = tk.Label(root, text="Welcome to NumbaOneWestuang")
label.pack(pady=10)
burger = MenuItem("burger", 100, 3)
cheeseburger = MenuItem("cheeseburger", 110, 5)
menu = {burger, cheeseburger}
cart = deque()
cartLabel = tk.Label(root, text="Cart: ")
cartLabel.pack(pady=10)
readyLabel = tk.Label(root, text="Pickup ready: \n")
readyLabel.pack(pady=10)

def addItem(item):
    cart.append(item)
    updateDisplay()

def updateDisplay():
    order = "Cart: "
    price = 0
    for i in menu:
        count = cart.count(i)
        if(count > 0):
            order += i.name + "(" + str(count) + ") "
            price += i.price * count
    cartLabel.config(text=order + " \nTotal: " + str(price)+ " ")

def confirmOrder():
    if len(cart) == 0:
        return
    foo_rstout = cart.popleft()
    #kör funktionen en gång i taget rekursivt istället för loop
    def update_label():
        bar = readyLabel.cget("text")
        bar += foo_rstout.name + "\n"
        readyLabel.config(text=bar)
        updateDisplay()
        # näste item
        confirmOrder()
    readyLabel.after(foo_rstout.time * 1000, update_label)
        
def system():
    for i in menu:
        buttonName = i.name + "\n" + str(i.price)
        b = tk.Button(root, text=buttonName, command= lambda item=i: addItem(item))
        b.pack(pady=10)
    confirmButton = tk.Button(root, text="Confirm order", command=confirmOrder)
    confirmButton.pack(pady=20)
    root.mainloop()
    
system()