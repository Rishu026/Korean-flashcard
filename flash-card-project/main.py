from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#f1faee"
current_card = {}
to_learn = {}
try:    
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    og_data = pandas.read_csv("data/1500_words.csv")
    to_learn = og_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient='records')
    
#print(to_learn)

def flip_card():
    canvas.itemconfig(card_title,text="English",fill ="white")
    canvas.itemconfig(card_word,text=current_card["English"],fill ="black")
    canvas.itemconfig(card_bg,image=card_back_img)
    
def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)# curr_card =  random.choice(to_learn)(Made this var global in orfer to grab it for translation and flip the card)
    
    # print(curr_card["Korean"])
    canvas.itemconfig(card_title,text ="Korean",fill='black')
    canvas.itemconfig(card_word,text =current_card["Korean"],fill = 'white')
    canvas.itemconfig(card_bg,image=card_front_img)
    flip_timer= window.after(4000,func=flip_card)
    # canvas.itemconfig(card_word, )

def is_known():
    to_learn.remove(current_card)
    next_card()
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv",index=False)

window = Tk()
window.title('Kr flashcards')
window.config(padx= 0,pady = 0, bg= BACKGROUND_COLOR)

flip_timer = window.after(4000,func=flip_card)

canvas= Canvas(width=1440, height=1024)
card_front_img = PhotoImage(file="images/untitled.png")
card_back_img = PhotoImage(file="images/Kflash.png")
card_bg = canvas.create_image(720,512,image = card_front_img)


canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
card_title = canvas.create_text(720,512,font=('Times Roman',40,"underline italic"))
card_word = canvas.create_text(720,205,font=('Times Roman',60,"bold"))
canvas.grid(row = 0,column =0,columnspan=2)
next_card()


#Now wrong is to define that the user does not know that word
cross_img = PhotoImage(file="images/wrong_1.png")
unkwon_btn = Button(image=cross_img,highlightthickness=0,command= next_card)
unkwon_btn.place(x=340, y=550)
#Now right is to define that the user does know the word and tat word will go to a seperate csv 
check_img = PhotoImage(file= "images/right_1.png")
known_btn = Button(image=check_img,highlightthickness=0,command=is_known)
known_btn.place(x=1100, y=550)
window.mainloop()