#import module
from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"
current_word = {}
to_learn = {}
# Create flashcard with pandas
#get the csv data
try: 
  data = pandas.read_csv(filepath_or_buffer="./flash-card-project-start/data/words_to_learn.csv")
except FileNotFoundError:
  original_data = pandas.read_csv(filepath_or_buffer="./flash-card-project-start/data/french_words.csv")
  #convert csv to dict 
  to_learn = original_data.to_dict(orient="records")
else:
  #convert csv to dict 
  to_learn = data.to_dict(orient="records")

def next_card():
  global current_word, flip_timer

  window.after_cancel(flip_timer)
  #get a random word in french and english
  current_word = random.choice(to_learn)

  #get the random french word
  french_word = current_word["French"]
  english_word = current_word["English"]

  #print the random french word  
  card.itemconfig(language_print, text="French", fill="black")  
  card.itemconfig(word_print, text=french_word, fill="black")

  card.itemconfig(card_image, image=front_card_img)

  flip_timer = window.after(3000, func=flip_card)

def flip_card():
  global current_word

  card.itemconfig(language_print, text="English", fill="white")  
  card.itemconfig(word_print, text=current_word["English"], fill="white")

  card.itemconfig(card_image, image=back_card_img)
  
  window.after_cancel(3000, func=flip_card)

def is_known():
  to_learn.remove(current_word)
  data = pandas.DataFrame(to_learn)
  data.to_csv("./flash-card-project-start/data/words_to_learn.csv", index=False)
  next_card()


# UI Design 
window = Tk()
window.title("Flashcard")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer =window.after(3000, func=flip_card)


#Create all image 
front_card_img = PhotoImage(file="./flash-card-project-start/images/card_front.png")
back_card_img = PhotoImage(file="./flash-card-project-start/images/card_back.png")

right_img = PhotoImage(file="./flash-card-project-start/images/right.png")
wrong_img = PhotoImage(file="./flash-card-project-start/images/wrong.png")

#Create card Canva 
card = Canvas(bg=BACKGROUND_COLOR, height=526, width=800, highlightthickness=0)

#add the image of the front card to the canvas
#First parameter = width, 2nd = height 
card_image = card.create_image(400, 263, image=front_card_img)

#add the language and the word of the front card to the canvas
#position are relative to the canvas 
language_print = card.create_text(400, 150, text="",fill="black" ,font=("Arial", 40, "italic"))
word_print = card.create_text(400, 263, text="", fill="black",font=("Arial", 60, "bold"))

# back_card = Label(image=front_card_img, bg=BACKGROUND_COLOR, highlightthickness=0)


#Create all button 
right_button = Button(image=right_img, highlightbackground=BACKGROUND_COLOR, highlightthickness=0, command=is_known)

wrong_button = Button(image=wrong_img, highlightbackground=BACKGROUND_COLOR, highlightthickness=0, command=next_card)


#place all widget with grid 
card.grid(column=0, columnspan=2, row=0)
right_button.grid(column=1, row=1, padx=50, pady=50)
wrong_button.grid(column=0, row=1, padx=50, pady=50)

next_card()

window.mainloop()



