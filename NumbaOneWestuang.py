import tkinter as tk

root = tk.Tk()
root.title("NumbaOneWestuang")

label = tk.Label(root, text="Welcome to NumbaOneWestuang")
label.pack(pady=10)

class MenuItem:
    def __init__(self, n, p):
        self.name = n
        self.price = p

burger = MenuItem("burger", 100)
cheeseburger = MenuItem("cheeseburger", 110)
menu = {burger, cheeseburger}
cart = []
cartLabel = tk.Label(root, text="Cart: ")
cartLabel.pack(pady=10)

def addItem(item):
    cart.append(item)
    updateDisplay()

def updateDisplay():
    order = "Cart: "
    price = 0
    for i in menu:
        count = cart.count(i)
        if(count > 0):
            order += i.name + "(" + str(count) + ")"
            price += i.price * count
    cartLabel.config(text=order + " \nTotal: " + str(price)+ " ")

def system():
    for i in menu:
        buttonName = i.name + "\n" + str(i.price)
        b = tk.Button(root, text=buttonName, command=lambda item=i: addItem(item))
        b.pack(pady=10)
    root.mainloop()
    
system()