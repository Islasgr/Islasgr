import tkinter as tk
import time

def getname():
    global businessname
    businessname = entry.get()
    text2.config(text = f"current name is '{businessname}' ")
    print(businessname)

def buylemstand():
    global money
    global lemstands
    if (money - (5 * (lemstands+1))) >= 0:
        money -= (5 * (lemstands+1))
        lemstands += 1
        label.config(text = f"money: £{money}")
        label2.config(text = f"lemonade stands: {lemstands}")
        button.config(text = f"buy lemonade stand (£{(lemstands+1) * 5})")
        button4.config(text = f"sell (£{(hdstands*50)+lemstands+(pzstands*1000)})")
    else:
        from tkinter import messagebox
        tk.Tk().withdraw()
        messagebox.showinfo("ERROR", "NOT ENOUGH FUNDS")

def buyhdstand():
    global money
    global hdstands
    if (money - ((hdstands+1)*1000)) >= 0:
        money -= ((hdstands+1)*1000)
        hdstands+= 1
        label.config(text = f"money: £{money}")
        button3.config(text = f"buy hot dog stand (£{(hdstands+1)*1000})")
        label3.config(text = f"hot dog stands: {hdstands}")
        button4.config(text = f"sell (£{(hdstands*50)+lemstands+(pzstands*1000)})")
    else:
        from tkinter import messagebox
        tk.Tk().withdraw()
        messagebox.showinfo("ERROR", "NOT ENOUGH FUNDS")

def buypzstand():
    global money
    global pzstands
    if (money - ((pzstands+1)*50000)) >= 0:
        money -= ((pzstands+1)*50000)
        pzstands+= 1
        label.config(text = f"money: £{money}")
        button5.config(text = f"buy pizza stand (£{(pzstands+1)*50000})")
        label4.config(text = f"pizza stands: {pzstands}")
        button4.config(text = f"sell (£{(hdstands*50)+lemstands+(pzstands*1000)})")
    else:
        from tkinter import messagebox
        tk.Tk().withdraw()
        messagebox.showinfo("ERROR", "NOT ENOUGH FUNDS")

def sellall():
    global money
    global hdstands
    global lemstands
    money += ((hdstands*50)+lemstands+(pzstands*1000))
    label.config(text = f"money: £{money}")
    if money >= 1000000:
        goal.config(text = "goal reached! congratulations")
        from tkinter import messagebox
        tk.Tk().withdraw()
        messagebox.showinfo("well done!", "one million reached!")

def temp():
    global money
    money += 100000
    label.config(text = f"money: £{money}")

businessname = "untitled"
money = 100
lemstands = 0
hdstands = 0
pzstands = 0

if businessname == "untitled":
    root0 = tk.Tk()
    root0.title("naming screen")

    ttl = tk.Label(root0, text = "name your business", font = ("courier new", 20, "underline"))
    ttl.pack()

    label0 = tk.Label(root0, text = "name your business")
    label0.pack()

    entry = tk.Entry(root0)
    entry.pack()

    button0 = tk.Button(root0, text = "submit", command = getname)
    button0.pack()

    text = tk.Label(root0, text = "close window when done", font = ("courier new", 8))
    text.pack()

    text2 = tk.Label(root0, text = f"current name is '{businessname}' ", font = ("courier new", 10))
    text2.pack()
    
    root0.mainloop()
    
elif businessname != "untitled":
    root0.withdraw()

root = tk.Tk()
root.title(businessname)

title = tk.Label(root, text = f"{businessname}", font = ("courier new", 20, "underline"))
title.pack()

label = tk.Label(root, text = f"money: £{money}", font = ("courier new", 14))
label.pack()

goal = tk.Label(root, text = "the goal is 1,000,000", font = ("courier new", 8))
goal.pack()

divider1 = tk.Label(root, text = f"--------------lemonade--------------", font = ("courier new", 10))
divider1.pack()

button = tk.Button(root, text = f"buy lemonade stand (£{(lemstands+1)*5})", command = buylemstand, font = ("courier new", 10))
button.pack()

label2 =  tk.Label(root, text = f"lemonade stands: {lemstands}", font = ("courier new", 10))
label2.pack()

divider2 = tk.Label(root, text = f"--------------hotdogs--------------", font = ("courier new", 10))
divider2.pack()

button3 = tk.Button(root, text = f"buy hot dog stand (£{(hdstands+1)*1000})", command = buyhdstand, font = ("courier new", 10))
button3.pack()

label3 = tk.Label(root, text = f"hot dog stands: {hdstands}", font = ("courier new", 10))
label3.pack()

divider4 = tk.Label(root, text = f"----------------pizzas---------------", font = ("courier new", 10))
divider4.pack()

button5 = tk.Button(root, text = f"buy pizza stand (£{(pzstands+1)*50000})", command=buypzstand, font = ("courier new", 10))
button5.pack()

label4 = tk.Label(root, text = f"pizza stands: {pzstands}", font = ("courier new", 10))
label4.pack()

divider1 = tk.Label(root, text = f"--------------selling--------------", font = ("courier new", 10))
divider1.pack()

button4 = tk.Button(root, text = f"sell (£{(hdstands*50)+lemstands+(pzstands*1000)})", command = sellall, font = ("courier new", 14))
button4.pack()

label5 = tk.Label(root, text = f"sells from all stands", font = ("courier new", 8))
label5.pack()

root.mainloop()
