# import Modules

import tkinter as tk
from tkinter import messagebox, Button
from random  import randint
from time import sleep
from character import *

#CREATE MAIN WINDOW
root = tk.Tk()

root.title("Hare and Turtle Race")
root.configure(bg='gray')
canvas = tk.Canvas(root, bg="ivory2", width=600, height=352)
canvas.pack()
play_btn = tk.PhotoImage(file='reloading.png')


###############  METHODS  ##################################

# RESTART BTN
def restart(state):
    if state == False:
        restart_button = Button(root, image=play_btn, command=start_race, borderwidth=2)
        restart_button.place(x=40, y=0)
    
        
        
# game functionalities
def start_race():
    turtle_img = tk.PhotoImage(file="turtle.png")
    hare_image = tk.PhotoImage(file="Hare.png")
    turtle = character(canvas, 0, 284, tk.NW, turtle_img)
    hare = character(canvas, 0, 304, tk.NW, hare_image)
    
    turtle_prog = icon(canvas,0,70,15, 85,'#b8d8be', "turt")
    hare_prog = icon(canvas, 0,120,15, 105 ,'#FDFD96', "rabit")
    
    
    # INTIALIZATIONS
    hare_position = 0
    turtle_position = 0
    checker =  True
    
    # TIMER
    color = ["Green","Yellow","Red"]
    for i in reversed(range(3)):
        canvas.create_text(275, 135, text=i+1, anchor=tk.NW, font=('arial black',64, 'bold'), tags="count",fill=color[i] )
        root.update()
        canvas.delete("count")
        sleep(1)
        if  i == 0:
            canvas.create_text(205, 135, text="GO!!", anchor=tk.NW, font=('arial black',64, 'bold'), tags="count",fill="WHITE" )
            root.update()
            sleep(.15)
            canvas.delete("count")
    
    # loop
    while checker:
        #  character steps
        turtle_step = randint(1,2)
        hare_step = randint(-15, 8)
        
        # IF CONDITION  FOR HARE MOVEMENT STOPS AND GO
        if hare_step > 0:
            hare.move(hare_step)
            hare_prog.move(hare_step)
            hare_position += hare_step
        
        # TURTLE MOVEMENT
        turtle_position += turtle_step
        turtle.move(turtle_step)
        turtle_prog.move(turtle_step)

        # COORDINATE TRACKER IN CLI
        print(f"Hare: {hare_position} - Turtle: {turtle_position}")
        root.update()
        sleep(.01)
        
        
        # WNNING CONDITION
        if hare_position >= 550 and turtle_position >= 550:
            canvas.create_text(105, 135, text="Its a Draw!", anchor=tk.NW, font=('arial black',48, 'bold'), tags="results",fill="orange" )
            root.update()
            sleep(1)
            canvas.delete("turt", "rabit", "results")
            # messagebox.showinfo("Race Result", "Its a Draw!")
            restart(True)
            return False 
        elif turtle_position >= 550:
            canvas.create_text(105, 135, text="Turtle Wins!", anchor=tk.NW, font=('arial black', 48, 'bold'), tags="results",fill="#1c352d" )
            root.update()
            sleep(1)
            canvas.delete("turt", "rabit", "results")
            # messagebox.showinfo("Race Result", "Turtle Wins!")
            restart(False)
            return False
        elif hare_position >= 550:
            canvas.create_text(105, 135, text="Hare Wins!", anchor=tk.NW, font=('arial black',48, 'bold'), tags="results",fill="#ffd700" )
            root.update()
            sleep(1)
            canvas.delete("turt", "rabit", "results")
            # messagebox.showinfo("Race Result", "Hare wins!")     
            restart(False)
            return False
        
        
# MAIN FUNCTION
def main():
    # ON CLICK
    def onClikc():
        start_button['state'] = 'disabled' 
        start_race()

    # DISPLAY
    bg_img = tk.PhotoImage(file="set.png")
    turtleface = tk.PhotoImage(file="turtle_face.png")
    rabbitface = tk.PhotoImage(file="rabbit.png")
    title = tk.PhotoImage(file="title.png")
    canvas.create_image(0, 0,anchor=tk.NW, image=bg_img)
    canvas.create_image(185, 0,anchor=tk.NW, image=title)
    
    canvas.create_image(50, 65,anchor=tk.NW, image=turtleface)
    canvas.create_image(45, 95,anchor=tk.NW, image=rabbitface)
    
    canvas.create_text(5, 60, text="Turtle", anchor=tk.NW, font=('arial black', 10, 'bold'))
    canvas.create_text(5, 95, text="Hare", anchor=tk.NW, font=('arial black', 10, 'bold'))
    
    canvas.create_oval(555,75,565,84,fill='green', outline="")
    canvas.create_oval(555,119,565,110,fill='ivory2', outline="")
    
    canvas.create_rectangle(0,75,560, 85, fill="green", outline="")   
    canvas.create_rectangle(0,120,560, 110 , fill="ivory2", outline="") 
    
    finish = tk.PhotoImage(file="finish.png")
    character(canvas, 496, 280, tk.NW, finish)
    
    # BUTTON SECTION
    play_btn = tk.PhotoImage(file='play-button.png')
    start_button = Button(root, image=play_btn, command=onClikc)             
    start_button.place(x=0, y=0)
    
    
    
    

    
    

    root.mainloop()

if __name__ == "__main__":
    main()
    

