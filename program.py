import random
import tkinter as tk

def key_pressed(o):
    global letter
    letter = f"{o}"
    print(letter)
    checkcorrect()

def pick_word():
    global word
    global theme
    global length
    th = random.randint(1,2)
    if th == 1:
        theme = "animals"
        word = random.choice(animals)
        length = len(word)
    elif th == 2:
        theme = "transport"
        word = random.choice(transport)
        length = len(word)
        
def createlbl1():
    global length
    global blank
    blank = ["-" for i in range(length)]
    print(blank)
    
def checkcorrect():
    global blank
    global letter
    global word
    global strikes
    counter = 0
    x = 0
    while counter < length:
        if letter == word[counter]:
            blank[counter] = f"{letter}"
            x = 1
        counter += 1
    if x == 0:
        strikes += 1
        if strikes == 1:
            label3.config(text = f"{stage5}")
        elif strikes == 2:
            label3.config(text = f"{stage4}")
        elif strikes == 3:
            label3.config(text = f"{stage3}")
        elif strikes == 4:
            label3.config(text = f"{stage2}")
        elif strikes == 5:
            label3.config(text = f"{stage1}")
        elif strikes == 6:
            label3.config(text = f"{stage}")
    if "".join(blank) == word:
        from tkinter import messagebox
        tk.Tk().withdraw()
        messagebox.showinfo("CONGRATS", "Word guessed!")       
    label1.config(text = " ".join(blank) )
    
stage = (" ____ \n   O  ┃\n -┃- ┃ \n  /\  ┃\n _____┃")
stage1 = ("  ____ \n   O  ┃\n -┃- ┃ \n  /   ┃\n  _____┃")
stage2 = ("  _____ \n   O  ┃\n -┃- ┃ \n      ┃\n _____┃")
stage3 = ("  _____ \n   O  ┃\n -┃  ┃ \n      ┃\n _____┃")
stage4 = ("  _____\n   O  ┃\n  ┃  ┃ \n      ┃\n  _____┃")
stage5 = ("  ____ \n   O  ┃\n       ┃ \n       ┃\n _____┃")
stage6 = ("  ____ \n      ┃\n      ┃ \n      ┃\n _____┃")


transport = ['CAR', 'BUS', 'TRAIN', 'TAXI', 'PLANE', 'ELEPHANT', 'HORSE', 'CAMEL', 'SKIS', 'SNOWBOARD']
animals = ['HORSE', 'LOBSTER', 'PANDA', 'HIPPOPOTAMUS', 'WHALE', 'ZEBRA', 'GIRAFFE', 'WOLF', 'ELEPHANT', 'BONGO', 'ELEPHANT']
letter = "-"
theme = "-"
word = "-"
length = 0
blank = ["-"]
strikes = 0

pick_word()
createlbl1()

root = tk.Tk()
root.title("keyboard")

label = tk.Label(root, text = "hangman", font = ("courier new", 20))
label.pack()

label1 = tk.Label(root, text = " ".join(blank) , font = ("courier new", 10))
label1.pack()

label2 = tk.Label(root, text = f"theme : {theme}", font = ("courier new", 10))
label2.pack()

label3 = tk.Label(root, text = f"{stage6}")
label3.pack()

keys = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L','Z', 'X', 'C', 'V', 'B', 'N', 'M']

row = 1
col = 0
for key in keys:
    button = tk.Button(root, text=key, width=5, command=lambda k=key: key_pressed(k))
    button.pack(side=tk.LEFT)



root.mainloop()
