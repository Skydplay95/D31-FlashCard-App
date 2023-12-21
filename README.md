Day 31 of 100 days of Python : Create a flash card app by Angela Wu's courses

The Project of the day xas to make a flashcard app, for it we have to use GUI with Tkinter and pandas modules

The first part was to set up the user interface using the tkinter module, it was pretty easy

The second part was to make take the data in the csv file and convert it to a dict with pandas
At first i manage to make it by my own i was pretty happy
But when i was trying to flip the card it was when the difficulty show up, because i dont take the data with the orient="records"

So when i was walking throught the solution of this part, when she show the data.to_dict(orient="records"), i understand that it can help me a lot because the data was a way much more better classified. So after that is was pretty smooth

The third part was to set up the timer, it was diffulct because i dont understand how after()
and after_cancel() works so i manage to make it when she explain it during the solution path

The last part was to put all card know by the user in a different csv file, this part i manage to handle it
And alse we have to catch the exception of reading the csv file original or word_to_learn
this part was a bit tricky because i manage to catch the fist exception but not the second one which was which csv file to read
