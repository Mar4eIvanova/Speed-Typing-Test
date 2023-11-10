from tkinter import *
import math
import tkinter.messagebox

window = Tk()
timer = None
input_time = 60
count = 1
random_text = "chin quality wait relinquish sight like lie appendix rabbit basketball contradiction double month kid " \
              "breakfast eye bottom brainstorm depend view suppress pill marketing idea nail splurge dialect deter " \
              "delivery infinite donor climate doctor bake impound distort open challenge swear decay win conscious " \
              "president depressed ostracize inspiration install revive pass certain"


def start_timer():
    count_down(input_time)



def get_usr_input(event):
    user_text = user_input.get("1.0", "end")
    print(user_text)

def word_count(string):
    count_words = len(string.split())
    return count_words


def solve(x, g):
    xlist = x.split(" ")
    glist = g.split(" ")
    return len(list(set(xlist) & set(glist)))

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0 or count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    elif count == 0:
        user_text = user_input.get("1.0", "end")
        tkinter.messagebox.showinfo("Score", f"Yor score is {solve(random_text, user_text)}/{word_count(random_text)}")



window.title("Speed Typing")
window.geometry("700x700")
window.config(bg="bisque3")

canvas = Canvas(width=100, height=100, bg="bisque1", highlightthickness=0)
timer_text = canvas.create_text(50, 50, text="00:00", fill="black", font=("Courier", 25, "bold"))
canvas.grid(row=0, column=1)
start_button = Button(text="Start", width=10, command=start_timer, bg="bisque1")
start_button.grid(row=0, column=2)
label = Label(text=random_text, fg="black", bg="bisque1", font=("Courier", 20), wraplength=400)
label.grid(row=2, column=0, columnspan=2)
user_input = Text(window, width=40, height=34, bg="beige")
user_input.grid(row=2, column=2)

user = user_input.bind("<Return>", get_usr_input)




#("Score", f"Yor score is{solve(random_text, input_text)}/{word_count(random_text)}")

window.mainloop()
