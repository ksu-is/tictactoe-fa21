from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("Tic Tac Toe")
root.iconbitmap() #######

b1 = Button(root, text = "  ", font = ("Arial", 20), height = 3, width = 6,bg = "SystemButtonFace", command = lambda: b_click(b1))
b2 = Button(root, text = "  ", font = ("Arial", 20), height = 3, width = 6,bg = "SystemButtonFace", command = lambda: b_click(b2))
b3 = Button(root, text = "  ", font = ("Arial", 20), height = 3, width = 6,bg = "SystemButtonFace", command = lambda: b_click(b3))

b4 = Button(root, text = "  ", font = ("Arial", 20), height = 3, width = 6,bg = "SystemButtonFace", command = lambda: b_click(b4))
b5 = Button(root, text = "  ", font = ("Arial", 20), height = 3, width = 6,bg = "SystemButtonFace", command = lambda: b_click(b5))
b6 = Button(root, text = "  ", font = ("Arial", 20), height = 3, width = 6,bg = "SystemButtonFace", command = lambda: b_click(b6))

b7 = Button(root, text = "  ", font = ("Arial", 20), height = 3, width = 6,bg = "SystemButtonFace", command = lambda: b_click(b7))
b8 = Button(root, text = "  ", font = ("Arial", 20), height = 3, width = 6,bg = "SystemButtonFace", command = lambda: b_click(b8))
b9 = Button(root, text = "  ", font = ("Arial", 20), height = 3, width = 6,bg = "SystemButtonFace", command = lambda: b_click(b9))




def button(frame):          #Function to define a button
    b=Button(frame,padx=1,bg="papaya whip",width=3,text="   ",font=('arial',60,'bold'),relief="sunken",bd=10)
    return b
def change_a():             #Function to change the operand for the next player
    global a
    for i in ['O','X']:
        if not(i==a):
            a=i
            break
def reset():                #Resets the game
    global a
    for i in range(3):
        for j in range(3):
                b[i][j]["text"]=" "
                b[i][j]["state"]=NORMAL
    a=r.choice(['O','X'])
def check():                #Checks for victory or Draw
    for i in range(3):
            if(b[i][0]["text"]==b[i][1]["text"]==b[i][2]["text"]==a or b[0][i]["text"]==b[1][i]["text"]==b[2][i]["text"]==a):
                    messagebox.showinfo("Congrats!!","'"+a+"' has won")
                    reset()
    if(b[0][0]["text"]==b[1][1]["text"]==b[2][2]["text"]==a or b[0][2]["text"]==b[1][1]["text"]==b[2][0]["text"]==a):
        messagebox.showinfo("Congrats!!","'"+a+"' has won")
        reset()   
    elif(b[0][0]["state"]==b[0][1]["state"]==b[0][2]["state"]==b[1][0]["state"]==b[1][1]["state"]==b[1][2]["state"]==b[2][0]["state"]==b[2][1]["state"]==b[2][2]["state"]==DISABLED):
        messagebox.showinfo("Tied!!","The match ended in a draw")
        reset()
        
def click(row,col):
        b[row][col].config(text=a,state=DISABLED,disabledforeground=colour[a])
        check()
        change_a()
        label.config(text=a+"'s Chance")
###############   Main Program #################
root=Tk()                   #Window defined
root.title("Tic-Tac-Toe")   #Title given
a=r.choice(['O','X'])       #Two operators defined
colour={'O':"deep sky blue",'X':"lawn green"}
b=[[],[],[]]
for i in range(3):
        for j in range(3):
                b[i].append(button(root))
                b[i][j].config(command= lambda row=i,col=j:click(row,col))
                b[i][j].grid(row=i,column=j)
label=Label(text=a+"'s Chance",font=('arial',20,'bold'))
label.grid(row=3,column=0,columnspan=3)
root.mainloop()
